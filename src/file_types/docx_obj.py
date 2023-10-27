import dataclasses
import datetime
import shutil

import docx

from src.file_types.base_file_object import BaseFileObject
from src.tools.files import get_filename, get_unique_filename
from src.tools.notification import notify


@dataclasses.dataclass
class DocXObject(BaseFileObject):
    file: str

    def __post_init__(self):
        self.docx_file = docx.Document(self.file)
        self.docx_props = dir(self.docx_file.core_properties)
        self.metadata_list = [
            prop for prop in self.docx_props if not prop.startswith("_")
        ]
        self.metadata_dict = {
            prop: getattr(self.docx_file.core_properties, prop)
            for prop in self.docx_props
            if not prop.startswith("_")
        }

    def present_metadata_list(self):
        return self.metadata_list

    def present_metadata_dict(self):
        return self.metadata_dict

    @notify("Delete all metadata")
    def delete_all_metadata(self):
        for prop_name, _ in self.metadata_dict.items():
            if prop_name == "revision":
                continue
            self.metadata_dict[prop_name] = ""

    @notify("Change metadata field")
    def change_metadata_field(self, key: str, value: str) -> None:
        """Any field can be added, but if field is not necessary for docx file
        it won't be added"""

        self.metadata_dict[key] = value

    def update_file_properties(self, docx_file):
        """Set new metadata to a modified file"""

        for prop_name, value in self.metadata_dict.items():
            try:
                setattr(
                    docx_file.core_properties,
                    prop_name,
                    int(value) if isinstance(value, int) else value,
                )
            except ValueError:
                setattr(docx_file.core_properties, prop_name, datetime.datetime.min)

    @notify("Saving file into modified_files folder")
    def save_file(self) -> None:
        """Saves modified file"""

        name, fmt = get_filename(self.file).rsplit(".")
        filename = get_unique_filename(name, fmt)
        shutil.copy(self.file, filename)
        self.update_file_properties(docx.Document(filename))

import dataclasses

from exif import Image

from src.file_types.base_file_object import BaseFileObject
from src.tools.files import get_unique_filename, get_filename
from src.tools.notification import notify


@dataclasses.dataclass
class ImageObject(BaseFileObject, Image):
    file: str

    def __post_init__(self):
        self.image_file = Image(self.file)
        self.metadata_list = self.image_file.list_all()
        self.metadata_dict = self.image_file.get_all()

    def present_metadata_list(self) -> list[str]:
        return self.metadata_list

    def present_metadata_dict(self) -> dict[str, str]:
        return self.metadata_dict

    @notify("Saving file into modified_files folder")
    def save_file(self) -> None:
        """Saves modified file"""

        self.get_modified_image()

    @notify("Change metadata field")
    def change_metadata_field(self, key: str, value: str) -> None:
        self.metadata_dict[key] = value
        self.image_file.set(key, value)

    @notify("Delete all metadata")
    def delete_all_metadata(self) -> None:
        self.image_file.delete_all()
        self.metadata_list.clear(), self.metadata_dict.clear()

    def get_modified_image(self) -> None:
        """Save modified image in a folder.
        Now its called modified_files and based on the same
        level as deleter starter"""

        name, fmt = get_filename(self.file).rsplit(".")
        filename = get_unique_filename(name, fmt)
        with open(filename, 'wb') as new_image_file:
            new_image_file.write(self.image_file.get_file())

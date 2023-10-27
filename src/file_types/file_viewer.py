import dataclasses

from src.file_types.base_file_object import BaseFileObject
from src.tools.print_colorful import print_colorful


@dataclasses.dataclass
class FileViewer:
    file: BaseFileObject

    def __post_init__(self):
        self.no_metadata_msg = "No metadata were found"

    def detailed_metadata_info(self) -> None:
        """Represent metadata keys and values if a format:
        Metadata_key    Metadata_value
        ...             ...
        """

        detailed_metadata = "\n".join(
            [f"{k}  -->  {v}" for k, v in self.file.present_metadata_dict().items()]
        )
        print_colorful("Here is metadata with fields", "blue")
        print_colorful(detailed_metadata or self.no_metadata_msg, "green")

    def metadata_info(self) -> None:
        """Represent metadata keys in a format:
        Metadata_key1
        Metadata_key2
        ...
        """
        metadata_list = "\n".join(
            self.file.present_metadata_list(),
        )
        print_colorful("Here's metadata I have found", "blue")
        print_colorful(metadata_list or self.no_metadata_msg, "green")

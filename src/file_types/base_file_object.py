from abc import ABC, abstractmethod


class BaseFileObject(ABC):
    """Base class for all supported file types"""

    @property
    @abstractmethod
    def present_metadata_list(self):
        ...

    @property
    @abstractmethod
    def present_metadata_dict(self):
        ...

    @abstractmethod
    def delete_all_metadata(self):
        ...

    @abstractmethod
    def change_metadata_field(self, key: str, value: str) -> None:
        ...

    @abstractmethod
    def save_file(self) -> None:
        ...

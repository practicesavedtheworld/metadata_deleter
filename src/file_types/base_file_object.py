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



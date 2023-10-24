import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent

def get_unique_filename(name: str, fmt: str) -> str:
    """Checks if the filename exists, if it does, appends an integer affix
    until the filename is unique."""

    filename = f"{ROOT}/modified_files/new_{name}.{fmt}"
    name_already_taken = os.path.isfile(filename)
    if name_already_taken:
        num = 1
        while name_already_taken:
            filename = f"{ROOT}/modified_files/new_{name}({num}).{fmt}"
            name_already_taken = os.path.isfile(filename)
            num += 1

    return filename


def get_filename(path: str | os.PathLike) -> str:
    splitter = "/"
    if sys.platform.startswith("win"):
        splitter = "\\"
    _, filename = str(path).rsplit(splitter, 1)
    return filename
import os
import sys
from pathlib import Path

import docx  # type: ignore
from PIL import Image, UnidentifiedImageError

from src.constants import NOT_IMAGE

ROOT = Path(__file__).parent.parent.parent


def do_nothing(sig, sig_frame):
    pass


def get_image_format(path: str) -> str | NOT_IMAGE:
    """Using PIL try opening file and define format."""
    try:
        img = Image.open(path)
        return img.format
    except UnidentifiedImageError:
        return NOT_IMAGE  # type: ignore


def is_docx(path: str) -> bool:
    """Basic checking docx file.
    Return True if it is docx else False."""
    _, fmt = path.rsplit(".", 1)
    if fmt.startswith("doc"):
        try:
            docx.Document(path)
            return True
        except Exception as doc_err:  # TODO find exc
            # TODO log that
            pass
    return False


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

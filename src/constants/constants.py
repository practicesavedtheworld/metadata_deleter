from typing import TypeAlias

IMAGE_TYPES = (
    "rgb",
    "gif",
    "pbm",
    "pgm",
    "ppm",
    "tiff",
    "rast",
    "xbm",
    "jpeg",
    "bmp",
    "png",
    "webp",
    "exr",
    "svg",
)

COMMANDS = {
    ("help", "-h"): "help",
    ("change", "-c"): "change",
    ("delete", "-d"): "delete",
    ("metadata", "-m"): "metadata",
    ("metadata-detailed", "-md"): "metadata-detailed",
    ("save", "-s"): "save",
}

NOT_IMAGE: TypeAlias = None

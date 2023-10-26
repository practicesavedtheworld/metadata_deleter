import os.path
import sys
import signal

from src.constants import IMAGE_TYPES
from src.file_types.docx_obj import DocXObject
from src.file_types.image import ImageObject
from src.tools.commands import CommandHandler
from src.tools.files import get_filename, get_image_format, do_nothing, is_docx
from src.tools.print_colorful import print_colorful
from src.file_types.file_viewer import FileViewer


def main():
    while True:
        print_colorful("choose file", "blue")
        file_path = sys.stdin.readline().strip()
        if not os.path.exists(file_path) or os.path.isdir(file_path):
            print_colorful(
                f"Nothing found in {file_path}. File does not exist.\nTry again or "
                "Ctrl+Z for exit",
                "red",
            )
            continue
        print_colorful(f"Working with {file_path}", "green")
        print_colorful(f"Defining file type...", "blue")
        # TODO transfer into imageObj

        # Based on file type creates different instances
        if get_image_format(file_path) is not None and (
                get_image_format(file_path).lower() in IMAGE_TYPES
        ):
            mod_file = ImageObject(file_path)
        elif is_docx(file_path):
            mod_file = DocXObject(file_path)
        else:
            print_colorful("UNSUPPORTED TYPE DETECTED. Try again or "
                           "Ctrl+Z for exit", "red")
            continue

        file_viewer = FileViewer(mod_file)
        file_viewer.metadata_info()

        print_colorful(
            f"Delete some metadata?"
            f"Or change some field?\nType help to see what command is available"
            f"\nCtrl+Z for exit\n\n",
            "blue",
        )
        command = sys.stdin.readline().strip()
        while True:
            CommandHandler(command, mod_file)
            command = sys.stdin.readline().strip()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, do_nothing)
    main()

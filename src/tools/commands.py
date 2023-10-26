import dataclasses
import sys
from typing import Never

from src.file_types.base_file_object import BaseFileObject
from src.file_types.file_viewer import FileViewer
from src.constants import COMMANDS
from src.tools.print_colorful import print_colorful


def unacceptable_command(arg=Never) -> None: ...


@dataclasses.dataclass
class CommandHandler:
    command: str
    file: BaseFileObject

    def __post_init__(self):
        self.file_viewer = FileViewer(self.file)
        self.execute_command(self.command)
        print_colorful("Wait some command...", "blue")

    @staticmethod
    def available_commands() -> None:
        """Show list of all available command"""

        commands = "\n".join([", ".join(k) for k in COMMANDS.keys()])
        print_colorful("Here is all available commands\n", "blue")
        print_colorful(commands, "green")

    def execute_command(self, command: str):
        """Execute user command."""

        for cmd in COMMANDS.keys():
            if any([
                command == cmd[0],
                command == cmd[1],
            ]):
                match COMMANDS.get(cmd):
                    case "help":
                        self.available_commands()
                    case "delete":
                        print_colorful("Starting delete all file metadata...", "cyan")
                        self.file.delete_all_metadata()
                    case "change":
                        print_colorful("Select field and set the field value\n"
                                       "Change carefully\n"
                                       "Example: field value\n", "blue")
                        self.file_viewer.detailed_metadata_info()
                        change_command = sys.stdin.readline().strip()

                        # Change command requires two params.
                        # If it's not you'll be noticed.
                        try:
                            field, value = change_command.split(" ", 1)
                            self.file.change_metadata_field(field.strip(), value.strip())
                        except ValueError:
                            # TODO log that
                            print_colorful("NOT ENOUGH PARAMETERS. IT SHOULD BE 2", "red")
                    case "metadata":
                        self.file_viewer.metadata_info()
                    case "metadata-detailed":
                        self.file_viewer.detailed_metadata_info()
                    case "save":
                        self.file.save_file()
                    case _:
                        # This should never be executed
                        unacceptable_command()
                break
        else:
            print_colorful(f"Command -> '{command}' does not exist. "
                           "Type help for more commands", "red")

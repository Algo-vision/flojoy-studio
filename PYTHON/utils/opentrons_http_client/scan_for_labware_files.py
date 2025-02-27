import pathlib


def scan_for_labware_files(labware_directory: pathlib.Path) -> list[pathlib.Path]:
    if not labware_directory.is_dir():
        raise FileNotFoundError("THe specified paht is not a directory")
    files = [file for file in labware_directory.glob("*.json")]
    return files

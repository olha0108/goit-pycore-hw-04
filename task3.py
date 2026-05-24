import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def directory_structure(path, prefix=""):
    for item in path.iterdir():
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}{item.name}/")
            directory_structure(item, prefix + "    ")
        else:
            print(f"{prefix}{Fore.GREEN}{item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hw03.py <directory_path>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    if not directory_path.exists():
        print("Directory not found")
        sys.exit(1)

    print(f"{Fore.YELLOW}Directory structure of {directory_path}:")
    directory_structure(directory_path)

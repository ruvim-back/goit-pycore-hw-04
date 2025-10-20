from pathlib import Path
from colorama import init, Fore, Style
import sys

def print_tree(path: Path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.CYAN + item.name + "/" + Style.RESET_ALL)
            print_tree(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + item.name + Style.RESET_ALL)

if __name__ == "__main__":
    init(autoreset=True)

    if len(sys.argv) < 2:
        print("Використання: python task3.py <шлях_до_директорії>")
        sys.exit(1)

    root = Path(sys.argv[1])

    if not root.exists() or not root.is_dir():
        print("Некоректний шлях або це не директорія!")
        sys.exit(1)

    print(Fore.CYAN + root.name + "/" + Style.RESET_ALL)
    print_tree(root)

import os

def print_directory_contents(path='/New folder'):
    try:
        print(f"Contents of directory '{path}':")
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"[FILE] {entry.name}")
                elif entry.is_dir():
                    print(f"[DIR ] {entry.name}")
                else:
                    print(f"[OTHER] {entry.name}")
    except FileNotFoundError:
        print("Directory not found.")
    except PermissionError:
        print("Permission denied.")

if __name__ == "__main__":
    print_directory_contents('.')

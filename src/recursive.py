import os
import shutil

def make_abs_dir(relative_dir: str) -> str:
    return os.path.abspath(relative_dir)

def static_to_public(static_path: str, public_path: str) -> None:

    if not os.path.exists(public_path):
        os.mkdir(public_path)
    else:
        shutil.rmtree(public_path)
        os.mkdir(public_path)

    recursive_copy(static_path, public_path)
    return 


def recursive_copy(source: str, destination: str) -> None:

    if not os.path.isdir(source):
        return

    if not os.path.exists(destination):
        os.mkdir(destination)

    for directory in os.listdir(source):
        full_path = os.path.join(source, directory)
        full_dest_path = os.path.join(destination, directory)

        if os.path.isdir(full_path):
            print(f"New path: {full_path}")
            recursive_copy(full_path, full_dest_path)

        if os.path.isfile(full_path):
            print(f"moving file: {full_path}")
            shutil.copy(full_path, full_dest_path)

if __name__ == "__main__":
    static_to_public(make_abs_dir("./static"), make_abs_dir("./public"))



import os
import shutil
import argparse


def flatten_directory(source_dir, destination_dir):
    """
    Flattens the folder structure by copying all .py files, except __init__.py, 
    from nested directories into a single destination directory. 
    Clears the destination directory if it exists before copying.

    :param source_dir: Path to the source directory
    :param destination_dir: Path to the destination directory
    """

    # Clear the destination directory if it exists
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.makedirs(destination_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            # Only process .py files and exclude __init__.py
            if file.endswith(".py") and file != "__init__.py":
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_dir, file)
                
                # Rename the file if it already exists in the destination
                counter = 1
                while os.path.exists(destination_file):
                    name, ext = os.path.splitext(file)
                    destination_file = os.path.join(destination_dir, f"{name}_{counter}{ext}")
                    counter += 1
                
                shutil.copy2(source_file, destination_file)
                print(f"Copied: {source_file} -> {destination_file}")


def main():
    parser = argparse.ArgumentParser(description="Flatten directory by copying all .py files into a single directory.")
    parser.add_argument("--src", required=True, help="Source directory path")
    parser.add_argument("--dest", required=True, help="Destination directory path")
    args = parser.parse_args()

    try:
        flatten_directory(args.src, args.dest)
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    main()

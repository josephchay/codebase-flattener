import os
import shutil
import argparse


def flatten_directory(source_dir, destination_dir, include_init=False):
    """
    Flattens the folder structure by copying all .py files into a single destination directory.
    Files are prefixed with their parent directory names separated by double hyphens.
    
    :param source_dir: Path to the source directory
    :param destination_dir: Path to the destination directory
    :param include_init: Whether to include __init__.py files (default: False)
    """

    # Clear the destination directory if it exists
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.makedirs(destination_dir)

    source_dir_parts = len(os.path.normpath(source_dir).split(os.sep))

    for root, _, files in os.walk(source_dir):
        for file in files:
            # Filter Python files based on include_init parameter
            if file.endswith(".py"):
                if not include_init and file == "__init__.py":
                    continue
                
                source_file = os.path.join(root, file)
                
                # Get the relative path components after the source directory
                path_parts = os.path.normpath(root).split(os.sep)[source_dir_parts:]
                
                # Create the new filename with directory prefixes
                if path_parts:
                    new_filename = "__".join(path_parts + [file])
                else:
                    new_filename = file
                    
                destination_file = os.path.join(destination_dir, new_filename)
                
                # Rename the file if it already exists in the destination
                counter = 1
                original_dest_file = destination_file
                while os.path.exists(destination_file):
                    name, ext = os.path.splitext(original_dest_file)
                    destination_file = f"{name}_{counter}{ext}"
                    counter += 1
                
                shutil.copy2(source_file, destination_file)
                print(f"Copied: {source_file} -> {destination_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Flatten directory by copying all .py files into a single directory."
    )
    parser.add_argument("--src", 
                        required=True, 
                        help="Source directory path")
    parser.add_argument("--dest", 
                        required=True, 
                        help="Destination directory path")
    parser.add_argument("--include-init",
                        action="store_true",
                        help="Include __init__.py files in the flattening process (default: False)")

    args = parser.parse_args()

    try:
        flatten_directory(args.src, args.dest, args.include_init)
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    main()

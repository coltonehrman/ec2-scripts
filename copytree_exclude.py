import os
import shutil
import subprocess

def copytree_exclude(src, dst, exclude_dirs):
    """
    Copy a directory and its contents, excluding specified directories.
    
    :param src: Source directory to copy.
    :param dst: Destination directory where the copy will be created.
    :param exclude_dirs: List of directory names to exclude from the copy.
    """
    if os.path.exists(dst):
        print(f"Removing {dst}")
        shutil.rmtree(dst)
        print(f"Successfully removed {dst}")

    os.makedirs(dst)

    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, item)

        if os.path.isdir(src_item):
            if item in exclude_dirs:
                continue  # Skip the directory specified in exclude_dirs
            print(f"Copying folder into {dst_item}")
            shutil.copytree(src_item, dst_item)
        else:
            print(f"Copying files into {dst_item}")
            shutil.copy2(src_item, dst_item)  # Copy files
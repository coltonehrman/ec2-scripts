#!/usr/bin/env python

import os
import subprocess
from copytree_exclude import copytree_exclude

if "TMP" not in os.environ:
    raise Exception("Missing TMP environment variable!")

project_folder = "budget-app"
tmp_dir = os.environ["TMP"]
tmp_project_path = os.path.join(tmp_dir, project_folder)
home_dir = os.environ["HOME"]
home_project_path = os.path.join(home_dir, project_folder)

cwd = os.getcwd()
print(f"TMP={tmp_dir}\nHOME={home_dir}")
print(f"Current working directory={cwd}")
print()

def check_tmp_project_and_delete():
    # Check if the file exists & delete it
    if os.path.exists(tmp_project_path):
        print(f"Removing {tmp_project_path}")
        subprocess.run(f"rm -rf {tmp_project_path}", shell=True)
        print(f"Successfully removed {tmp_project_path}")
        print()
    else:
        print(f"File '{tmp_project_path}' does not exist.")

check_tmp_project_and_delete()

def clone(repo):
    clone_cmd = f"git clone --depth=1 --branch=main {repo}"

    print(f"Cloning repo from {repo}")
    subprocess.run(clone_cmd, shell=True, cwd=tmp_dir)
    print(f"Successfully cloned repo from {repo}")
    print()

def install(path):
    install_cmd = f"npm install"

    print(f"Installing project {path}")
    subprocess.run(install_cmd, shell=True, cwd=path)
    print(f"Successfully installed project {path}")
    print()

def build(path):
    build_cmd = f"npm run build"

    print(f"Building project {path}")
    subprocess.run(build_cmd, shell=True, cwd=path)
    print(f"Successfully built project {path}")
    print()

def run_vite(path):
    run_cmd = f"npx vite preview --host 0.0.0.0 --port 443"

    print(f"Running vite project {path}")
    subprocess.run(run_cmd, shell=True, cwd=path)

# Run the shell command in the specified directory and capture the output
try:
    repo = f"https://github.com/coltonehrman/{project_folder}.git"
    
    clone(repo=repo)

    copytree_exclude(tmp_project_path, home_project_path, [".git"])
    
    install(home_project_path)
    build(home_project_path)
    run_vite(home_project_path)
except subprocess.CalledProcessError as e:
    print(f"Command failed with error: {e}")
except Exception as e:
    print(f"Error: {e}")

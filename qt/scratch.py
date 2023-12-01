import subprocess
import sys
import os

def open_file_explorer(path):
    # Make sure the path is absolute
    absolute_path = os.path.abspath(path)

    if sys.platform.startswith('darwin'):
        # For macOS
        subprocess.run(['open', absolute_path])
    elif sys.platform.startswith('win32'):
        # For Windows
        subprocess.run(['explorer', absolute_path])

# Example path
path_to_open = "/Documents"  # Replace with your path
path_to_open = os.getcwd()
print(f'current working directory{path_to_open}')
open_file_explorer(path_to_open)

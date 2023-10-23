# This script is designed to parse and extract the filenames of any thumbnail files present within a Linux user account.
# These files are typically located within $HOME/.cache/thumbnails.
# Running the script, and then giving it the path to the thumbnail directory will result in a text file being produced in the same directory as the script was run from, which will contain the subfolder and filename details of the thumbnail files present.

import os

# Prompt the user for the path of the thumbnail directory of interest. User should enter something like /home/user/.cache/thumbnails
directory_path = input("Enter the directory path: ")

# Check if the specified directory exists
if not os.path.exists(directory_path):
    print("Directory does not exist.")
    exit(1)

# Specify the output file's filenames
output_file = 'filenames.txt'

# Recursively collect filenames from sub-directories (normal, large, x-large etc.)
def collect_filenames(directory):
    filenames = []
    for root, _, files in os.walk(directory):
        for file in files:
            filenames.append(os.path.relpath(os.path.join(root, file), directory))
    return filenames

# List filenames from the specified directory and its subdirectories
try:
    filenames = collect_filenames(directory_path)
except OSError as e:
    print(f"Error: {e}")
    exit(1)

# Make text file for writing
with open(output_file, 'w') as file:
    # Write each filename to the text file, one per line
    for filename in filenames:
        file.write(filename + '\n')

print(f"Filenames have been written to '{output_file}'.")

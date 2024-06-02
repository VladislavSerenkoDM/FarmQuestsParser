import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# List all files in the directory
files_in_directory = os.listdir(script_dir)

# Print the names of the files without their extensions
for file_name in files_in_directory:
    if os.path.isfile(os.path.join(script_dir, file_name)):
        # Split the file name into the base name and the extension
#        base_name, _ = os.path.splitext(file_name)
        print(file_name)

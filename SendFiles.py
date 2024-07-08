import os
import shutil


def copy_files(src_directory, dest_directory):
    """Copy all files from the source directory to the destination directory."""

    # Copy files from src_directory to dest_directory
    for filename in os.listdir(src_directory):
        src_file = os.path.join(src_directory, filename)
        dest_file = os.path.join(dest_directory, filename)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dest_file)

if __name__ == '__main__':
    dest_directory = 'C:/PlayrixHS/homescapes/base_mm/events/FarmingLocation/FarmLocation5/Preload/Quests'  # Replace with the path to your source directory
    src_directory = 'C:/PlayrixHS/temp/Farm/ScriptRepo/FarmQuestsParser/output'  # Replace with the path to your destination directory

    # Ensure the destination directory exists
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    copy_files(src_directory, dest_directory)
    print(f'Files copied from {src_directory} to {dest_directory}')

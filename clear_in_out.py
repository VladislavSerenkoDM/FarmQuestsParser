import os
import shutil

def clear_folder(folder_path):
    # Check if the folder exists
    if os.path.exists(folder_path):
        # Iterate over all the files and folders in the specified folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                # Check if it is a file or a directory
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Remove file or link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove directory and its contents
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        print(f'The folder {folder_path} does not exist.')

def main():
    input_folder = 'input'
    output_folder = 'output'

    clear_folder(input_folder)
    clear_folder(output_folder)

if __name__ == '__main__':
    main()
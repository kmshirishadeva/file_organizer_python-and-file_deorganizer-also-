import os
import shutil

def deorganize_files(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # List all subdirectories in the given directory
    subdirectories = [os.path.join(directory, d) for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

    for subdirectory in subdirectories:
        # List all files in the subdirectory
        files = os.listdir(subdirectory)
        for file in files:
            # Move files to the parent directory
            src = os.path.join(subdirectory, file)
            dst = os.path.join(directory, file)
            shutil.move(src, dst)
            print(f"Moved {file} from {subdirectory} to {directory}")

        # Remove the now-empty subdirectory
        os.rmdir(subdirectory)
        print(f"Deleted empty folder: {subdirectory}")

if __name__ == "__main__":
    # Specify the directory to deorganize
    directory_to_deorganize = input("Enter the path of the directory to deorganize: ")
    deorganize_files(directory_to_deorganize)

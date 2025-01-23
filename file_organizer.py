import os
import shutil

# Define the file categories and their extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav'],
    'Others': []  # Files that don't fall into any category
}

def organize_files(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # List all files in the directory
    files = os.listdir(directory)

    for file in files:
        file_path = os.path.join(directory, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file's extension
        _, ext = os.path.splitext(file)
        ext = ext.lower()  # Convert to lowercase for consistency

        # Find the appropriate category for the file
        category = 'Others'  # Default category
        for folder, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                category = folder
                break

        # Create the category folder if it doesn't exist
        category_folder = os.path.join(directory, category)
        os.makedirs(category_folder, exist_ok=True)

        # Move the file to the category folder
        dest_path = os.path.join(category_folder, file)
        shutil.move(file_path, dest_path)
        print(f"Moved '{file}' to '{category_folder}'")

if __name__ == "__main__":
    # Specify the directory to organize
    directory_to_organize = input("Enter the path of the directory to organize: ")
    organize_files(directory_to_organize)

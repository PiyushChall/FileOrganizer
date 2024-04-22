import os
import shutil
import json

with open("Categories.json") as f:
    categories = json.load(f)

    
def organize_files(folder_path):
    for item in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, item)):
            file_name, file_extension = os.path.splitext(item)
            file_extension = file_extension.lower()

            moved = False
            for category, extensions in categories.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(folder_path, category)
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    shutil.move(os.path.join(folder_path, item), os.path.join(destination_folder, item))
                    moved = True
                    break

            if not moved:
                destination_folder = os.path.join(folder_path, "Others")
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                shutil.move(os.path.join(folder_path, item), os.path.join(destination_folder, item))


if __name__ == "__main__":
    folder_path = input("Enter the folder path to organize files: ")
    organize_files(folder_path)
    print("Files organized successfully!")

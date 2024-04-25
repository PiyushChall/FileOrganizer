import os
import tkinter
import customtkinter
import shutil
import json

with open("Categories.json") as f:
    categories = json.load(f)

# Appearance
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
app = tkinter.Tk()
app.geometry("720x480")
app.title("File Organizer")
app.configure(bg="#49243E")


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


def organize_file():
    try:
        file_path = path_input.get()
        title.configure(text=file_path, text_color="#DBAFA0")
        organized.configure(text="")
        organize_files(file_path)
        organized.configure(text=" Organized ", text_color="green")
    except:
        organized.configure(text=" Oops Invalid file path ", text_color="red")


title = customtkinter.CTkLabel(app, text=" Feed me the file path ", text_color="#DBAFA0")
title.pack(padx=10, pady=10)

path = tkinter.StringVar()
path_input = customtkinter.CTkEntry(app, width=350, height=50, textvariable=path, fg_color="#FFB1B1")
path_input.pack()


organized = customtkinter.CTkLabel(app, text="")
organized.pack()

organize_button = customtkinter.CTkButton(app, text=" Organize ", command=organize_file, fg_color="#DBAFA0", hover_color="#EFBC9B")
organize_button.pack(padx=10, pady=10)


app.mainloop()

import os
import time
import tkinter as tk
from tkinter import filedialog

def create_numbered_folders(base_name, count, parent_dir='.'):
    """
    Create a series of numbered folders.

    :param base_name: The base name for the folders.
    :param count: The number of folders to create.
    :param parent_dir: The parent directory where the folders will be created.
    """
    for i in range(1, count + 1):
        folder_name = f"{base_name}{i}"
        folder_path = os.path.join(parent_dir, folder_name)
        try:
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        except FileExistsError:
            print(f"Folder already exists: {folder_path}")
        except Exception as e:
            print(f"An error occurred while creating folder {folder_path}: {e}")

def browse_for_directory():
    """
    Open a file dialog for the user to select a directory.
    """
    root = tk.Tk()
    print("now choose a directory")
    root.withdraw()  # Hide the main window

    # Ask the user to select a directory
    selected_dir = filedialog.askdirectory()
    return selected_dir

def get_base_name():
    """
    Prompt the user to enter the base name for the folders.
    """
    base_name = input("Enter the base name for the folders: ")
    return base_name

# ASCII art
print("""
 cat MEOW!
┈┈╱╲┈┈┈╱╲┈┈╭━╮┈
┈╱╱╲╲__╱╱╲╲┈╰╮┃┈
┈▏┏┳╮┈╭┳┓▕┈┈┃┃┈
┈▏╰┻┛▼┗┻╯▕┈┈┃┃┈
┈╲┈┈╰┻╯┈┈╱▔▔┈┃┈
┈┈╰━┳━━━╯┈┈┈┈┃┈
┈┈┈┈┃┏┓┣━━┳┳┓┃┈
┈┈┈┈┗┛┗┛┈┈┗┛┗┛┈

""")

base_name = get_base_name()
parent_dir = browse_for_directory()

if parent_dir:
    create_numbered_folders(base_name=base_name, count=10, parent_dir=parent_dir)

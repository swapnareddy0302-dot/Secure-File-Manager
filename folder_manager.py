import os
from logger import log_action
import shutil

def create_folder(folder_name):
    """Creates a new folder."""
    print("Creating a folder")

    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
        log_action("CREATE_FOLDER", folder_name, "SUCCESS")
        return True

    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")
        log_action("CREATE_FOLDER", folder_name, "FAILURE")
        return False
    except OSError as e:
        print(e)
        log_action("CREATE_FOLDER", folder_name, "FAILURE")
        return False   

def delete_folder(folder_name):
    """Deletes an existing folder."""
    print("Deleting a folder")

    try:
        shutil.rmtree(folder_name)
        choice = input("do you want to delete the folder? (y/n): ")
        if choice.lower() == 'y':
            print(f"Folder '{folder_name}' deleted successfully.")
            log_action("DELETE_FOLDER", folder_name, "SUCCESS")
            return True
        else:
            print(f"Folder '{folder_name}' was not deleted.")
            return False

    except FileNotFoundError:
        print(f"Folder '{folder_name}' does not exist.")
        log_action("DELETE_FOLDER", folder_name, "FAILURE")
        return False
    except OSError as e:
        print(e)
        log_action("DELETE_FOLDER", folder_name, "FAILURE")
        return False        
def copy_folder(source_folder, destination_folder):
    """Copies a folder from the source path to the destination path."""
    try:
        shutil.copytree(source_folder, destination_folder)
        print(f"Folder copied from '{source_folder}' to '{destination_folder}' successfully.")
        log_action("COPY_FOLDER", f"{source_folder} to {destination_folder}", "SUCCESS")
        return True
    except FileExistsError:
        print(f"Destination folder '{destination_folder}' already exists.")
        log_action("COPY_FOLDER", f"{source_folder} to {destination_folder}", "FAILURE")
        return False
    except FileNotFoundError:
        print(f"Source folder '{source_folder}' does not exist.")
        log_action("COPY_FOLDER", f"{source_folder} to {destination_folder}", "FAILURE")
        return False
    except OSError as e:
        print(e)
        log_action("COPY_FOLDER", f"{source_folder} to {destination_folder}", "FAILURE")
        return False
def move_folder(source_folder, destination_folder):
    """Moves a folder from the source path to the destination path."""
    try:
        shutil.move(source_folder, destination_folder)
        print(f"Folder moved from '{source_folder}' to '{destination_folder}' successfully.")
        log_action("MOVE_FOLDER", f"{source_folder} to {destination_folder}", "SUCCESS")
        return True
    except FileNotFoundError:
        print(f"Source folder '{source_folder}' does not exist.")
        log_action("MOVE_FOLDER", f"{source_folder} to {destination_folder}", "FAILURE")
        return False
    except OSError as e:
        print(e)
        log_action("MOVE_FOLDER", f"{source_folder} to {destination_folder}", "FAILURE")
        return False                
import os
import shutil
import zipfile
from logger import log_action
def create_file(file_name):
    """Creates a new file with the specified name and allows the user to input
     content for the file."""
    print("creating a file")
    try:
       content = input("Enter the content for the file: ")
       with open(file_name, "w") as file:
         file.write(content)
         print(f"File '{file_name}' created successfully.")
         print(f"Content written to '{file_name}': {content}")
         log_action("CREATE_FILE", file_name, "SUCCESS")
       return True
    except OSError as e:
        print(f"Error creating file '{file_name}': {e}")
        log_action("CREATE_FILE", file_name, "FAILURE")
        return False
    
def list_files_and_folders():
    """Lists all files and folders in the current directory."""
    print("the list of files and folders in the current directory is:")
    items=input("Enter the directory path to list files and folders : ")
    try:
        items = os.listdir(items)
        log_action("LIST_FILES_AND_FOLDERS", items, "SUCCESS")
        return items
    except OSError as e:
        print(f"Error listing files and folders: {e}")
        log_action("LIST_FILES_AND_FOLDERS", os.getcwd(), "FAILURE")
        return []

def read_file(file_name):
    """Reads and displays the content of the specified file."""
    try:
        with open(file_name, "r") as file:
            content = file.read()
            log_action("READ_FILE", file_name, "SUCCESS")
            return content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        log_action("READ_FILE", file_name, "FAILURE")
        return None

def write_file(file_name, content):
    """Writes the specified content to the specified file."""
    try:
        with open(file_name, "w") as file:
            file.write(content)
            log_action("WRITE_FILE", file_name, "SUCCESS")
            return True
    except OSError as e:
        print(f"Error writing to file '{file_name}': {e}")
        log_action("WRITE_FILE", file_name, "FAILURE")
        return False

def delete_file(file_name):
    """Deletes the specified file."""
    try:
        os.remove(file_name)
        log_action("DELETE_FILE", file_name, "SUCCESS")
        return True
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        log_action("DELETE_FILE", file_name, "FAILURE")
        return False
    except OSError as e:
        print(e)
        log_action("DELETE_FILE", file_name, "FAILURE")
        return False

def rename_file(old_name, new_name):
    """Renames a file from old_name to new_name."""
    try:
        os.rename(old_name, new_name)
        log_action("RENAME_FILE", f"{old_name} to {new_name}", "SUCCESS")
        return True
    except FileNotFoundError:
        print(f"File '{old_name}' not found.")
        log_action("RENAME_FILE", f"{old_name} to {new_name}", "FAILURE")
        return False
    except FileExistsError:
        print(f"A file named '{new_name}' already exists.")
        log_action("RENAME_FILE", f"{old_name} to {new_name}", "FAILURE")
        return False

def append_to_file(file_name, content):
    """Appends the specified content to the end of the specified file."""
    try:
        with open(file_name, "a") as file:
            file.write(content)
            log_action("APPEND_TO_FILE", file_name, "SUCCESS")
            return True
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        log_action("APPEND_TO_FILE", file_name, "FAILURE")
        return False 
    except OSError as e:
        print(f"Error appending to file '{file_name}': {e}")
        log_action("APPEND_TO_FILE", file_name, "FAILURE")
        return False    

def read_file_line_by_line(file_name):
    """Reads and displays the content of the specified file line by line."""
    try:
        with open(file_name, "r") as file:
            for line in file:
                print(line.strip())
            log_action("READ_FILE_LINE_BY_LINE", file_name, "SUCCESS")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        log_action("READ_FILE_LINE_BY_LINE", file_name, "FAILURE")
    except OSError as e:
        print(f"Error reading file '{file_name}': {e}")
        log_action("READ_FILE_LINE_BY_LINE", file_name, "FAILURE")   
def create_file_exclusive(file_name):
    """Creates a new file with the specified name in exclusive mode."""
    try:
        content = input("Enter content: ")
        with open(file_name, "x") as file:
            file.write(content)
        log_action("CREATE_FILE_EXCLUSIVE", file_name, "SUCCESS")
        return True
    except FileExistsError:
        print(f"File '{file_name}' already exists.")
        log_action("CREATE_FILE_EXCLUSIVE", file_name, "FAILURE")
        return False
    except OSError as e:
        print(f"Error creating file '{file_name}': {e}")
        log_action("CREATE_FILE_EXCLUSIVE", file_name, "FAILURE")
        return False    

def read_and_write(file_name):
    try:
        with open(file_name, "r+") as file:
            content = file.read()
            print("Current content of the file:")
            print(content)
            new_content = input("Enter new content to write to the file: ")
            file.write(new_content)
            log_action("READ_AND_WRITE", file_name, "SUCCESS")
            return True
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        log_action("READ_AND_WRITE", file_name, "FAILURE")
        return False
    except OSError as e:
        print(f"Error reading or writing to file '{file_name}': {e}")
        log_action("READ_AND_WRITE", file_name, "FAILURE")
        return False

def read_and_append(file_name):
    try:
        with open(file_name, "a+") as file:
            file.seek(0)  # Move the cursor to the beginning of the file
            content = file.read()
            print("Current content of the file:")
            print(content)
            new_content = input("Enter new content to append to the file: ")
            file.write(new_content)
            log_action("READ_AND_APPEND", file_name, "SUCCESS")
            return True
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        log_action("READ_AND_APPEND", file_name, "FAILURE")
        return False
    except OSError as e:
        print(f"Error reading or appending to file '{file_name}': {e}")
        log_action("READ_AND_APPEND", file_name, "FAILURE")
        return False
            
def write_and_read(file_name):
    try:
        with open(file_name, "w+") as file:
            new_content = input("Enter new content to write to the file: ")
            file.write(new_content)
            file.seek(0)  # Move the cursor to the beginning of the file
            content = file.read()
            print("Current content of the file:")
            print(content)
            log_action("WRITE_AND_READ", file_name, "SUCCESS")
            return True
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        log_action("WRITE_AND_READ", file_name, "FAILURE")
        return False
    except OSError as e:
        print(f"Error creating or writing to file '{file_name}': {e}")
        log_action("WRITE_AND_READ", file_name, "FAILURE")
        return False    
 
def read_and_write_exclusive(file_name):
    try:
        with open(file_name, "x+") as file:
            new_content = input("Enter new content to write to the file: ")
            file.write(new_content)
            file.seek(0)  # Move the cursor to the beginning of the file
            content = file.read()
            print("Current content of the file:")
            print(content)
            log_action("READ_AND_WRITE_EXCLUSIVE", file_name, "SUCCESS")
            return True
    except FileExistsError:
        print(f"File '{file_name}' already exists.")
        log_action("READ_AND_WRITE_EXCLUSIVE", file_name, "FAILURE")
        return False
    except OSError as e:
        print(f"Error creating or writing to file '{file_name}': {e}")
        log_action("READ_AND_WRITE_EXCLUSIVE", file_name, "FAILURE")
        return False

def read_and_write_append(file_name):
    try:
        with open(file_name, "r+") as file:
            content = file.read()
            print("Current content of the file:")
            print(content)
            new_content = input("Enter new content to write to the file: ")
            file.write(new_content)
            file.seek(0)  # Move the cursor to the beginning of the file
            updated_content = file.read()
            print("Updated content of the file:")
            print(updated_content)
            log_action("READ_AND_WRITE_APPEND", file_name, "SUCCESS")
            return True
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        log_action("READ_AND_WRITE_APPEND", file_name, "FAILURE")
        return False
    except OSError as e:
        print(f"Error reading or writing to file '{file_name}': {e}")
        log_action("READ_AND_WRITE_APPEND", file_name, "FAILURE")
        return False

def file_information(file_name):
    """Displays information about the specified file."""
    try:
        file_stats = os.stat(file_name)
        print(f"Information for file '{file_name}':")
        print(f"Size: {file_stats.st_size} bytes")
        print(f"Created: {file_stats.st_ctime}")
        print(f"Last modified: {file_stats.st_mtime}")
        log_action("FILE_INFORMATION", file_name, "SUCCESS")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        log_action("FILE_INFORMATION", file_name, "FAILURE")
    except OSError as e:
        print(f"Error retrieving information for file '{file_name}': {e}")
        log_action("FILE_INFORMATION", file_name, "FAILURE")

def file_exists(file_name):
    if os.path.exists(file_name):
        print(f"The file '{file_name}' exists.")
        log_action("CHECK_FILE", file_name, "SUCCESS")
        return True
    else:
        print(f"The file '{file_name}' does not exist.")
        log_action("CHECK_FILE", file_name, "FAILURE")
        return False        
def move_file(source, destination):
    """Moves a file from the source path to the destination path."""
    try:
        shutil.move(source, destination)
        print(f"File moved from '{source}' to '{destination}'.")
        log_action("MOVE_FILE", f"{source} to {destination}", "SUCCESS")
        return True
    except FileNotFoundError:
        print(f"Source file '{source}' not found.")
        log_action("MOVE_FILE", f"{source} to {destination}", "FAILURE")
        return False
    except OSError as e:
        print(f"Error moving file from '{source}' to '{destination}': {e}")
        log_action("MOVE_FILE", f"{source} to {destination}", "FAILURE")
        return False        
def file_search(folder_path, file_name):
    """Searches for a file in the specified folder and its subfolders."""
    try:
        # Walk through all folders and subfolders
        for root, dirs, files in os.walk(folder_path):

            # Check every file in the current folder
            for filename in files:

                # If the current file matches the user's search
                if filename == file_name:
                    file_path = os.path.join(root, filename)

                    print(f"File found: {file_path}")
                    log_action("SEARCH_FILE", file_path, "SUCCESS")
                    return True

        # If the loop finishes without finding the file
        print(f"File '{file_name}' not found.")
        log_action("SEARCH_FILE", file_name, "FAILURE")
        return False

    except FileNotFoundError:
        print(f"The folder '{folder_path}' does not exist.")
        log_action("SEARCH_FILE", folder_path, "FAILURE")
        return False

    except OSError as e:
        print(f"Error searching folder: {e}")
        log_action("SEARCH_FILE", folder_path, "FAILURE")
        return False
def zip_file(source_file, zip_file_name):
    """Zips the specified file into a zip archive."""
    try:
        with zipfile.ZipFile(zip_file_name, 'w') as zipf:
            zipf.write(source_file, os.path.basename(source_file))
        print(f"File '{source_file}' zipped into '{zip_file_name}' successfully.")
        log_action("ZIP_FILE", f"{source_file} to {zip_file_name}", "SUCCESS")
        return True
    except FileNotFoundError:
        print(f"Source file '{source_file}' not found.")
        log_action("ZIP_FILE", f"{source_file} to {zip_file_name}", "FAILURE")
        return False
    except OSError as e:
        print(f"Error zipping file '{source_file}': {e}")
        log_action("ZIP_FILE", f"{source_file} to {zip_file_name}", "FAILURE")
        return False
def extract_zip(zip_file_name, destination_folder):
    """Extracts the contents of the specified zip file into the destination folder."""
    try:
        with zipfile.ZipFile(zip_file_name, 'r') as zipf:
            zipf.extractall(destination_folder)
        print(f"Contents of '{zip_file_name}' extracted to '{destination_folder}' successfully.")
        log_action("EXTRACT_ZIP", f"{zip_file_name} to {destination_folder}", "SUCCESS")
        return True
    except FileNotFoundError:
        print(f"Zip file '{zip_file_name}' not found.")
        log_action("EXTRACT_ZIP", f"{zip_file_name} to {destination_folder}", "FAILURE")
        return False
    except zipfile.BadZipFile:
        print(f"File '{zip_file_name}' is not a valid zip file.")
        log_action("EXTRACT_ZIP", f"{zip_file_name} to {destination_folder}", "FAILURE")
        return False
    except OSError as e:
        print(f"Error extracting zip file '{zip_file_name}': {e}")
        log_action("EXTRACT_ZIP", f"{zip_file_name} to {destination_folder}", "FAILURE")
        return False        
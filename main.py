import file_manager
import folder_manager


def display_menu():
    print("\n=================================")
    print("      Secure File Manager")
    print("=================================")

    print("\n========== FILE OPERATIONS ==========")
    print("1. Create File")
    print("2. Read File")
    print("3. Rename File")
    print("4. Delete File")
    print("5. Append to File")
    print("6. Write to File")
    print("7. Read File Line by Line")
    print("8. Create File (Exclusive Mode)")
    print("9. Read and Write (Exclusive Mode)")
    print("10. Read and Write (Append Mode)")
    print("11. File Information")
    print("12. Check File Exists")
    print("13. Move File")

    print("\n========== ZIP OPERATIONS ==========")
    print("14. Create ZIP File")
    print("15. Extract ZIP File")

    print("\n========== SEARCH ==========")
    print("16. Search File")

    print("\n========== FOLDER OPERATIONS ==========")
    print("17. Create Folder")
    print("18. List Files and Folders")
    print("19. Delete Folder")
    print("20. Copy Folder")
    print("21. Move Folder")

    print("\n22. Exit")


while True:

    display_menu()

    choice = input("\nEnter your choice (1-22): ").strip()

    if choice == "1":
        file_name = input("Enter file name: ").strip()

        if not file_name:
            print("File name cannot be empty.")
        else:
            file_manager.create_file(file_name)

    elif choice == "2":
        file_name = input("Enter file name: ").strip()
        file_manager.read_file(file_name)

    elif choice == "3":
        old_name = input("Enter current file name: ").strip()
        new_name = input("Enter new file name: ").strip()
        file_manager.rename_file(old_name, new_name)

    elif choice == "4":
        file_name = input("Enter file name: ").strip()
        file_manager.delete_file(file_name)

    elif choice == "5":
        file_name = input("Enter file name: ").strip()
        content = input("Enter content to append: ")
        file_manager.append_to_file(file_name, content)

    elif choice == "6":
        file_name = input("Enter file name: ").strip()
        content = input("Enter content to write: ")
        file_manager.write_file(file_name, content)

    elif choice == "7":
        file_name = input("Enter file name: ").strip()
        file_manager.read_file_line_by_line(file_name)

    elif choice == "8":
        file_name = input("Enter file name: ").strip()
        file_manager.create_file_exclusive(file_name)

    elif choice == "9":
        file_name = input("Enter file name: ").strip()
        file_manager.read_and_write_exclusive(file_name)

    elif choice == "10":
        file_name = input("Enter file name: ").strip()
        file_manager.read_and_write_append(file_name)

    elif choice == "11":
        file_name = input("Enter file name: ").strip()
        file_manager.file_information(file_name)

    elif choice == "12":
        file_name = input("Enter file name: ").strip()
        file_manager.file_exists(file_name)

    elif choice == "13":
        source = input("Enter source file path: ").strip()
        destination = input("Enter destination path: ").strip()
        file_manager.move_file(source, destination)


    elif choice == "14":
        source_file = input("Enter source file: ").strip()
        zip_name = input("Enter ZIP file name: ").strip()
        file_manager.zip_file(source_file, zip_name)

    elif choice == "15":
        zip_name = input("Enter ZIP file name: ").strip()
        destination = input("Enter destination folder: ").strip()
        file_manager.extract_zip(zip_name, destination)

    elif choice == "16":
        folder_path = input("Enter folder path: ").strip()
        file_name = input("Enter file name to search: ").strip()
        file_manager.file_search(folder_path, file_name)


    elif choice == "17":
        folder_name = input("Enter folder name: ").strip()

        if not folder_name:
            print("Folder name cannot be empty.")
        else:
            folder_manager.create_folder(folder_name)

    elif choice == "18":
        items = file_manager.list_files_and_folders()

        if items:
            print("\nFiles and Folders:")
            for item in items:
                print(item)

    elif choice == "19":
        folder_name = input("Enter folder name: ").strip()
        folder_manager.delete_folder(folder_name)

    elif choice == "20":
        source = input("Enter source folder: ").strip()
        destination = input("Enter destination folder: ").strip()
        folder_manager.copy_folder(source, destination)

    elif choice == "21":
        source = input("Enter source folder: ").strip()
        destination = input("Enter destination folder: ").strip()
        folder_manager.move_folder(source, destination)

    elif choice == "22":
        print("\nThank you for using Secure File Manager!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 22.")
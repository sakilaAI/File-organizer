import os
import shutil

def show_created_folders(path):
    """Displays the newly created folders after organizing files."""
    print("\nCreated folders:")
    for root, dirs, _ in os.walk(path):
        for dir in dirs:
            print(os.path.join(root, dir))

def organize_files(path):
    """Organizes files into folders based on their extensions."""
    try:
        if not os.path.exists(path):
            print("Error: The specified path does not exist.")
            return

        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        if not files:
            print("No files found in the specified directory.")
            return

        for file in files:
            print(f"Processing: {file}")
            extension = os.path.splitext(file)[1][1:]  # Extract extension without the dot
            
            if not extension:  # Handle files without extensions
                extension = "No_Extension"

            folder_path = os.path.join(path, extension)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            shutil.move(os.path.join(path, file), os.path.join(folder_path, file))

        show_created_folders(path)

    except PermissionError:
        print("Permission denied: Unable to modify files in the given path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def select_folder(path):
    """Allows the user to choose and view a directory."""
    selected_directory = os.path.join(path, input("\nChoose a Directory: "))

    if os.path.exists(selected_directory) and os.path.isdir(selected_directory):
        print(f"Selected directory: {selected_directory}")
        file_list = os.listdir(selected_directory)
        print("Files:", file_list)
    else:
        print("Invalid directory.")

def read_file():
    """Reads and displays the contents of a file."""
    file_name = input("Enter file name with extension (e.g., file.txt): ")

    try:
        with open(file_name, "r") as file:
            print("\nFile contents:\n" + file.read())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def create_file():
    """Creates a new file within a specified folder and warns if it already exists."""
    folder_path = input("Enter the folder where you want to create the file: ")

    if not os.path.exists(folder_path):
        print("Error: The specified folder does not exist.")
        return

    file_name = input("Enter the file name with extension (e.g., newfile.txt): ")
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        print(f"Warning: The file '{file_name}' already exists.")
        return

    try:
        with open(file_path, "w") as file:
            print(f"File '{file_name}' created successfully in '{folder_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def write_to_file():
    """Writes to an existing file without overwriting its contents."""
    file_name = input("Enter the file name with extension (e.g., file.txt): ")

    if not os.path.exists(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        return

    text = input("Enter text to append: ")

    try:
        with open(file_name, "a") as file:  # Append mode
            file.write("\n" + text)

        print("\nUpdated file contents:")
        read_file()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def delete_file():
    """Deletes a specified file."""
    file_name = input("Enter the file name with extension to delete (e.g., file.txt): ")

    if os.path.exists(file_name):
        try:
            os.remove(file_name)
            print(f"File '{file_name}' deleted successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("File not found.")

def choose_function():
    """Provides a menu for users to choose file operations."""
    while True:
        print("\n---------- Choose an Option ----------")
        print("1 - Organize files into folders")
        print("2 - Select and view a directory")
        print("3 - Read a file")
        print("4 - Create a new file")
        print("5 - Write to an existing file")
        print("6 - Delete a file")
        print("7 - Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                path = input("Enter the directory path to organize: ")
                organize_files(path)
            elif choice == 2:
                path = input("Enter the base directory path: ")
                select_folder(path)
            elif choice == 3:
                read_file()
            elif choice == 4:
                create_file()
            elif choice == 5:
                write_to_file()
            elif choice == 6:
                delete_file()
            elif choice == 7:
                print("Exiting. Thank you!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

choose_function()

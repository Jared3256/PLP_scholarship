def read_and_modify_file():
    filename = input("Enter the filename to read: ")  

    try:
        with open(filename, "r") as file:
            content = file.read()  # Read file content
            modified_content = content.upper()  # Modify content (convert to uppercase)
        
        new_filename = "modified_" + filename  # Create a new filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)  # Write modified content

        print(f"Modified content has been saved to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You might not have access to this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()

import os

directory_path = "."

try:
    directory_content = os.listdir(directory_path)
    print(f"Content of '{directory_path}': ")

    for item in directory_content:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")

except PermissionError:
    print(f"Permission denied to access the directory '{directory_path}.'")

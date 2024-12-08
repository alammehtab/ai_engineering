import os

directory_path = "."

try:
    directory_content = os.listdir(directory_path)
    print(f"Content of directory '{directory_path}':")

    for item in directory_content:
        print(item)

except FileNotFoundError:
    print(f"Directory '{directory_path}' does not exist.")

except PermissionError:
    print(f"Access denied to the directory '{directory_path}'.")

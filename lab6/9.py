import os

path = "/some/path"

try:
    # Проверим, существует ли путь
    if os.path.exists(path):
        directories = []
        files = []

        # Получаем список файлов и директорий
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                directories.append(item)
            elif os.path.isfile(item_path):
                files.append(item)

        print("Directories:", directories)
        print("Files:", files)
    else:
        print("The path does not exist.")
except PermissionError:
    print("Permission denied to access the path.")
except FileNotFoundError:
    print("The path was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


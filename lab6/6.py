import os

path = "/some/path"

# Проверим, существует ли путь перед его использованием
if os.path.exists(path):
    directories = []
    files = []

    try:
        # Получаем список файлов и директорий
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                directories.append(item)
            elif os.path.isfile(item_path):
                files.append(item)

        print("Directories:", directories)
        print("Files:", files)

    except PermissionError:
        print("Permission denied to access the path.")
else:
    print("The path does not exist.")

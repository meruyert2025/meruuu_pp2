import os

path = "/some/path"
if os.path.exists(path):
    print("Path exists")
else:
    print("Path does not exist")

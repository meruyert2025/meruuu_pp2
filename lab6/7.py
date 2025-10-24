import os

path = "/some/path"
if os.access(path, os.F_OK):
    print("Path exists")
else:
    print("Path does not exist")

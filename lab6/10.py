data = ["apple", "banana", "cherry"]
with open("file.txt", "w") as file:
    for item in data:
        file.write(item + "\n")

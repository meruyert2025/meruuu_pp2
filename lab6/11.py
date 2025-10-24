import string

for letter in string.ascii_uppercase:
    file_name = f"{letter}.txt"
    with open(file_name, "w") as file:
        file.write(letter)

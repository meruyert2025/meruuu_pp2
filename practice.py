'''
a=[]
b=3
d=1
for i in range(1,b+1):
    c=int(input())
    a.append(c)
print(a)
for i in a:
    d=d*i
print(d)
'''
'''
a="Meruyert3And4ErkenaZ"
b=0
l=0
k=0
for i in a:
    if i.isupper():
        b+=1
    if i.islower():
        l+=1
print(b)
print(l)
'''
'''
a="apple"
b=a[::-1]
if a==b:
    print("true")
else:
    print("false")
'''
'''

import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay)  # time.sleep секундпен жұмыс істейді, сондықтан миллисекундты секундқа аударамыз
    return math.sqrt(number)

number = 25100
delay = 0
result = delayed_sqrt(number, delay)
print("Square root of", number, "after", delay, "milliseconds is", result)

'''
'''
import time 
import math

a=49
b=2
time.sleep(b)
print(math.sqrt(a))
'''
'''
a=(1==1,2==2,3==3)
s=True
for i in a:
    if not i:
        s=False
        break
print(s)
'''
'''
import os

path = "/Users/meruert/Documents/Nicepage Templates"

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
'''
'''
file_path = "file.txt"
line_count = 0

# Файлдың бар-жоғын тексереміз
if os.path.exists(file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:
                line_count += 1
        print(line_count)
    except IOError:
        print("Error opening or reading the file.")
else:
    print("File does not exist.")
'''
'''
data = ["apple", "banana", "cherry"]
with open("file.txt", "w") as file:
    for item in data:
        file.write(item + "\n")
'''


'''
import string

for letter in string.ascii_uppercase:
    file_name = f"{letter}.txt"
    with open(file_name, "w") as file:
        file.write(letter)

'''
'''
import os

source_path = "source.txt"  
destination_path = "destination.txt"


if os.path.exists(source_path):
    try:
        
        with open(source_path, "r") as source_file:
            content = source_file.read()

        
        with open(destination_path, "w") as destination_file:
            destination_file.write(content)

        print(f"Contents copied from {source_path} to {destination_path}")
    
    except IOError:
        print("Error reading or writing the file. Check file permissions.")
else:
    print(f"The file {source_path} does not exist.")

'''
import os

file_path = "FILE.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted")
else:
    print("File does not exist")

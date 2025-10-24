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


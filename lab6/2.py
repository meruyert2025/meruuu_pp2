text = "Hello World"
upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print(upper_count, lower_count)

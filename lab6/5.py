tuple_data = (True, True, True)
all_true = True

for item in tuple_data:
    if not item:
        all_true = False
        break

print(all_true)

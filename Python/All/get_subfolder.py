import os

current_file_path = os.path.abspath(__file__)
print("Current file path:", current_file_path)

current_dir = os.path.dirname(current_file_path)
print(current_dir)

index = 0
for f in os.scandir(current_dir):
    if f.is_dir():
        index = index + 1
        print(str(index)+'. /'+f.name)
import os

current_file_path = os.path.abspath(__file__)
print("Current file path:", current_file_path)
folder_path = os.path.dirname(current_file_path)
# file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
index = 0
for f in os.listdir(folder_path):
    index = index + 1
    print(str(index)+'. /'+f)
        

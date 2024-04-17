import json

# Define the path to your JSON file
# file_path = 'D:\laragon\htdocs\config\project\luminar.txt'

# # Initialize an empty list to store the JSON data
# json_data = []

# with open(file_path, 'r') as file:
#     for line in file:
#         data = line.strip()
#         if data:
#             try:
#                 json_object = json.loads(data)
#                 json_data.append(json_object)
#             except json.JSONDecodeError as e:
#                 print(f"Error decoding JSON data: {e}")


# # Now you have a list of dictionaries (or objects) containing the JSON data
# for item in json_data:
#     print(item, )

# print(json_data[0]['python'])

filename = 'luminar'
file_path = f'D:\laragon\htdocs\config\project\{filename}.txt'
json_data = {}
with open(file_path, 'r') as file:
    json_data = json.load(file)

# Check if the key exists in the dictionary
if 'open' in json_data:
    # Update the value for the specified key
    json_data['open'] = 'close'

    # Write the updated JSON data back to the file
    with open(file_path, 'w') as file:
        json.dump(json_data, file, indent=4)
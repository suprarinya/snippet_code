from PIL import Image

# Load the image
img = Image.open("D:/allindex/recorder/asset/rescope.jpg")

# Convert the image to RGBA (if it's not already in that mode)
img = img.convert("RGBA")

# Get the data of the image
data = img.getdata()

# Create a new data list
new_data = []
for item in data:
    # Change all white (also shades of whites)
    # pixels to red
    if item[0] in range(200, 256) and item[1] in range(200, 256) and item[2] in range(200, 256):
        new_data.append((255, 0, 0, item[3]))  # change all white (also shades of whites) to red
    else:
        new_data.append(item)

# Update image data
img.putdata(new_data)

# Save the new image
img.save("D:/allindex/recorder/asset/red_image.png")

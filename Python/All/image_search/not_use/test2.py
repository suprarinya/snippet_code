from PIL import Image

img_name = 'button_click2.png'
img_name2 = 'button_click3.png'
width = 47
height = 31


image = Image.open(img_name)
new_image = image.resize((width, height))
new_image.save(img_name2)
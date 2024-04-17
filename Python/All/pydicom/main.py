import pydicom
from PIL import Image

dicom_file = pydicom.dcmread('asset/MRBRAIN.DCM')
pixel_array = dicom_file.pixel_array
image = Image.fromarray(pixel_array)
image.save('output_image.png')
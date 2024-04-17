import pydicom
from PIL import Image
import numpy as np
import sys
import os
import shutil
from pydicom.pixel_data_handlers.util import apply_color_lut

arg1 = sys.argv[1] # name
arg2 = sys.argv[2] # tempfilepath

def convert_dicom_to_image(dicom_file_path, output_file_path, output_format="JPEG"):
  """
  Converts a DICOM file to an image file (JPEG or PNG).

  Args:
      dicom_file_path (str): Path to the DICOM file.
      output_file_path (str): Path to save the converted image file.
      output_format (str, optional): Output image format ("JPEG" or "PNG"). Defaults to "JPEG".
  """

  try:
    dataset = pydicom.dcmread(dicom_file_path)
    pixel_data = dataset.pixel_array.astype(float)

    if len(pixel_data.shape) == 3:
      num_frames = pixel_data.shape[0]
      if num_frames > 1:
        for i in range(num_frames):
          frame = pixel_data[i]
          mode = "RGB"
          if dataset.PhotometricInterpretation.startswith("RGB"):
            if pixel_data.shape[-1] != 3:
                pixel_data = np.transpose(pixel_data, axes=[1, 2, 0])
          if dataset.PhotometricInterpretation.startswith("PALETTE"):
            frame = apply_color_lut(pixel_data[i], dataset)
          else:
              mode = "L" 

          frame_scaled = (frame - frame.min()) / (frame.max() - frame.min()) * 255
          frame_uint8 = frame_scaled.astype(np.uint8)
          frame_image = Image.fromarray(frame_uint8, mode=mode)
          frame_image.save(os.path.join( f"frame_{i}.{output_format.lower()}"), output_format.upper())
        return True
      else:
        slice_index = pixel_data.shape[0] // 2
        pixel_data = pixel_data[slice_index]
    # elif len(pixel_data.shape) == 2: 
    #     pixel_data = np.expand_dims(pixel_data, axis=-1) 

    if "PixelData" not in dataset:
      raise ValueError("DICOM file missing required elements for conversion.")
    
    if "RescaleIntercept" in dataset and "RescaleSlope" in dataset:
      pixel_data = pixel_data * dataset.RescaleSlope + dataset.RescaleIntercept
    elif 'WindowCenter' in dataset and 'WindowWidth' in dataset:
      pixel_data    = dataset.pixel_array
      window_center = dataset.WindowCenter
      window_width  = dataset.WindowWidth
      min_value     = window_center - window_width / 2.0
      max_value     = window_center + window_width / 2.0
      pixel_data    = np.clip(pixel_data, min_value, max_value) 

    pixel_data_scaled = (pixel_data - pixel_data.min()) / (pixel_data.max() - pixel_data.min()) * 255
    pixel_data_uint8 = pixel_data_scaled.astype(np.uint8)

    if dataset.PhotometricInterpretation == "MONOCHROME2":
      mode = "L" 
    else:
      mode = "RGB" 
      
    image = Image.fromarray(pixel_data_uint8, mode=mode)
    image.save(output_file_path, output_format.upper())

    return True

  except Exception as e:
    print(f"Error converting DICOM file: {e}")
    return False

def backup_dicomfile(dicom_path, store_path):
  if not os.path.exists(store_path):
    os.makedirs(store_path)
  
  to_path = os.path.join(store_path, 'backup', os.path.basename(dicom_path))
  try:
    shutil.copy(dicom_path, to_path)
    return True
  except:
    print('error')
    return False

storepath = 'D:/laragon/htdocs/ScreenRecord'
dicom_file_path = arg2
output_file_path = storepath + '/' + arg1
# dicom_file_path = 'asset/0020.dcm'
# output_file_path = 'test.jpg'
convert = convert_dicom_to_image(dicom_file_path, output_file_path)
backup  = backup_dicomfile(dicom_file_path, storepath)

if convert and backup:
  print("success")
else:
  print("error")
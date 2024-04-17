import pydicom
from PIL import Image
import numpy as np


def convert_dicom_to_image(dicom_file_path, output_file_path, output_format="PNG"):
  """
  Converts a DICOM file to an image file, handling cases without a pixel_array.

  Args:
      dicom_file_path (str): Path to the DICOM file.
      output_file_path (str): Path to save the converted image file.
      output_format (str, optional): Output image format (e.g., PNG, JPEG). Defaults to "PNG".
  """

  # Read the DICOM file
  ds = pydicom.dcmread(dicom_file_path)

  # Check if pixel_array exists
  if 'PixelData' not in ds:
    raise ValueError("DICOM file does not contain pixel data (missing PixelData element).")

  # Get pixel data and reshape if necessary
  pixel_data = ds.pixel_array
  if len(pixel_data.shape) == 2:  # Handle 2D data (e.g., single slice)
    pixel_data = np.expand_dims(pixel_data, axis=-1)  # Add channel dimension

  # Apply windowing if necessary (adjust based on your needs)
  if 'WindowCenter' in ds and 'WindowWidth' in ds:
    window_center = ds.WindowCenter
    window_width = ds.WindowWidth
    min_value = window_center - window_width / 2.0
    max_value = window_center + window_width / 2.0
    pixel_data = np.clip(pixel_data, min_value, max_value)  # Clip to window range

  # Rescale pixel data to 0-255 (assuming uint8)
  pixel_data = (pixel_data - pixel_data.min()) / (pixel_data.max() - pixel_data.min()) * 255

  # Convert to uint8 array
  pixel_data = pixel_data.astype(np.uint8)

  # Create and save image using Pillow
  image = Image.fromarray(pixel_data)
  image.save(output_file_path, output_format)


# Example usage
dicom_file_path = "asset/0020.dcm"
output_file_path = "output_image.png"
convert_dicom_to_image(dicom_file_path, output_file_path)
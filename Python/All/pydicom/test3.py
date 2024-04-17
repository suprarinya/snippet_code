import gdcm
import numpy as np

def convert_dicom_to_image_gdcm(dicom_file_path, output_file_path, output_format="JPEG"):
  """
  Converts a DICOM file to an image file (JPEG or PNG) using gdcm.

  Args:
      dicom_file_path (str): Path to the DICOM file.
      output_file_path (str): Path to save the converted image file.
      output_format (str, optional): Output image format ("JPEG" or "PNG"). Defaults to "JPEG".
  """

  try:
    reader = gdcm.ImageReader()
    reader.SetFileName(dicom_file_path)
    if not reader.Read():
      raise ValueError(f"Failed to read DICOM file: {e}")

    image = reader.GetImage()

    # Check for pixel data existence and data type
    pixel_data = None
    if image.GetBuffer():
      # Get pixel data as a NumPy array (assuming suitable data type)
      pixel_data = np.frombuffer(image.GetBuffer(), dtype=image.GetPixelType())
    else:
      print(f"DICOM file '{dicom_file_path}' might be missing PixelData element. Attempting alternative gdcm methods.")

    # Handle missing PixelData (heuristic approach)
    if pixel_data is None:
      try:
        # Try extracting pixel data using alternative gdcm methods (heuristic)
        transfer_syntax = reader.GetMetaDataElement("0002,0010").GetValue()
        if transfer_syntax.startswith("JPEG"):
          # Handle encapsulated JPEG data (heuristic)
          pixel_data = reader.GetJpegLosslessDataAsByteArray()
          pixel_data = np.frombuffer(pixel_data, dtype=np.uint8)  # Assuming JPEG data
        else:
          raise NotImplementedError(f"Automatic conversion for transfer syntax '{transfer_syntax}' not implemented.")
      except Exception as e:
        print(f"Alternative gdcm methods failed: {e}")
        return

    # Rescale data based on RescaleSlope and RescaleIntercept (if present)
    if reader.HasMetaDataElement("0028,1040") and reader.HasMetaDataElement("0028,1050"):
      rescale_slope = reader.GetMetaDataElement("0028,1040").GetValue()
      rescale_intercept = reader.GetMetaDataElement("0028,1050").GetValue()
      pixel_data = pixel_data * rescale_slope + rescale_intercept

    # Rescale to 0-255 range for 8-bit image (common for JPEG and PNG)
    array_data_scaled = (pixel_data - pixel_data.min()) / (pixel_data.max() - pixel_data.min()) * 255

    # Convert to uint8 for image data type compatibility
    array_data_uint8 = array_data_scaled.astype(np.uint8)

    # Create a NumPy array representing the image
    image_array = np.reshape(array_data_uint8, [image.GetDimensions()[1], image.GetDimensions()[0]])

    # Handle color channels based on PhotometricInterpretation
    photometric_interpretation = reader.GetMetaDataElement("0028,0004").GetValue()
    if photometric_interpretation == "MONOCHROME2":
      mode = "L"  # Grayscale mode for MONOCHROME2
    elif photometric_interpretation == "PALETTECOLOR":
      # Handle palette color images (more complex logic needed)
      raise NotImplementedError("Conversion for PALETTECOLOR PhotometricInterpretation not implemented yet.")
    else:
      mode = "RGB"  # Default to RGB mode for other interpretations

    # Save the image using Pillow
    from PIL import Image
    image_pil = Image.fromarray(image_array, mode=mode)
    image_pil.save(output_file_path, output_format.upper())

  except Exception as e:
    print(f"Error converting DICOM file: {e}")

# Example usage
dicom_file_path = "asset/MRBRAIN.DCM"
output_file_path = "converted_image1.png"
convert_dicom_to_image_gdcm(dicom_file_path, output_file_path)


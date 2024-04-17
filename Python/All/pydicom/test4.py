from pydicom import examples
from pydicom.pixel_data_handlers.util import apply_color_lut

# Fetch an example PALETTE COLOR dataset
ds = examples.palette_color
arr = ds.pixel_array
rgb = apply_color_lut(arr, ds)
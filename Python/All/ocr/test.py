import mss
import mss.tools
from PIL import Image


with mss.mss() as sct:
    # Get information of monitor 2
    monitor_number = 2
    mon = sct.monitors[monitor_number]

    # The screen part to capture
    monitor = {
        "top": mon["top"],
        "left": mon["left"],
        "width": mon["width"],
        "height": mon["height"],
        "mon": monitor_number,
    }
    output = "sct-mon{mon}_{top}x{left}_{width}x{height}_2.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)

    snap_im = Image.open(output)
    # crop_im = snap_im.crop((1390, 480, 1575, 520))
    crop_im = snap_im.crop((1390, 450, 1480, 480))
    newname = f"crop_2_{output}"
    crop_im.save(newname)


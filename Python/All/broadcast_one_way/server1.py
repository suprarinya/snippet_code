# import required libraries
import uvicorn
from vidgear.gears.asyncio import WebGear_RTC

# various performance tweaks
# options = {
#     "frame_size_reduction": 30,
# }

# options = {"custom_data_location": "/home/foo/foo1", "enable_live_broadcast": True, "enable_infinite_frames": True}

# initialize WebGear_RTC app
# from video file
# web = WebGear_RTC(source="foo1.mp4", logging=True, **options)

options = {"enable_infinite_frames": True, "custom_data_location": "D:/laragon/htdocs/playground/python/broadcast_one_way"}
# from camera
web = WebGear_RTC(source=0, logging=True, resolution=(1280,720), framerate=60, **options)

# run this app on Uvicorn server at address http://localhost:8000/
# templates at C:\Users\bright\.vidgear\templates
uvicorn.run(web(), host="localhost", port=5001)

# close app safely
web.shutdown()
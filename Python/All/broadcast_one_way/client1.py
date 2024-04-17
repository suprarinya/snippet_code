# import required libraries
import uvicorn
from vidgear.gears.asyncio import WebGear_RTC

# initialize WebGear_RTC app 
# web = WebGear_RTC(source="rtsp://192.168.0.102:8554/webCamStream", logging=True)
web = WebGear_RTC(source="rtsp://127.0.0.1:5003/", logging=True)

# run this app on Uvicorn server at address http://localhost:8000/
uvicorn.run(web(), host="localhost", port=5002)

# close app safely
web.shutdown()
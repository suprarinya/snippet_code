import asyncio
import argparse
import random
import string
from aiohttp import web
from aiortc import RTCPeerConnection, RTCSessionDescription, VideoStreamTrack
from aiortc.contrib.media import MediaPlayer, MediaRecorder

# Define a basic video stream track class
class VideoTrack(VideoStreamTrack):
    def __init__(self, filepath):
        super().__init__()
        self.player = MediaPlayer(filepath)

    async def recv(self):
        pts, time_base = await self.next_timestamp()
        frame = await self.player.get_frame()
        if frame is not None:
            return frame.to_bytes(), pts, time_base, None
        else:
            return None


async def offer(request):
    # Parse the filepath parameter from the request
    params = await request.json()
    filepath = params.get('filepath')

    # Create a new peer connection
    pc = RTCPeerConnection()

    # Add a video track to the connection
    video_track = VideoTrack(filepath)
    pc.addTrack(video_track)

    # Create an offer
    await pc.setLocalDescription(await pc.createOffer())
    offer = {'sdp': pc.localDescription.sdp, 'type': pc.localDescription.type}

    # Return the offer as a JSON response
    return web.json_response(offer)


async def answer(request):
    # Parse the filepath parameter from the request
    params = await request.json()
    filepath = params.get('filepath')

    # Create a new peer connection
    pc = RTCPeerConnection()

    # Add a video track to the connection
    video_track = VideoTrack(filepath)
    pc.addTrack(video_track)

    # Parse the remote description from the request
    remote = await request.json()
    await pc.setRemoteDescription(RTCSessionDescription(sdp=remote['sdp'], type=remote['type']))

    # Create an answer
    await pc.setLocalDescription(await pc.createAnswer())
    answer = {'sdp': pc.localDescription.sdp, 'type': pc.localDescription.type}

    # Return the answer as a JSON response
    return web.json_response(answer)


async def index(request):
    # Serve the index.html file
    with open('templates/index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


app = web.Application()
app.router.add_get('/', index)
app.router.add_post('/offer', offer)
app.router.add_post('/answer', answer)


# Define a dictionary of video files mapped to their corresponding URLs
video_files = {
    '/video1': 'asset/small.mp4',
    '/video2': 'asset/sample.mp4',
}


# Define a handler function for serving video files
async def video_handler(request):
    # Parse the URL and retrieve the corresponding video file path
    url = request.path
    filepath = video_files.get(url)

    if filepath is None:
        # Return a 404 error if the URL is not found in the dictionary
        return web.HTTPNotFound()
    else:
        # Serve the video file
        with open(filepath, 'rb') as f:
            return web.Response(body=f.read(), content_type='video/mp4')


# Add the video handler to the application router for each URL in the dictionary
for url in video_files.keys():
    app.router.add_get(url, video_handler)


if __name__ == '__main__':
    # Start the server
    web.run_app(app, port=8000)

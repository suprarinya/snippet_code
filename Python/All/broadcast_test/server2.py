import cv2
import numpy as np
import asyncio
from aiohttp import web
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaRecorder, MediaPlayer
from flask import Flask, render_template

app = Flask(__name__)

async def offer_pc(room):
    pc = RTCPeerConnection()

    file_name = 'asset/small.mp4' if room ==  'room1' else 'asset/sample.mp4'

    @pc.on("track")
    async def on_track(track):
        recorder = MediaRecorder(file_name)
        recorder.addTrack(track)
        await recorder.start()

    pc.addTransceiver("video")
    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)

    return pc.localDescription.sdp


async def answer_pc(offer_sdp):
    pc = RTCPeerConnection()

    @pc.on("datachannel")
    def on_datachannel(channel):
        @channel.on("message")
        def on_message(message):
            print(message)

    await pc.setRemoteDescription(RTCSessionDescription(sdp=offer_sdp, type="offer"))
    pc.addTransceiver("video")
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return pc.localDescription.sdp


async def room1(request):
    offer_sdp = await offer_pc("room1")
    return web.Response(text=offer_sdp)


async def room2(request):
    offer_sdp = await offer_pc("room2")
    return web.Response(text=offer_sdp)


app = web.Application()
app.router.add_get('/room1', room1)
app.router.add_get('/room2', room2)


if __name__ == '__main__':
    web.run_app(app, port=5003)
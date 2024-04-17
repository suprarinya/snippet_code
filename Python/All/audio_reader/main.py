# pip install pydub
# ต้องเอา ffprobe.exe ไปวางไว้ในโฟลเดอร์เดียวกับ python.exe
from pydub import AudioSegment
from pydub.playback import play

file_path = 'D:\\laragon\\htdocs\\playground\\python\\audio_reader\\shutter.m4a'
song = AudioSegment.from_file(file_path)
play(song)
import os
import cv2 
import time
import string
import random


from win32      import win32api
from win32      import win32process
from win32      import win32gui
from pickle     import FALSE
from PIL        import Image

from datetime   import datetime
from ssl        import HAS_NEVER_CHECK_COMMON_NAME
from flask      import Flask, render_template, Response, request
import datetime
import json

f = open("D:/laragon/htdocs/config/project/scope.txt", "r")
config = json.loads(f.read())


app = Flask(__name__)

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
    # 'mp4': cv2.VideoWriter_fourcc(*'mp4v'),
    '.mp4': cv2.VideoWriter_fourcc(*'avc1'),
}


def callback(hwnd, pid):
  if win32process.GetWindowThreadProcessId(hwnd)[1] == pid:
    # hide window
    win32gui.ShowWindow(hwnd, 0)

# find hwnd of parent process, which is the cmd.exe window
win32gui.EnumWindows(callback, os.getppid())


def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

# Standard Video Dimensions Sizes
# currently can't record video using 1080p (below is OK)
# suspect it because of camera's spec
STD_DIMENSIONS =  {
    "480p":     (640, 480),
    "720p":     (1280, 720),
    "1080p":    (1920, 1080),
    "4k":       (3840, 2160),
}

def get_dimension(cap, res='1080p'):
    width, height = STD_DIMENSIONS['1080p']
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height


def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    print('get: ',filename, ext)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['mp4']


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def generate_frames(source,hn,caseuniq,cid):
    
    # source = 1

    second_i=0
    fps     = 24.0
    bitrate = 1000000
    camera  =cv2.VideoCapture(int(source))   
    # camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')) # depends on fourcc available camera
    # camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'P', '4', 'V')) # depends on fourcc available camera
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4')) # depends on fourcc available camera    
    ddd     = datetime.datetime.now()
    mmm     = ddd.strftime("%Y%m%d%H%M%S")

    if os.path.exists("D:/laragon/htdocs/vdo/"+ddd.strftime("%Y%m")):
        print("have")
    else:
        os.mkdir("D:/laragon/htdocs/vdo/"+ddd.strftime("%Y%m"))

    filename = "D:/laragon/htdocs/vdo/"+ddd.strftime("%Y%m")+"/"+cid +"_0_"+ hn + "_" + mmm + "_" + source + ".mp4"
    # filename = "D:/laragon/htdocs/vdo/"+ddd.strftime("%Y%m")+"/"+cid +"_0_"+ hn + "_" + mmm + "_" + source + ".h264"

    gstream = f"appsrc ! videoconvert ! mfxh264enc ! \
        video/x-h264, profile=baseline ! bitrate={bitrate} \
        matroskamux ! filesink location={filename}"

    ## ห้ามลบสองบรรทัดนี้ ##
    dims2 = get_dimension(camera, res='1080p')
    # dims2 = get_dimension(camera, res='480p')  #สำหรับกล้อง webcamsoun
    ## ห้ามลบสองบรรทัดนี้ ##
    
    video_type_cv2  = get_video_type(filename)
    print(video_type_cv2, filename)
    # 
    # out             = cv2.VideoWriter(filename, video_type_cv2, fps, dims2) # dims = width, height
    out             = cv2.VideoWriter(f"appsrc ! videoconvert ! avenc_mpeg4 bitrate=100000 ! mp4mux ! filesink location={filename}", cv2.CAP_GSTREAMER, 0, fps, dims2)
    # 
    record_status   = False
    if  os.path.exists("D:/laragon/htdocs/ScreenRecord/stop"+source+".txt"):
        os.remove("D:/laragon/htdocs/ScreenRecord/stop"+source+".txt")
        os.remove("D:/laragon/htdocs/ScreenRecord/start"+source+".txt")

    while True:
        (success, frame)  = camera.read()
        if record_status:
            out.write(frame)
            if os.path.exists("D:/laragon/htdocs/ScreenRecord/stop"+source+".txt"):
                if  os.path.exists("D:/laragon/htdocs/ScreenRecord/start"+source+".txt"):
                    os.remove("D:/laragon/htdocs/ScreenRecord/start"+source+".txt")
                    os.remove("D:/laragon/htdocs/ScreenRecord/stop"+source+".txt")
                    out.release()
                record_status = False
        else:
            if os.path.exists("D:/laragon/htdocs/ScreenRecord/start"+source+".txt"):
                record_status   = True


        second_i = second_i+1
        if(second_i>400):
            if(config['readocr']):
                ocrname = "C:\\allindex\\capture\\__pycache__\\ocr"+source+".jpg"
                #Olympus
                if(config['olympus']):
                    cropped_image = frame[660:710, 65:200]
                    cv2.imwrite(ocrname, cropped_image)

                #Fuji
                if(config['fuji']):
                    cropped_image = frame[475:520, 1390:1600]
                    cv2.imwrite(ocrname, cropped_image)

            if(config['checkblack']):
                picblack = "C:\\allindex\\capture\\__pycache__\\black"+source+".jpg"
                cropped_image = frame[500:600, 900:1000]
                cv2.imwrite(picblack, cropped_image)
            second_i = 0




        if os.path.exists("D:/laragon/htdocs/ScreenRecord/cap"+source+".txt"):
            camera_id   = open("D:/laragon/htdocs/ScreenRecord/camera"+source+".txt", "r")
            aaa         = datetime.datetime.now()
            sss         = aaa.strftime("%y%m%d%H%M%S")
            
            micro = (list(str(aaa.microsecond)))
            if(len(micro)<2):
                timerecord = sss+"0"+micro[0]
            else:
                timerecord = sss+micro[0]+micro[1]
                
            picturename = cid+"_"+camera_id.read()+"_"+ hn + "_" + timerecord + "_" + source + ".jpg"
            img_name    = 'D:/laragon/htdocs/ScreenRecord/temp/'+ picturename
            cv2.imwrite(img_name, frame)
            os.remove("D:/laragon/htdocs/ScreenRecord/cap"+source+".txt")

        if not success:
            break
        else:
            (ret, buffer) = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n'+frame + b'\r\n')




@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/video')
def video():
    cid     = request.args.get('cid')
    source  = request.args.get('source')
    hn      = request.args.get('hn')
    caseuniq= request.args.get('caseuniq')
    return Response(generate_frames(source,hn,caseuniq,cid), mimetype='multipart/x-mixed-replace; boundary=frame' )
    

if __name__ == "__main__":
    app.run(debug=True)
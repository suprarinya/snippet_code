import numpy as np
import cv2
import ffmpeg

def save_video(cap,saving_file_name,fps=33.0):

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            i_width,i_height = frame.shape[1],frame.shape[0]
            break

    num = 10000

    process = (
    ffmpeg
        .input('pipe:',format='rawvideo', pix_fmt='rgb24',s='{}x{}'.format(i_width,i_height))
        .output(saved_video_file_name,pix_fmt='yuv420p',vcodec='libx264',r=fps,crf=23, video_bitrate=num*1000) #  video_bitrate=num*1000
        .overwrite_output()
        .run_async(pipe_stdin=True)
    )

    return process

if __name__=='__main__':

    input_file = 'blackpink.mp4'
    cap = cv2.VideoCapture(input_file)

    # cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    # cap.set(3,1920)
    # cap.set(4,1080)
    # saved_video_file_name = 'output.avi'
    saved_video_file_name = 'output1.mp4'
    process = save_video(cap,saved_video_file_name,24)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            # frame = cv2.flip(frame,0)
            process.stdin.write(
                cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    .astype(np.uint8)
                    .tobytes()
                    )

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                process.stdin.close()
                process.wait()
                cap.release()
                cv2.destroyAllWindows()
                break
        else:
            process.stdin.close()
            process.wait()
            cap.release()
            cv2.destroyAllWindows()
            break
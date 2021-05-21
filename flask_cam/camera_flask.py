from flask import Flask, render_template, Response
import cv2

# Flask insistnace app

app = Flask(__name__)

camera = cv2.VideoCapture(0)
'''
if not camera.isOpend():
    print("Cannot Open Camera!")
    exit()
'''
camera.set(cv2.CAP_PROP_FRAME_WIDTH,320)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,240)

def gen_frames():
    while True:
        # Capture frame-by-frame
        success,frame= camera.read()
        if not success:
            print("Camera.read() Failed!")
            break
        else:
            ret,buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') # Loop after Return


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace;boundary=frame')

@app.route('/')
def index():
    '''Video Streaming Main Page'''
    return render_template('index.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=False)
import cv2
import requests
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()

endpoint = os.getenv("ENDPOINT")
api_key = os.getenv("PREDICCIONKEY")

### En este apartedo tenemos un algoritmo que nos ayudara a detectar objetos que con Azure Vision, de la clases de objetos que ellos tienes ###
videoset = "./dataset/prueba.mp4"
cam = cv2.VideoCapture(videoset) # para cambiar si queremos que sea la camara o un video que nosotros cambiemos solo debemos cambiar "numero de camara: 0 o el path del video"

frame_count = 0

while True:
    ret, frame = cam.read()

    if not ret:
        break

    frame_count += 1

    if frame_count % 5 != 0:
        continue

    frame = cv2.resize(frame, (640, 360))

    _, img_encode = cv2.imencode('.jpg', frame)
    body = img_encode.tobytes()
    
    try:
        res = requests.post(
            endpoint,
            headers={
                "Prediction-Key": api_key,
                "Content-Type": "application/octet-stream"
            },
            data=body
        )

        print("Status: ",res.status_code)
        if res.status_code == 200:
            result = res.json()

            for obj in result.get("objects",[]):
                print(json.dumps(obj["object"], indent=2))
        else:
            print(res.text)
    except Exception as e:
        print("Error: ", e)

    cv2.imshow("Video", frame) # Para video o Camara solo debemos de cambiar "Cam o Video"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.1)

cam.release()
cv2.destroyAllWindows()
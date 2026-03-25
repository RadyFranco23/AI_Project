import cv2
from PIL import Image
from python.onnxruntime_predict import ONNXRuntimeObjectDetection
from customvision_postprocess import postprocess_custom_vision

with open("./ObjectDetection/python/labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

objectDetection = ONNXRuntimeObjectDetection("ObjectDetection/python/model.onnx", labels)

videoset = "./dataset/prueba.mp4"
cam = cv2.VideoCapture(videoset)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb)

    raw_output = objectDetection.predict(pil_img)

    detecciones = postprocess_custom_vision(raw_output, labels)

    h, w, _ = frame.shape

    for d in detecciones:
        bb = d["boundingBox"]

        x = int(bb["left"] * w)
        y = int(bb["top"] * h)
        ww = int(bb["width"] * w)
        hh = int(bb["height"] * h)

        cv2.rectangle(frame, (x, y), (x + ww, y + hh), (0, 255, 0), 2)
        cv2.putText(
            frame,
            f"{d['tagName']} {d['probability']:.2f}",
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2
        )

    cv2.imshow("Detección ONNX", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

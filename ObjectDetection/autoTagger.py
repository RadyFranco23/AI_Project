from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from PIL import Image
from io import BytesIO
import os


credential = ApiKeyCredentials(in_headers={"Prediction-key":apiKey})
credentiasTrain= ApiKeyCredentials(in_headers={"Training-key": apiKeyTraining})

client = CustomVisionPredictionClient(endpoint, credential)
trainer = CustomVisionTrainingClient(endpointTraining, credentiasTrain)


folder = "./dataset"

def is_valid_image(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        img = Image.open(BytesIO(data))
        img.verify()
        return True
    except:
        return False

for file in os.listdir(folder):
    if not file.lower().endswith((".jpg", ".jpeg", ".png")):
        continue
    
    path = os.path.join(folder, file)

    if not is_valid_image(path):
        print("SKIP (imagen dañada):", file)
        continue

    with open(path, "rb") as img:
        data = img.read()
    
    try:
        res = client.detect_image(PROJECT_ID, ModelName, data)
    except Exception as e:
        print("ERROR con:", file)
        print(e)
        continue

    # res = client.detect_image(PROJECT_ID, ModelName, data)
    best = max(res.predictions, key=lambda x: x.probability)

    if best.probability > 0.85:
        trainer.create_images_from_data(PROJECT_ID, data, tag_ids=[best.tag_id])
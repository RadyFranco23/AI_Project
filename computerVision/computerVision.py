import os
from dotenv import load_dotenv
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

load_dotenv()

#Lector de texto en imagenes.

client = ImageAnalysisClient(
    endpoint=os.getenv("ENDPOINT"),
    credential=AzureKeyCredential(os.getenv("KEY"))
)

result = client.analyze_from_url(
    image_url= 'https://raw.githubusercontent.com/Azure/azure-sdk-for-java/main/sdk/vision/azure-ai-vision-imageanalysis/src/samples/java/com/azure/ai/vision/imageanalysis/sample.jpg',
    visual_features=[VisualFeatures.READ],
    gender_neutral_caption=True
)

print("Read: ")
if result.read is not None:
    for line in result.read.blocks[0].lines:
        print(f'LINE: "{line.text}", Bounding box: {line.bounding_polygon}')
        for word in line.words:
            print(f'Word: "{word.text}", Bouding polygon {word.bounding_polygon}')
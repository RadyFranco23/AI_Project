import sounddevice as sd
from openai import AzureOpenAI
from dotenv import load_dotenv
import os
import numpy as np
import whisper
import torch



load_dotenv()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = whisper.load_model("tiny", device=device) # cargando el modelo

fs = 16000
duration = 4


apikey = os.getenv("API_KEY")
azureendpoint = os.getenv("AZURE_ENDPOINT")
apivertion = os.getenv("API_VERSION")

# Prueba funcional escuchando a traves del microfono
idiomaTraducir = input("Introduzca al idioma que quiere traducir: ")

def GrabarAudio(): 

    print("Grabando.....")
    grabacion = sd.rec(int(duration*fs),samplerate=fs,channels=1,dtype='float32')
    sd.wait()

    return grabacion

def reproducirTest(grabacion):
    print("Reproduciendo.....")
    sd.play(grabacion, fs)
    sd.wait()

# reproducirTest(GrabarAudio()) # Ya podemos grabar el audio por 5 segundos, ahora volvamolo a texto

def SpeachToText(grabacion, model):

    spechtext = model.transcribe(grabacion.flatten()) # task="translate"
    print(spechtext["text"])

    client = AzureOpenAI(
        api_version= apivertion,
        azure_endpoint =azureendpoint,
        api_key= apikey
        
    )

    prompt = (f"Traduce el siguiente texto de {spechtext["language"]} a '{idiomaTraducir}'"
              f"Solo devuelve el texto traducido, sin comentarios ni formato: '{spechtext["text"]}'")
    

    responseTranslation = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "Eres un traductor profesional y preciso."
            }
            ,{
                "role": "user",
                "content": prompt,
            }
        ], 
        temperature=0.0
    )

    oracionestraducidas = responseTranslation.choices[0].message.content.strip()
    print(f"Traducción ({idiomaTraducir}): {oracionestraducidas}")


SpeachToText(GrabarAudio(), model)


#para la video llamadas podemos capturar el texto de la salida de audio del dispositivo
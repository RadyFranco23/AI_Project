import sounddevice as sd
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
import os
import numpy as np
import whisper
import torch
import sys
import time
import queue

load_dotenv()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = whisper.load_model("tiny", device=device) # cargando el modelo

q = queue.Queue()
fs = 16000
duration = 4

azurePushStream = None
suscrip = os.getenv("SUBSCRIPTION_AZURESPEECH")
azureregion = os.getenv("AZURE_SPEECHREGION")

print(sd.query_devices())

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)



def trancribirAudio(audio):
    audio_float = audio.astype(np.float32) / 32768.0 
    result = model.transcribe(audio_float)
    return result["text"]


def iniciarEscuchaContinua():
    
    audio_buffer = np.empty((0, 1), dtype="int16")

    try:
        #Iniciamos el flujo de entrada de sounddevice
        with sd.InputStream(
            samplerate=fs,
            device= 1, # prueba el 28, 29 que tienen la misma cantidad de canales
            channels= 1,
            callback=callback,
            dtype="int16",
            blocksize= 1024
        ):
            print("es aqui 1")
            while True:
                time.sleep(1)
                chunk = q.get()
                audio_buffer = np.append(audio_buffer, chunk, axis=0)

                if len(audio_buffer) >= (fs*duration):

                    chunk_Transcribir = audio_buffer[:(fs*duration)]
                    audio_buffer = audio_buffer[(fs*duration):]
                    textoTrancrito = trancribirAudio(chunk_Transcribir)

                    print(f"{time.strftime('%H:%M:%S')}: {textoTrancrito}")

    except KeyboardInterrupt:
        print("\n\n Proceso de transcripción detenido por el usuario.")
    except Exception as e:
        print(f"\n Ocurrió un error: {e}")

iniciarEscuchaContinua()




import sounddevice as sd
import azure.cognitiveservices.speech as speechsdk
import azure.cognitiveservices.speech.translation as translation
from dotenv import load_dotenv
import os
import numpy as np
import whisper
import torch
import sys
import time

load_dotenv()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = whisper.load_model("tiny", device=device) # cargando el modelo

fs = 16000
duration = 5

azurePushStream = None
suscrip = os.getenv("SUBSCRIPTION_AZURESPEECH")
azureregion = os.getenv("AZURE_SPEECHREGION")

print(sd.query_devices())

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)

    # Aseguramos la conversión a mono (si Stereo Mix da 2 canales)
    dataToSed = indata.copy()
    if dataToSed.ndim > 1:
        dataToSed = np.mean(dataToSed, axis=1, dtype=dataToSed.dtype)
    
    audiosBytes = dataToSed.tobytes()

    if azurePushStream:
        # Escribe los bytes directamente al conducto de Azure
        azurePushStream.write(audiosBytes)


def azureSetupRecognizer():

    
    global azurePushStream

    #CREAR CONEXION CON AZURE SPEECH
    azureSpeechset = translation.SpeechTranslationConfig(
        subscription= suscrip,
        region=azureregion,
    )

    #Aqui setteamos el audio que queramos que reconozca.
    azureSpeechset.speech_recognition_language = "cs-CZ"
    azureSpeechset.add_target_language("es")

    #Configuracion del formato de audio (16kHz, 16-bit, Mono)
    azureAudioFormat = speechsdk.audio.AudioStreamFormat(
        samples_per_second=fs,
        bits_per_sample=16,
        channels=1
    )

    #Crear el Stream de Empuje
    azurePushStream = speechsdk.audio.PushAudioInputStream(azureAudioFormat)
    azureAudioConfi = speechsdk.audio.AudioConfig(stream=azurePushStream)

    #Crear el reconocedor de palabras
    azureRecognizer = translation.TranslationRecognizer(
        translation_config=azureSpeechset,
        audio_config=azureAudioConfi
    )

    return azureRecognizer


def iniciarEscuchaContinua():

    azureRecognizer = azureSetupRecognizer()

    #Reconocimiento de palabras mientra hablas
    azureRecognizer.recognizing.connect(
        # lambda evt: evt.result.text,
        lambda evt: evt.result.translations["es"]
    )

    #Reconocimiento final, cuando detecta una pausa o fin de la frase
    azureRecognizer.recognizing.connect(
        # lambda evt: print(f"[FINAL]:   {evt.result.text}"),
        lambda evt: print(f"\n[FINAL TRAD]: {evt.result.translations["es"]}")
    )

    #eventos de errores
    azureRecognizer.session_stopped.connect(
        lambda evt: print('\nSesión de Azure detenida.')
    )
    azureRecognizer.canceled.connect(
        lambda evt: print(f'Reconocimiento cancelado: {evt.cancellation_details.reason}')
    )

    #iniciar el reconocimento de palabras de azure
    azureRecognizer.start_continuous_recognition_async()

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

    except KeyboardInterrupt:
        print("\n\n Proceso de transcripción detenido por el usuario.")
    except Exception as e:
        print(f"\n Ocurrió un error: {e}")
    finally:
        #Detener el reconocimiento y cerrer el stream
        azureRecognizer.stop_continuous_recognition_async()
        if azurePushStream:
            azurePushStream.close()
            print("Servicios detenidos")


iniciarEscuchaContinua()
import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

load_dotenv()

speech_config = speechsdk.SpeechConfig(
    subscription=os.getenv("SPEECH_KEY"),
    endpoint= os.getenv("ENDPOINT")
)

audio_config = speechsdk.audio.AudioOutputConfig(
    use_default_speaker=True
)

speech_config.speech_synthesis_voice_name="en-US-AvaMultilingualNeural"


speech_sintetizador = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=audio_config,
)

print("Enter some text that you want to speak: ")
text = input()

result_speech_sintetizador = speech_sintetizador.speak_text_async(text).get()

if result_speech_sintetizador.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print(f"Speech synthesized for tex [{text}]")
elif result_speech_sintetizador.reason == speechsdk.ResultReason.Canceled:
    cancel_detail = result_speech_sintetizador.cancellation_details
    print(f'Speech cancelled: {cancel_detail.reason}')

    if cancel_detail.reason == speechsdk.CancellationReason.Error:
        if cancel_detail.error_details:
            print(f'error details: {cancel_detail.error_details}')
            print('Are the key and endpoit provide ?') 

from email import message
from email.mime import audio
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys


recogniser = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

def greet():
    speaker.say("hello, i'm jenny your personal assistant")
    speaker.runAndWait()


mappings = {
    "greeting": greet
}


assistant =GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()

while True:
    try:
        with speech_recognition.Microphone() as mic:

            recogniser.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recogniser.listen(mic)

            message = recogniser.recognize_google(audio)
            message = message.lower()

        assistant.request(message)

    except speech_recognition.UnknownValueError:
        recogniser = speech_recognition.Recognizer()
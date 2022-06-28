import pyttsx3
import speech_recognition as recognizer

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f3')
activation_word = 'jenny'

def speak(text: str, rate: int = 150):
    engine.setProperty('rate', rate)
    engine.save_to_file(text, 'voice.mp3')
    engine.runAndWait()

def parseCommand():
    listener = recognizer.Recognizer()
    print('establishing Recognizer')

    with recognizer.Microphone() as mic:
        print('switching on the mic')
        listener.adjust_for_ambient_noise(mic)
        listener.energy_threshold = 1932
        listener.dynamic_energy_threshold = True
        listener.pause_threshold = 1.2

        print('listening via mic')
        print("please say something!")
        speech = listener.listen(mic)
        print('listening via mic')

    try:
        query = listener.recognize_google(speech, language='eng_gb')
        print(f'getting what was said..., you said: {query}')

    except Exception as exception:
        speak('I did not quite get that')
        print(exception)

    return query

speak('hello')
# while True:
#     speak('Hello, i am jenny your personal assistant.')
#     query = jenny.parseCommand().lower().split()
#     if jenny.activation_word in query:
#         jenny.speak('Hi, Ken')
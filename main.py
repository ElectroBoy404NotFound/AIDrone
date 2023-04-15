import speech_recognition as sr
from djitellopy import Tello

r = sr.Recognizer()
mic = sr.Microphone()

tello = Tello()
tello.connect()

print("Start talking!")

while True:
    try:
        with mic as source:
            audio = r.listen(source)
        words = r.recognize_google(audio)
        if words.find("take off") == 0:
            print("Talking off")
            tello.takeoff()
        elif words.find("land") == 0:
            print("Landing")
            tello.land()
    except sr.UnknownValueError:
        pass
    
import time
import speech_recognition as sr

# Record Audio
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening ...")
        audio = r.listen(source)
    try:
        print("You said: " + r.recognize_google(audio))
        time.sleep(1)
    except sr.UnknownValueError:
        print("Google Speech Recognition couldn't understand")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))



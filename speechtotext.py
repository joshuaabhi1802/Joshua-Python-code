import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
import speech_recognition as sr
def speech_to_text(address):
    audio=sr.AudioFile(address)
    with audio as source:
        speech=sr.Recognizer().record(source)
        try:
            text=sr.Recognizer().recognize_google(speech,language="en-US")
            print(text)
        except:
            print("Sorry couldn't understand")
if __name__ == "__main__":
    address=r"C:\Users\Admin\Downloads\recordspeech.wav"
    speech_to_text(address)
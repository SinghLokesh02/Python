import speech_recognition as sr

r = sr.Recognizer()
print("Say something! The computer will recognize it.")
with sr.Microphone() as source:
    audio = r.listen(source)
    print("Got it! Now to recognize it...")
    try:
        print("You said: " + r.recognize_google(audio))
    except Exception as e:
        print("I couldn't understand you.")
        print(f"Could not request results from Google Speech Recognition service {e}")




 

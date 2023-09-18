# This library provides the functionality for speech recognition.
import speech_recognition as sr
# This library allows you to control the keyboard and mouse to automate tasks.
import pyautogui
# his library enables you to manipulate PowerPoint presentations programmatically.

from pptx import Presentation


def main():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    # Initialize PowerPoint
    presentation = Presentation("E:\\College\\NOTES\\Minor project II.pptx")

    while True:
        with sr.Microphone() as source:
            print("Listening for commands...")
            audio = recognizer.listen(source)

        try:
            # Recognize the command
            command = recognizer.recognize_google(audio).lower()

            if "next" in command:
                # Simulate a keypress to go to the next slide
                pyautogui.press("right")
                print("Next slide.")
            elif "previous" in command:
                # Simulate a keypress to go to the previous slide
                pyautogui.press("left")
                print("Previous slide.")
            elif "close" in command:
                break  # Exit the loop if the user says "exit"

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("Could not request results; check your network connection.")


if __name__ == "__main__":
    main()

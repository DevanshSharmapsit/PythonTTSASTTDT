import pyttsx3

text_speech = pyttsx3.init()

answer = input("what you w to convert to speech")
text_speech.say(answer)
text_speech.runAndWait()
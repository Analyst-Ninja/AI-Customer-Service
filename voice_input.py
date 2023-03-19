import speech_recognition  as sr
import pyttsx3 as ts

def voice_in():
    r = sr.Recognizer()
    engine = ts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    with sr.Microphone() as source:
        print("Speak anything:")
        r.pause_threshold = 1
        audio = r.listen(source,10,10)
        with open('speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
        try:
            text = r.recognize_google(audio)
            customer_prompt = text
            engine.say(customer_prompt)
            engine.runAndWait()
            print("You said : {}".format(text))
            with open("speech.wav", "rb") as file:
                # Read the binary data
                audio_binary = file.read()
            return customer_prompt, audio_binary
        except:
            engine.say("Sorry, I did not understand what you said")
            engine.runAndWait() 
        # Open the audio file
        
        
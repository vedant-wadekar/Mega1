import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak (text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open insta" in c.lower():
        webbrowser.open("https://instagram.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]  
        link = musiclib.music[song] 
        webbrowser.open(link)


if __name__=="__main__":
    speak("vedant we are starting... ")
    while True:
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listing...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "hello"):
                speak("Ya")
                # Listern for command
                with sr.Microphone() as source:
                    
                    speak("ji maharaj")
                    print("kaushik Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    processCommand(command)



        except Exception as e:
            print("Error; {0}".format(e))
           
           

import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import cohere # type: ignore

music_library = {
     "lemon tree" : "https://open.spotify.com/album/3epesmrZX0KYpeImQtcVUa",
     "song 2": "https://open.spotify.com/track/2PEYf3S9LhnHZCfoPWxegG",
     "yesterday" : "https://open.spotify.com/track/7mwF74tjZx4L2bjJNo7l72"
}
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty('rate', 140)

def speak(text):
 engine.say(text)
 engine.runAndWait()

def process_command():  
    if "go to amazon" in r.recognize_google(audio).lower():
              speak("Opening Amazon for you mister john wick and also happy hunting mister wick")
              
              webbrowser.open("https://www.amazon.in/")
    elif "go to amazon cart" in r.recognize_google(audio).lower():
              speak("Opening Amazon cart for you mister john wick and also happy hunting mister wick")
              
              webbrowser.open("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart") 
    elif "go to kali" in r.recognize_google(audio).lower():
              speak("Opening kali for you mister john wick and also happy hunting mister wick")
              
              webbrowser.open("http://kali.org/")  
    elif r.recognize_google(audio).lower().startswith("play"):
         speak("playing song for you mister john wick and also happy hunting mister wick")
         
         song = r.recognize_google(audio).lower().split(" ",1)[1]
         webbrowser.open(music_library[song])
    elif "news" in r.recognize_google(audio).lower():
         speak("as you want mister wick and also happy hunting mister wick")
         news = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=879d5b45a4f14b0e9a92e39e32faa027")
         articles = news.json().get("articles")
         for i in articles:
              speak(i["title"])    
    else:     
         co = cohere.Client('AhjaR7uPviTz8mATeeGf7uKkXePtRCLe9HSOAt18')
         response = co.generate(prompt=r.recognize_google(audio), model='command-r-plus')
         speak(response.generations[0].text)

if __name__ == "__main__":
    while True:
      
      with sr.Microphone() as client_voice:
         print("sir sir now you can speak")
         audio = r.listen(client_voice,phrase_time_limit=2)
      try:
         print(f"so what you are saying is ...{r.recognize_google(audio)}")
         
         if(r.recognize_google(audio).lower() == "natasha"):
            speak("i am natasha ,,how can i help you mister john wick.")
            with sr.Microphone() as client_voice:
              print("listening....")
              audio = r.listen(client_voice)
              if(r.recognize_google(audio).lower()=="your name"):
                 speak("my name is natasha mister wick")
         else:
              process_command()          
            
      except sr.UnknownValueError:
          print("Google Speech Recognition could not understand audio")
      except sr.RequestError as e:
          print("Could not request results from Google Speech Recognition service; {0}".format(e))  
from wit import Wit
from gtts import gTTS 
import os
import app
import speech_recognition as sr
import TwitterFuctions
import FacebookFunctions
import GoogleSearchFunctions
witKey = os.getenv("witApiKey")
r = sr.Recognizer()


def wit():
  intro()
  client = Wit(witKey)
  results = None
  with sr.Microphone() as source:
     audio = r.record(source, duration=5)
     results = client.speech(audio, {'Content-Type': 'audio/wav'})
  commandID = None
  for elements in results["intents"]:
    commandID = elements["id"]
  return action(commandID)

def intro():
  text = "Welcome to HearEverything, please tell us what do you want to do"
  language = "en"
  speech = gTTS(text = text, lang = language, slow = False)
  speech.save("intro.mp3")
  return os.system("start intro.mp3")

def readCommand(command):
  text = None
  language = "en"
  if command == "552986868917206":
    text = "You have choosen twitter"
  elif command == "2988512127933065":
    text = "You have choosen facebook"
  elif command == "2939217719529274":
    text = "You have choosen to search something on google/wikipedia"
  else:
    text = "Sorry I did not get that, can you repeat it again please?"
  speech = gTTS(text = text, lang = language, slow = False)
  speech.save("action.mp3")
  return os.system("start action.mp3")

def action(command):
  language = "en"
  readCommand(command)

  #Twitter
  if command == "552986868917206":

    text = "In the next 9 second we will record the tweet you want to post"
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save("tweet.mp3")
    os.system("start tweet.mp3")
    command = None
    with sr.Microphone() as source:
      audio_data = r.record(source, duration=9)
      command = r.recognize_google(audio_data)
    text2 = "You are going to tweet " + command
    speech2 = gTTS(text = text2, lang = language, slow = False)
    speech2.save("tweet2.mp3")
    os.system("start tweet2.mp3")
    twitter(command)
    text3 = "Your tweet has been posted!"
    speech3 = gTTS(text = text3, lang = language, slow = False)
    speech3.save("tweet3.mp3")
    os.system("start tweet3.mp3")

  #Facebook
  elif command == "2988512127933065":

    text = "In the next 9 second we will record the post you want to put on your wall"
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save("face.mp3")
    os.system("start face.mp3")
    command = None
    with sr.Microphone() as source:
      audio_data = r.record(source, duration=9)
      command = r.recognize_google(audio_data)
    text2 = "You are going to post " + command
    speech2 = gTTS(text = text2, lang = language, slow = False)
    speech2.save("face2.mp3")
    os.system("start face2.mp3")
    face(command)
    text3 = "Your post has been posted!"
    speech3 = gTTS(text = text3, lang = language, slow = False)
    speech3.save("face3.mp3")
    os.system("start face3.mp3")

    face()
  
  #Google
  elif command == "2939217719529274":

    text = "Beware, this is going to be loooooooooooong. Prepare to take notes"
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save("google.mp3")
    os.system("start google.mp3")
    text2 = "In the next 9 second we will record the post you want to put on your wall"
    speech2 = gTTS(text = text2, lang = language, slow = False)
    speech.save("face2.mp3")
    os.system("start face2.mp3")
    command = None
    with sr.Microphone() as source:
      audio_data = r.record(source, duration=9)
      command = r.recognize_google(audio_data)
    text3 = "You are going to search " + command
    speech3 = gTTS(text = text3, lang = language, slow = False)
    speech3.save("google3.mp3")
    os.system("start google3.mp3")
    resume = google(command)
    resumeSpeech = gTTS(text = resume, lang = language, slow = False)
    resumeSpeech.save("research.mp3")
    os.system("start research.mp3")

  #Error
  else:
    text = "Sorry we got an error, we will have to start over"
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save("apologize.mp3")
    os.system("start apologize.mp3")

def face(command):
  FacebookFunctions.login()
  FacebookFunctions.postingFace(command)

def twitter(command):
  TwitterFuctions.login()

def google(command):
  return GoogleSearchFunctions.search(command)


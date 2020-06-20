from wit import Wit
from gtts import gTTS 
import os
import app

def wit():
  intro()
  client = Wit("57R3JGXTZ6BF3ASCVE6G35OBBEJEMMYF")
  results = None
  with open('16-122828-0002.wav', 'rb') as f:
    results = client.speech(f, {'Content-Type': 'audio/wav'})
  commandID = None
  for elements in results["intents"]:
    commandID = elements["id"]
  print(commandID)
  readCommand(commandID)
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
  if command == "550491782311147":
    text = "at least test works"
  elif command == "552986868917206":
    text = "twitter"
  elif command == "2002521963215550":
    text = "youtube"
  elif command == "2988512127933065":
    text = "facebook"
  elif command == "2939217719529274":
    text = "google"
  else:
    text = "Sorry I did not get that, can you repeit it again please?"
  speech = gTTS(text = text, lang = language, slow = False)
  speech.save("action.mp3")
  return os.system("start action.mp3")

def action(command):
  if command == "550491782311147":
    test()
  elif command == "552986868917206":
    twitter()
  elif command == "2002521963215550":
    youtube()
  elif command == "2988512127933065":
    facebook()
  elif command == "2939217719529274":
    google()
  else:
    print("Error")

def facebook():
  print("Posted")

def twitter():
  print("tweeted")

def youtube():
  print("played")

def google():
  print("google")

def test():
  print("at least test works")



from wit import Wit
from gtts import gTTS 
import os
import app
import facebook

faceApiKey = os.getenv("faceKey")
witKey = os.getenv("witApiKey")
faceToken = os.getenv("faceAppToken")

def wit():
  intro()
  client = Wit(witKey)
  results = None
  with open('16-122828-0002.wav', 'rb') as f:
    results = client.speech(f, {'Content-Type': 'audio/wav'})
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
    text = "Sorry I did not get that, can you repeat it again please?"
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
    face()
  elif command == "2939217719529274":
    google()
  else:
    print("Error")

def face():
  print("posted!")

def twitter():
  print("tweeted")

def youtube():
  print("played")

def google():
  print("google")

def test():
  print("at least test works")

face()

from wit import Wit
import app

def wit():
  client = Wit("57R3JGXTZ6BF3ASCVE6G35OBBEJEMMYF")
  results = None
  with open('16-122828-0002.wav', 'rb') as f:
    results = client.speech(f, {'Content-Type': 'audio/wav'})
  command = None
  for elements in results["intents"]:
    command = elements["name"]
  print(command)
  return command

def facebook():
  print("Posted")

def twitter():
  print("tweeted")

def youtube():
  print("played")
  
def test():
  print("at least test works")

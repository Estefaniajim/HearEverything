from wit import Wit
import app

def wit():
  client = Wit("57R3JGXTZ6BF3ASCVE6G35OBBEJEMMYF")
  results = None
  with open('16-122828-0002.wav', 'rb') as f:
    results = client.speech(f, {'Content-Type': 'audio/wav'})
  command = None
  for elements in results["intents"]:
    command = elements["id"]
  print(command)
  return action(command)

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



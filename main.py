from wit import Wit
from gtts import gTTS
import os
import speech_recognition as sr
import TwitterFuctions
import FacebookFunctions
import GoogleSearchFunctions
from dotenv import load_dotenv

load_dotenv()
# Load environment variables
witKey = os.getenv("witApiKey")
if not witKey:
    raise ValueError("Wit.ai API key not found. Set 'witApiKey' as an environment variable.")

r = sr.Recognizer()

def witCall():
    """Main function to handle voice commands using Wit.ai."""
    print("Wit function called!")
    intro()
    client = Wit(witKey)

    try:
        with sr.Microphone() as source:
            print("Listening for 7 seconds...")
            audio = r.record(source, duration=7)
            print("Processing audio...")
            results = client.speech(audio.get_wav_data(), {'Content-Type': 'audio/wav'})
        commandID = None
        for elements in results["intents"]:
            commandID = elements["id"]
            break  # Use the first intent found

        if commandID is None:
            raise ValueError("No valid command found.")

        print(f"Command ID: {commandID}")
        action(commandID)

    except Exception as e:
        print(f"Error during voice command processing: {e}")
        play_audio("Sorry, we encountered an error. Please try again.")

def intro():
    """Plays an introductory message."""
    text = "Welcome to HearEverything, please tell us what you want to do."
    play_audio(text)

def play_audio(text):
    """Convert text to speech and play the audio."""
    language = "en"
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("output.mp3")
    os.system("start output.mp3")

def readCommand(command):
    """Reads the user's selected command."""
    responses = {
        "552986868917206": "You have chosen Twitter.",
        "1135931194419043": "You have chosen Facebook.",
        "1698371974430723": "You have chosen to search something on Google or Wikipedia.",
    }
    text = responses.get(command, "Sorry, I did not understand that. Can you repeat it?")
    play_audio(text)

def action(command):
    """Handles the actions based on the command ID."""
    readCommand(command)

    if command == "552986868917206":  # Twitter
        handle_twitter_action()

    elif command == "1135931194419043":  # Facebook
        print("Facebook was choosen")
        handle_facebook_action()

    if command == "1698371974430723":  # Google/Wikipedia
        print("Google was choosen")
        handle_google_action()

    else:
        play_audio("Sorry, we encountered an error. We will have to start over.")

def handle_twitter_action():
    """Handles Twitter-related actions."""
    play_audio("There si no twitter")
    play_audio("In the next 9 seconds, we will record the tweet you want to post.")
    # try:
    #     with sr.Microphone() as source:
    #         audio_data = r.record(source, duration=9)
    #         tweet_content = r.recognize_google(audio_data)

    #     play_audio(f"You are going to tweet: {tweet_content}")
    #     TwitterFuctions.login()
    #     TwitterFuctions.post_tweet(tweet_content)
    #     play_audio("Your tweet has been posted!")

    # except Exception as e:
    #     print(f"Error while handling Twitter action: {e}")
    #     play_audio("Failed to post your tweet. Please try again.")

def handle_facebook_action():
    """Handles Facebook-related actions."""
    play_audio("In the next 9 seconds, we will record the post you want to put on your wall.")
    try:
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=9)
            post_content = r.recognize_google(audio_data)

        play_audio(f"You are going to post: {post_content}")
        FacebookFunctions.login()
        FacebookFunctions.postingFace(post_content)
        play_audio("Your post has been posted!")

    except Exception as e:
        print(f"Error while handling Facebook action: {e}")
        play_audio("Failed to post your Facebook message. Please try again.")

def handle_google_action():
    """Handles Google/Wikipedia search actions."""
    play_audio("In the next 9 seconds, we will record what you want to search for.")
    try:
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=9)
            search_query = r.recognize_google(audio_data)

        play_audio(f"You are going to search for: {search_query}")
        summary = GoogleSearchFunctions.search(search_query)
        play_audio(f"Search result summary: {summary}")

    except Exception as e:
        print(f"Error while handling Google action: {e}")
        play_audio("Failed to process your search. Please try again.")
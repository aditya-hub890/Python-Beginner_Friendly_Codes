import speech_recognition as sr
from elevenlabs import ElevenLabs
from pydub.playback import play 
from pydub import AudioSegment
import io
import webbrowser
import Music_Lib_02
import requests
from openai import OpenAI


recongnizer=sr.Recognizer()

def speak(text):
    # Set your API key
    api_key = "Your_api_key" # Get your api key from elevenlabs
    client = ElevenLabs(api_key=api_key)

    # Generate speech
    audio = client.text_to_speech.convert(
        text=text,
        voice_id="Voice_ID",  # use voice_id here 
        model_id="eleven_multilingual_v2"
    )
        
    # To increase or decrease the volume
    audio_byt=b"".join(audio)
    audio_bytes=io.BytesIO(audio_byt)

    audio_segment=AudioSegment.from_file(audio_bytes,format="mp3")

    Audio=audio_segment + 8 # you can increase or decrease by changing the value

    # Play the audio
    play(Audio)


# A function for operations to perform
def order(a):
    if "open chat" in a.lower():
        webbrowser.open("https://chatgpt.com")
    elif "open google" in a.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in a.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in a.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in a.lower():
        webbrowser.open("https://facebook.com")
    elif a.lower().startswith("play"):
        song=a.lower().split(" ")[1]
        link=Music_Lib_02.music[song]
        webbrowser.open(link)
    elif "news" in a.lower():
        newsapi="Your_news_api_key" # Get your news api key from news api
        response=requests.get (f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        articles=response.json().get("articles",[])
        if not articles:
            speak("no news articles found in the country")
        else:
            for i,article in enumerate(articles,start=1):
                speak(article["title"])
                print(f"{i}. {article["title"]}")
    else:
        
        client=OpenAI(api_key="Your_openai_api_key") # Get it from openai api 

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What's the capital of France?"}
            ]
        )

        speak(completion.choices[0].message.content)

            

# The program for th execution
if __name__=="__main__":
    speak("Initializing jarvis")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=recongnizer.listen(source,timeout=2,phrase_time_limit=1)
                word=recongnizer.recognize_google(audio)
                print("Recognizing...")
                if word.lower()=="jarvis":
                    speak("Yes sir")
            with sr.Microphone() as source:
                audio=recongnizer.listen(source)
                command=recongnizer.recognize_google(audio)
                order(command)

        except Exception as e:
            print(e)

            
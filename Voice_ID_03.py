# Get all the different voices and voice IDs from this code 
from elevenlabs.client import ElevenLabs

client=ElevenLabs(api_key="Your_api_key") # Get your api key from elevenlabs

response=client.voices.get_all()

for voice in response.voices:
    print(f"{voice.name}-{voice.voice_id}")

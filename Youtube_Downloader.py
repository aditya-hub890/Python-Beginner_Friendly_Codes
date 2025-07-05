import subprocess

url="Video_url"
command=["yt-dlp",url]

subprocess.run(command)

# Want to custom output and file name, replace the value of command with this:
command=[
    "yt-dlp",
    "-o","download/%(title)s.%(ext)s", # title will be the name of the file and the ext will be the extension
    url
]
# To download audio only replace the value of command with this:
command=[
    "yt-dlp",
    "-x",
    "--audio_format","mp3"
    "-o","audio/%(title)s.%(ext)s",
    url
]

# To get the Metadeta without downloading anything
import json

url="Video_url"
command=["yt-dlp","--dump-json",url]

result=subprocess.run(command,capture_output=True,text=True)
metadata=result.json(result.stdout)

print(f"Title:{metadata["title"]}")
print(f"Duration:{metadata["duration"]}")


# To download a playlist 
url="playlist_url"
command=[
    "yt-dlp",
    "-o","playlist/%(playlist_title)s/%(title)s.%(ext)s"
]




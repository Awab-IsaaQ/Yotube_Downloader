import subprocess
import os
subprocess.check_call(["pip", "install", "pytube"])

from pytube import Playlist
from pytube import YouTube

url = input("Enter the Youtube link: ")
indexer = 1

try:
    # Create a Playlist object
    playlist = list(Playlist(url).video_urls)
    lenlist = len(playlist)

    for video_url in playlist:
        yt = YouTube(video_url)
        if (os.path.exists(yt.title+".mp4")):
            print(f' [{indexer}/{lenlist}] Downloaded: {yt.title} ======= Already Exists')
            continue

        video_stream = yt.streams.get_highest_resolution()
        video_stream.download()
        print(f' [{indexer}/{lenlist}] Downloaded: {yt.title}')
        indexer += 1

except Exception as e:
    try:
        yt = YouTube(url)
        if not(os.path.exists(yt.title+".mp4")):
            print(os.path.exists(yt.title))
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download()
            print(f"[1/1] Downloaded: {yt.title}")
        else:print(f"[1/1] Downloaded: {yt.title} ======= Already Exists")


    except Exception as aha:print("Allah Kreem my friend ", e , aha)

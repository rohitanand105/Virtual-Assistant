from pytube import YouTube

from pytube import YouTube
from pytube.contrib.playlist import Playlist

def download_video(url, path='', email=None, password=None):
    try:
        if email and password:
            YouTube(email=email, password=password).authenticate()

        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(path)
        print("Download successful!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = "https://www.youtube.com/watch?v=kBQ2ilj3VO4"  # Example URL
email = "rohitanand105@gmail.com"  # Your YouTube email
password = "rohit anand"  # Your YouTube password
download_video(url, path='./', email=email, password=password)

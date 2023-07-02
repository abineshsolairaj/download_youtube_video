import os
from pytube import YouTube, Playlist

youtubeURL = input("Enter the youtube url here: ")
video = YouTube(youtubeURL)
video.streams.get_highest_resolution().download()
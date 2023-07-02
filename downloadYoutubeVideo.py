import os
from pytube import YouTube, Playlist

youtubeURL = input("Enter the youtube url here: ")
video = YouTube(youtubeURL)
video.streams.get_highest_resolution().download()


# Replace the lines 272, 273 with the following line in cipher.py of pytube
# r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
# r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
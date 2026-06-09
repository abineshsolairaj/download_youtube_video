# download_youtube_video

A small command-line script for downloading a YouTube video at its highest available resolution.

## Why `pytubefix`?

The original script used [`pytube`](https://github.com/pytube/pytube), which is no longer actively maintained and breaks frequently as YouTube changes its player. The fix required users to manually edit `cipher.py` inside the installed library — a brittle workaround. This project now uses [`pytubefix`](https://github.com/JuanBindez/pytubefix), a maintained drop-in replacement that keeps the cipher logic up to date.

## Install

```bash
pip install -r requirements.txt
```

## Usage

```bash
python downloadYoutubeVideo.py
```

You will be prompted for a YouTube URL. The video is saved to the current working directory.

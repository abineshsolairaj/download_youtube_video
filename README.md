# download_youtube_video

A small command-line script for downloading a YouTube video at its highest available resolution.

## Features

- Downloads a single YouTube video at the highest resolution available in a progressive stream.
- Friendly error messages instead of raw stack traces when something goes wrong.
- No manual library patching required — uses the maintained `pytubefix` library.

## Requirements

- Python 3.8 or newer
- `pip` for installing dependencies

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/abineshsolairaj/download_youtube_video.git
cd download_youtube_video
pip install -r requirements.txt
```

Using a virtual environment is recommended:

```bash
python -m venv .venv
source .venv/bin/activate    # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run the script and paste a YouTube URL when prompted:

```bash
python downloadYoutubeVideo.py
```

Example session:

```
$ python downloadYoutubeVideo.py
Enter the youtube url here: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Downloading: Rick Astley - Never Gonna Give You Up (Official Music Video)
Saved to: /home/you/download_youtube_video/Rick Astley - Never Gonna Give You Up (Official Music Video).mp4
```

The file is saved to the current working directory.

## Why `pytubefix`?

The original script used [`pytube`](https://github.com/pytube/pytube), which is no longer actively maintained and breaks frequently as YouTube changes its player. Keeping it working required users to manually edit `cipher.py` inside the installed library — a brittle workaround. This project now uses [`pytubefix`](https://github.com/JuanBindez/pytubefix), a maintained drop-in replacement that keeps the cipher logic up to date.

## Troubleshooting

- **`Failed to download video: ...`** — the URL was rejected by YouTube or by the library. Confirm the URL is correct, the video is public, and that your `pytubefix` is up to date (`pip install --upgrade pytubefix`).
- **No video downloaded but no error printed** — no progressive stream was available for that video. Higher-resolution YouTube videos sometimes split video and audio into separate streams; this script intentionally sticks to a single progressive stream for simplicity.
- **`ModuleNotFoundError: No module named 'pytubefix'`** — run `pip install -r requirements.txt` inside the right environment.

## Running the tests

Unit tests use `unittest` and mock the network — no real download is required:

```bash
python -m unittest test_downloadYoutubeVideo -v
```

## Project structure

```
.
├── downloadYoutubeVideo.py        # entry point
├── test_downloadYoutubeVideo.py   # unit tests
├── requirements.txt               # Python dependencies
├── README.md                      # this file
└── .gitignore
```

## License

This project is provided as-is for educational purposes. Respect YouTube's Terms of Service and only download content you have the right to download.

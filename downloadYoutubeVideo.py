from pathlib import Path

from pytubefix import YouTube
from pytubefix.exceptions import PytubeFixError


def download_video(url: str, output_dir: str = ".") -> Path:
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    if stream is None:
        raise RuntimeError("No downloadable stream found for this video.")

    print(f"Downloading: {yt.title}")
    file_path = stream.download(output_path=output_dir)
    return Path(file_path)


def main() -> None:
    url = input("Enter the youtube url here: ").strip()
    if not url:
        print("No URL provided. Exiting.")
        return

    try:
        path = download_video(url)
    except PytubeFixError as exc:
        print(f"Failed to download video: {exc}")
        return
    except Exception as exc:
        print(f"Unexpected error: {exc}")
        return

    print(f"Saved to: {path}")


if __name__ == "__main__":
    main()

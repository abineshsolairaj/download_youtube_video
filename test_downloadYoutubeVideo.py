import io
import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from pytubefix.exceptions import PytubeFixError, VideoUnavailable

import downloadYoutubeVideo as dl


class DownloadVideoTests(unittest.TestCase):
    @patch("downloadYoutubeVideo.YouTube")
    def test_returns_downloaded_path(self, mock_yt_cls):
        stream = MagicMock()
        stream.download.return_value = "/tmp/video.mp4"
        yt = MagicMock(title="Test Title")
        yt.streams.get_highest_resolution.return_value = stream
        mock_yt_cls.return_value = yt

        result = dl.download_video("https://example.test/v", output_dir="/tmp")

        mock_yt_cls.assert_called_once_with("https://example.test/v")
        stream.download.assert_called_once_with(output_path="/tmp")
        self.assertEqual(result, Path("/tmp/video.mp4"))

    @patch("downloadYoutubeVideo.YouTube")
    def test_raises_when_no_stream_available(self, mock_yt_cls):
        yt = MagicMock(title="No Streams")
        yt.streams.get_highest_resolution.return_value = None
        mock_yt_cls.return_value = yt

        with self.assertRaises(RuntimeError) as ctx:
            dl.download_video("https://example.test/v")
        self.assertIn("No downloadable stream", str(ctx.exception))

    @patch("downloadYoutubeVideo.YouTube")
    def test_propagates_pytubefix_error(self, mock_yt_cls):
        mock_yt_cls.side_effect = VideoUnavailable("xyz")
        with self.assertRaises(PytubeFixError):
            dl.download_video("https://example.test/v")


class MainCliTests(unittest.TestCase):
    def _run_main(self, fake_input):
        captured = io.StringIO()
        with patch("builtins.input", return_value=fake_input), \
             patch("sys.stdout", new=captured):
            dl.main()
        return captured.getvalue()

    def test_empty_input_exits_cleanly(self):
        output = self._run_main("")
        self.assertIn("No URL provided", output)

    @patch("downloadYoutubeVideo.download_video")
    def test_success_prints_saved_path(self, mock_download):
        mock_download.return_value = Path("/tmp/video.mp4")
        captured = io.StringIO()
        with patch("builtins.input", return_value="https://example.test/v"), \
             patch("sys.stdout", new=captured):
            dl.main()
        self.assertIn("Saved to: /tmp/video.mp4", captured.getvalue())

    @patch("downloadYoutubeVideo.download_video")
    def test_pytubefix_error_prints_friendly_message(self, mock_download):
        mock_download.side_effect = VideoUnavailable("xyz")
        captured = io.StringIO()
        with patch("builtins.input", return_value="https://example.test/v"), \
             patch("sys.stdout", new=captured):
            dl.main()
        out = captured.getvalue()
        self.assertIn("Failed to download video", out)
        self.assertNotIn("Traceback", out)

    @patch("downloadYoutubeVideo.download_video")
    def test_unexpected_error_is_caught(self, mock_download):
        mock_download.side_effect = RuntimeError("boom")
        captured = io.StringIO()
        with patch("builtins.input", return_value="https://example.test/v"), \
             patch("sys.stdout", new=captured):
            dl.main()
        out = captured.getvalue()
        self.assertIn("Unexpected error: boom", out)


if __name__ == "__main__":
    unittest.main()

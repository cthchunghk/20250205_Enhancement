"""
Please install ffmpeg library to make the transformation
"""
import yt_dlp
import os
from pathlib import Path
from app.utils.path_setting import youtube_download_path


class YouTubeDownloader():

    def downloadAudio(url, output_path=youtube_download_path):
        format = 'mp3'
        # Set up options for yt-dlp to download only audio
        ydl_opts = {
            'format': 'bestaudio/best',  # best audio quality
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Ensure the correct key here
                'preferredcodec': format,  # Convert to mp3
                'preferredquality': '192',  # Audio quality (bitrate)
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }

        # Download the audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            yinfo = ydl.extract_info(url, download=True)
        filename = f"{yinfo['title']}"
        final_path = f'{os.path.join(output_path, (filename+'.'+format))}'
        return final_path

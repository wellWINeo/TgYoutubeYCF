import asyncio
from yt_dlp import YoutubeDL


async def download_video(url: str, path: str):
    options = {'outtmpl': path}

    with YoutubeDL(options) as ydl:
        await asyncio.get_running_loop().run_in_executor(None, ydl.download, [url])


async def read_file(path: str):
    with open(path, 'rb') as file:
        return file.read()

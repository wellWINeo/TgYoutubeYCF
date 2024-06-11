import os
from telegram import Bot
from yt_dlp import YoutubeDL
from ycf import YCF


def get_bot() -> Bot:
    token = os.environ["TG_TOKEN"]
    return Bot(token)


async def send_welcome(chat_id: int) -> None:
    bot = get_bot()
    async with bot:
        await bot.send_message(
            chat_id=chat_id,
            text="Welcome!"
        )


async def send_help(chat_id: int) -> None:
    async with get_bot() as bot:
        await bot.send_message(
            chat_id=chat_id,
            text="Send me a youtube's url to download!"
        )


async def send_youtube_video(chat_id: int, url: str) -> None:
    tmp_path = os.environ["TEMP_VIDEO_PATH"]
    cookies_path = os.path.join(tmp_path, "cookies.txt")

    with open(cookies_path, 'w') as cookies_file:
        cookies_file.writelines(os.environ["YT_COOKIES"])

    options = {
        'outtmpl': os.path.join(tmp_path, "video"),
        'cookies': cookies_path,
        'format': 'bestvideo[height<=1920]+bestaudio/best[height<=1080]/best',
        'ffmpeg_location': os.environ["FFMPEG_PATH"],
        'extractor_args': {'youtube:player_client': 'android'},
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }],
        'cachedir': False,
        'quiet': True,
    }

    with YoutubeDL(options) as ydl:
        metadata = ydl.extract_info(url, download=True)

    video_file = os.listdir(tmp_path)[0]
    video_path = os.path.join(tmp_path, video_file)

    print(f"File downloaded to {video_file}")

    async with get_bot() as bot:
        await bot.send_video(
            chat_id=chat_id,
            video=video_path,
            width=metadata["width"],
            height=metadata["height"],
            duration=metadata["duration"],
            caption=metadata["title"],
            supports_streaming=True,
        )

    if YCF.isOutside():
        os.remove(video_path)


async def send_exhaust_message(chat_id: int) -> None:
    async with get_bot() as bot:
        await bot.send_message(
            chat_id=chat_id,
            text="What the fuck you want?"
        )

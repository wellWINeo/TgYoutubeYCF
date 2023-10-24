import asyncio
import os
from telegram import Bot
from video_funcs import download_video, read_file


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
    video_path = os.environ["TEMP_VIDEO_FILE"]

    await download_video(url, video_path)

    await asyncio.sleep(2)

    video = await read_file(video_path)

    async with get_bot() as bot:
        await bot.send_video(
            chat_id=chat_id,
            video=video
        )

    os.remove(video_path)


async def send_exhaust_message(chat_id: int) -> None:
    async with get_bot() as bot:
        await bot.send_message(
            chat_id=chat_id,
            text="What the fuck you want?"
        )

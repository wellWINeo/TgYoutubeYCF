import re
from handlers import send_help, send_welcome, send_youtube_video, send_exhaust_message


async def handle_update(update: dict) -> None:
    chat_id = update["message"]["chat"]["id"]
    message = update["message"]["text"]

    match message:
        case "/start":
            await send_welcome(chat_id)
        case "/help":
            await send_help(chat_id)
        case message_text if is_youtube_url(message_text):
            await send_youtube_video(chat_id, message_text)
        case _:
            await send_exhaust_message(chat_id)


def is_youtube_url(url: str) -> bool:
    regex = r"^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$"

    return True if re.match(regex, url) else False

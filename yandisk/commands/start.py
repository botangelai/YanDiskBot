from yandisk.events import message

@message(pattern="/start")
async def start(event):
    await event.reply(
        f"""
**Hey!
I'm Yandex Drive Upload Bot. I can upload files (Telegram files as well as URLs) to your Yandex Drive, if you authorise me.
Use/login to authorise me.**
"""
    )

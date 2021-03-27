import telegram


def upload_post_to_chanal(token, chanal_name, text, image):
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chanal_name, photo=open(image, 'rb'))
    bot.send_message(chat_id=chanal_name, text=text)


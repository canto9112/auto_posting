import telegram


def upload_post_to_chanal(token, chanal_name, text, image):
    with open(image, "rb") as file:
        image_file = file.read()

    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chanal_name, photo=image_file)
    bot.send_message(chat_id=chanal_name, text=text)


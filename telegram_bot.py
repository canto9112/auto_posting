import telegram
from environs import Env


def upload_post_to_chanal(bot, chanal_name, text, image):
    bot.send_photo(chat_id=chanal_name, photo=open(image, 'rb'))
    bot.send_message(chat_id=chanal_name, text=text)


if __name__ == '__main__':
    env = Env()
    env.read_env()

    token = env('TELEGRAM_BOT_TOKEN')

    bot = telegram.Bot(token=token)

    chanal_name = '@auto_posting_vk_tg'
    test_message = 'hello world'
    photo = 'test_photo.jpg'

    upload_post_to_chanal(bot, chanal_name, test_message, photo)

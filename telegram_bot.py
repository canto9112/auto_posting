import telegram
from environs import Env

if __name__ == '__main__':
    env = Env()
    env.read_env()

    token = env('TELEGRAM_BOT_TOKEN')

    bot = telegram.Bot(token=token)

    chanal_name = '@auto_posting_vk_tg'
    test_message = 'hello world'

    bot.send_message(chat_id=chanal_name, text=test_message)
    print(bot.get_me())
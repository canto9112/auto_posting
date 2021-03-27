import vk_bot
import telegram_bot
import facebook_bot
from environs import Env


def main():
    env = Env()
    env.read_env()

    vk_token = env('VK_USER_TOKEN')
    telegram_token = env('TELEGRAM_BOT_TOKEN')
    facebook_token = env('FACEBOOK_TOKEN')

    test_message = 'Тест 2345'
    photo = 'test_photo.jpg'

    vk_owner_id = 203517016
    vk_album_id = '280071703'
    telegram_chanal_name = '@auto_posting_vk_tg'
    facebook_group_id = 472212560631956

    vk_bot.upload_image_alboum(vk_token, photo, vk_album_id, vk_owner_id, test_message)
    telegram_bot.upload_post_to_chanal(telegram_token, telegram_chanal_name, test_message, photo)
    facebook_bot.posting_post(facebook_token, test_message, facebook_group_id, photo)


if __name__ == '__main__':
    main()

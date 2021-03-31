import argparse
import os

from environs import Env

import facebook_bot
import google_sheets
import telegram_bot
import vk_bot


def delete_image(image_name):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), image_name)
    os.remove(path)


def get_line_number():
    parser = argparse.ArgumentParser(
        description=''
    )
    parser.add_argument('number', help='Вставить номер строки где в А1 - текст, в В1 - ссылка на картинку')
    args = parser.parse_args()
    return args.number


def main():
    env = Env()
    env.read_env()

    vk_token = env('VK_USER_TOKEN')
    vk_group_id = env.int('VK_GROUP_ID')
    vk_album_id = env('VK_ALBOUM_ID')

    telegram_token = env('TELEGRAM_BOT_TOKEN')
    telegram_chanal_name = env('TELEGRAM_CHANAL_NAME')

    facebook_token = env('FACEBOOK_TOKEN')
    facebook_group_id = env('FACEBOOK_GROUP_ID')

    google_config_file = env('GOOGLE_CONFIG_FILE')
    google_sheet_id = env('GOOGLE_SHEET_ID')

    line_number = get_line_number()

    text, image = google_sheets.get_text_and_imagename(line_number, google_config_file, google_sheet_id)

    try:
        vk_bot.upload_image_alboum(vk_token, image, vk_album_id, vk_group_id, text)
        telegram_bot.upload_post_to_chanal(telegram_token, telegram_chanal_name, text, image)
        facebook_bot.posting_post(facebook_token, text, facebook_group_id, image)
    except ValueError:
        text, image = google_sheets.get_text_and_imagename(line_number, google_config_file, google_sheet_id)
    finally:
        delete_image(image)


if __name__ == '__main__':
    main()

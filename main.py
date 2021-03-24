from environs import Env
import vk_api
from pprint import pprint


def upload_image_alboum(token, photo, album_id, owner_id):
    vk_session = vk_api.VkApi(token=token)
    upload = vk_api.VkUpload(vk_session)

    photo_img = upload.photo(photo,
                             album_id=album_id,
                             group_id=owner_id)
    image_id = photo_img[0]['id']
    return image_id


def upload_post_to_wall(token, text, owner_id, media_id):
    vk_session = vk_api.VkApi(token=token)

    vk = vk_session.get_api()
    vk.wall.post(message=text,
                 owner_id=-owner_id,
                 from_group=1,
                 attachments=f'photo{-owner_id}_{media_id}')


if __name__ == '__main__':
    env = Env()
    env.read_env()

    vk_token = env('VK_USER_TOKEN')

    test_message = 'hello world'
    owner_id = 203517016
    album_id = '280071703'
    photo = 'test_photo.jpg'
    from_group = 1  # 1 — запись будет опубликована от имени группы, 0 — запись будет опубликована от имени пользователя

    image_id = upload_image_alboum(vk_token, photo, album_id, owner_id)
    upload_post_to_wall(vk_token, test_message, owner_id, image_id)

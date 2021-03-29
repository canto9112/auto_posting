import vk_api


def upload_image_alboum(token, photo, album_id, owner_id, text):
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    upload = vk_api.VkUpload(vk_session)

    photo_img = upload.photo(photo,
                             album_id=album_id,
                             group_id=owner_id)
    image_id = photo_img[0]['id']

    vk.wall.post(message=text,
                 owner_id=-owner_id,
                 from_group=1, # 1 — запись будет опубликована от имени группы, 0 — запись будет опубликована от имени пользователя
                 attachments=f'photo{-owner_id}_{image_id}')


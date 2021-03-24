from environs import Env
import vk_api


def push_text_vk(token, text, owner_id):
    vk_session = vk_api.VkApi(token=token)

    vk = vk_session.get_api()
    vk.wall.post(message=text, owner_id=owner_id, from_group=1)


if __name__ == '__main__':
    env = Env()
    env.read_env()

    vk_token = env('VK_TOKEN')
    test_message = 'hello world'
    owner_id = '-203517016'
    from_group = 1  # 1 — запись будет опубликована от имени группы, 0 — запись будет опубликована от имени пользователя
    push_text_vk(vk_token, test_message, owner_id)
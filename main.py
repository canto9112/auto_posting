from environs import Env


if __name__ == '__main__':
    env = Env()
    env.read_env()

    vk_token = env('VK_TOKEN')
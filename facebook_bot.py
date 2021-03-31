import requests


def posting_post(token, text, group_id, image):
    url = f'https://graph.facebook.com/v10.0/{group_id}/photos'
    with open(image, "rb") as file:
        image_file = file.read()
    files = {'file': image_file}

    data = {
        "message": text,
        'access_token': token
    }
    response_post = requests.post(url, data=data, files=files)
    response_post.raise_for_status()


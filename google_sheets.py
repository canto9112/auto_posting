import gspread
import requests


def get_text_and_imagename(post_number, config_file, sheet_id):
  gc = gspread.service_account(filename=config_file)
  sh = gc.open_by_key(sheet_id)

  worksheet = sh.sheet1
  result3 = worksheet.row_values(post_number)
  text,  url_image = result3

  response = requests.get(url_image)
  image_name = f'pic{post_number}.jpg'

  with open(image_name, 'wb') as file:
    file.write(response.content)

  return text, image_name


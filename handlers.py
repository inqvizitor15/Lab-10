# Тут будут храниться обработчики каждой команды
import io
import requests
from voice import voice
from random import randint
from pathlib import Path
import os
import webbrowser
from PIL import Image
from io import BytesIO

# # from googletrans import Translator
# # from googletrans import text
# from googletrans import *
from deep_translator import GoogleTranslator

API_URL = 'https://rickandmortyapi.com/api'
ID = randint(1, 826)
DOWNLOADS_DIR = str(Path.home() / "Downloads")  # определние пути папки "Загрузки"


# Команда 1, "случайный" (сказать имя случайного персонажа)
def rand(id=ID, url=API_URL):
    response = requests.get(url + f'/character/{id}')
    if response.status_code == 200:

        data = response.json()
        name_eng = data['name']

        # translator = Translator()
        name_ru = GoogleTranslator(source="en", target="ru").translate(name_eng)

        voice.text_to_speech(name_ru)
        print(f'Имя слуйчаного персонажа: {name_eng, name_ru}')
    else:
        print(f"Ошибка: {response.status_code}")
        print(response.json())  # Вывод сообщения об ошибке


# Команда 2, "сохранить" (сохраняет картинку)
def save(id=ID, url=API_URL, dir_save=DOWNLOADS_DIR):
    response = requests.get(url + f'/character/avatar/{id}.jpeg')

    if response.status_code == 200:

        # Объявляем переменные
        filename = f"avatar{id}.jpeg"  # Можно изменить на .png и др.
        save_path = os.path.join(dir_save, filename)

        # Сохраняем изображение ('wb': w отвечает за запись в файл, а b - за бинарный режим,
        #                                необходимый для работы с изображениями)

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"Изображение сохранено в: {save_path}")


    else:
        print(f"Ошибка: {response.status_code}")
        print(response.json())


# Команда 3, "эпизод" (назвать эпизод первого появления)
def episode(id=ID, url=API_URL):
    response = requests.get(url + f'/character/{id}')

    if response.status_code == 200:
        data = response.json()
        episode_address = data['episode'][0]
        response_episode = requests.get(episode_address)

        if response_episode.status_code == 200:
            data_ep = response_episode.json()
            name_episode_eng = data_ep['name']

            name_episode_ru = GoogleTranslator(source="en", target="ru").translate(name_episode_eng)

            voice.text_to_speech(name_episode_ru)
            print(f'Название эпизода: {name_episode_eng, name_episode_ru}')

# Команда 4, "показать" (вывести картинку)
def show(id=ID, url=API_URL):
    webbrowser.open(url + f'/character/avatar/{id}.jpeg')

# Команда 5, "разрешение" (назвать разрешение в пикселях
def permission(id=ID, url=API_URL):
    image_url = f'{url}/character/avatar/{id}.jpeg'
    response = requests.get(image_url)
    print(f"ID: {id}, URL: {image_url}")
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        width, height = image.size  # возвращает (ширина, высота)
    else:
        print(f"Ошибка: {response.status_code}")
        return None
    result = f"Разрешение составляет {width} на {height} пикселей"
    print(result)

    voice.text_to_speech(result)



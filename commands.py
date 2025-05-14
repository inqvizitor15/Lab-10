from handlers import rand, save, episode, show, permission
from voice import voice
from random import randint
from pathlib import Path

# COMMANDS = [
#     {'id': 0, 'text' : 'спасибо', 'handler' : thanks},
#     {'id': 1, 'text': 'хочу отдохнуть', 'handler': relax}
#     # {'id': 2, 'text': '', 'handler': ''}
# ]

COMMANDS = [
    {'id': 0, 'text' : 'случайный', 'handler' : rand},
    {'id': 1, 'text': 'сохранить', 'handler': save},
    {'id': 2, 'text': 'эпизод', 'handler': episode},
    {'id': 3, 'text': 'показать', 'handler': show},
    {'id': 4, 'text': 'разрешение', 'handler': permission}
]

# COMMANDS = [
#     {'id': 0, 'text' : 'ноль', 'handler' : rand},
#     {'id': 1, 'text': 'два', 'handler': save},
#     {'id': 2, 'text': 'три', 'handler': episode},
#     {'id': 3, 'text': 'пять', 'handler': show},
#     {'id': 4, 'text': 'семь', 'handler': permission}
# ]

# Формируем базовые аргументы для функций
API_URL = 'https://rickandmortyapi.com/api'
ID = randint(1, 826)
DOWNLOADS_DIR = str(Path.home() / "Downloads") # определние пути папки "Загрузки"

ACTIVATION = 'купер'
class Command:

    def __init__(self, text):
        self.text = text
        self.map()

    # map: проходится по всем командам,
    # сравнивает произнесенный текст с командами
    # и выполняет соответствующую с помощью run
    def map(self):
        if self.text.startswith(ACTIVATION):
            self.text = self.text.replace(ACTIVATION, '').strip()
            for cmd in COMMANDS:
                if self.text.startswith(cmd['text']):
                    self.run(cmd)
                    return True
            else:
                voice.text_to_speech('Я не знаю такой команды')

    def run(self, cmd): #ф-я выполнение команды, использующая рез-т map
        handler = cmd['handler']
        # handler(self.text)
        if cmd['text'] == 'случайный':
            handler(id=ID, url=API_URL)
        elif cmd['text'] == 'сохранить':
            handler(id=ID, url=API_URL, dir_save=DOWNLOADS_DIR)
        elif cmd['text'] == 'эпизод':
            handler(id=ID, url=API_URL)
        elif cmd['text'] == 'показать':
            handler(id=ID, url=API_URL)
        elif cmd['text'] == 'разрешение':
            handler(id=ID, url=API_URL)
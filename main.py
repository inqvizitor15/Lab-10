# .\venv\Scripts\activate
# команда, по которой переключаемся на виртуальную среду

# Чтобы переключиться на другой интерпритатор, необходимо прописать
# deactivate
# а затем указать полный путь до другого интерпритатора
import time
from recognize import Recognizer
from voice import voice
from commands import Command

rec = Recognizer()
text_gen = rec.listen()
rec.stream.stop_stream()

voice.text_to_speech('Привет! Я голосовой ассистент')
time.sleep(3)

rec.stream.start_stream()

# rec = Recognizer()
# text_gen = rec.listen()
#
# voice.text_to_speech('Привет! Я голосовой ассистент')
for text in text_gen:
    print(text)

    rec.stream.stop_stream()
    Command(text)
    time.sleep(1)
    rec.stream.start_stream()
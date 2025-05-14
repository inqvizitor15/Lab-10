import json
import vosk
import pyaudio

class Recognizer:
    def __init__(self):
        model = vosk.Model('vosk-model-small-ru-0.22')
        self.rec = vosk.KaldiRecognizer(model, 16000)# подключаем модель к recognize.py
        self.start_stream()

    def start_stream(self):  # метод, считывающий звук с микрофона
        pa = pyaudio.PyAudio()
        self.stream = pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=8000
        )
    def listen(self): # метод, передающий звук, который считали в модель vosk, и возвращающий текст из звука
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if self.rec.AcceptWaveform(data) and len(data) > 0: # передаем считанные данные и проверяем, что они не пусты
                res = self.rec.Result()
                answer = json.loads(res)
                if answer['text']:
                    yield answer['text']

if __name__ == '__main__':
    rec = Recognizer()
    text_gen = rec.listen()
    for text in text_gen:
        print(text)
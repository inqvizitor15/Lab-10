from vosk_tts import Model, Synth
from playsound import playsound
import winsound

class Voice:
    def __init__(self):
        model = Model(model_name='vosk-model-tts-ru-0.7-multi')
        self.synth = Synth(model)
        self.voice = 3

    def text_to_speech(self, text='Добрый день!'):
        #text - текст, который он произнесёт
        # out.wav - сгенерированный звук

        voice_file = 'out.wav'

        self.synth.synth(text,
                         'out.wav',
                         speaker_id=self.voice)

        winsound.PlaySound(voice_file, winsound.SND_FILENAME | winsound.SND_ASYNC)

    def self_voice(self, voice):
        self.voice = voice

voice = Voice()

if __name__ == '__main__':
    voice = Voice()
    voice.text_to_speech()
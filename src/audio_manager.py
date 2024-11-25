import os
import pygame

class AudioManager:
    def __init__(self, audio_dir):
        self.audio_dir = audio_dir
        pygame.mixer.init()

    def play_audio(self, word):
        audio_file = os.path.join(self.audio_dir, f"{word}.mp3")
        if os.path.exists(audio_file):
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
        else:
            print(f"Audio for {word} not found!")


from pygame import mixer

class AudioPlayer:
    def __init__(self):
        mixer.init()
        mixer.music.load("temp_audio_file")
        self._is_started: bool = False

    def play(self):
        if not self.is_started:
            mixer.music.play()
        else:
            mixer.music.unpause()
        self.is_started = True

    def pause(self):
        mixer.music.pause()

    def stop(self):
        mixer.music.stop()
        self.is_started = False

    def exit(self):
        mixer.music.stop()
        self.is_started = False

    @property
    def is_started(self):
        return self._is_started

    @is_started.setter
    def is_started(self, value):
        self._is_started = value
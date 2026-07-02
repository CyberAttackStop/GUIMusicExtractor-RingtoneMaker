import vlc
import os


class MediaPlayer:

    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.current_file = None

    def load(self, file_path):
        if not os.path.exists(file_path):
            return False

        media = self.instance.media_new(file_path)
        self.player.set_media(media)
        self.current_file = file_path
        return True

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def is_playing(self):
        return self.player.is_playing()

    def get_length(self):
        return self.player.get_length()

    def get_time(self):
        return self.player.get_time()

    def set_volume(self, volume):
        self.player.audio_set_volume(volume)

    def get_volume(self):
        return self.player.audio_get_volume()

    def set_position(self, pos):
        self.player.set_position(pos)

    def get_position(self):
        return self.player.get_position()
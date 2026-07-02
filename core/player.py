import vlc


class MediaPlayer:

    def __init__(self):

        self.instance = vlc.Instance()

        self.player = self.instance.media_player_new()

        self.current_file = None

    def load(self, filepath):

        media = self.instance.media_new(filepath)

        self.player.set_media(media)

        self.current_file = filepath


    def play(self):

        if self.current_file:
            self.player.play()

    def pause(self):

        self.player.pause()

    def stop(self):

        self.player.stop()

    def set_volume(self, volume):

        self.player.audio_set_volume(int(volume))
    
    def get_time(self):
        """
        Current playback time in milliseconds.
        """
        return self.player.get_time()

    def get_length(self):
        """
        Total media duration in milliseconds.
        """
        return self.player.get_length()


    def get_position(self):
        """
        Playback position (0.0 to 1.0)
        """
        return self.player.get_position()


    def set_position(self, position):
        """
        Seek to a position (0.0 to 1.0)
        """
        self.player.set_position(position)

    def is_playing(self):
        return self.player.is_playing()

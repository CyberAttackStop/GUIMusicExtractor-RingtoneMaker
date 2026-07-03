import subprocess


class AudioConverter:

    @staticmethod
    def convert_to_wav(input_file, output_file):

        command = [
            "ffmpeg",
            "-y",
            "-i", input_file,
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "44100",
            "-ac", "2",
            output_file
        ]

        subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        return output_file
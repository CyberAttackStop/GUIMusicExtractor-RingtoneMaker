import subprocess
import os


class AudioExtractor:

    @staticmethod
    def extract(input_file, output_file):

        command = [
            "ffmpeg",
            "-y",
            "-i", input_file,
            "-vn",
            "-acodec", "libmp3lame",
            "-q:a", "2",
            output_file
        ]

        subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        return output_file
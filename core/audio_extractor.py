import subprocess
import re


class AudioExtractor:

    @staticmethod
    def extract(input_file, output_file, progress_callback=None):

        command = [
            "ffmpeg",
            "-y",
            "-i", input_file,
            "-vn",
            "-acodec", "libmp3lame",
            "-q:a", "2",
            "-progress", "-",
            "-nostats",
            output_file
        ]

        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            universal_newlines=True
        )

        duration = 0

        current = 0

        for line in process.stdout:

            line = line.strip()

            if line.startswith("duration="):

                duration = int(line.split("=")[1])

            elif line.startswith("out_time_ms="):

                current = int(line.split("=")[1])

                if duration > 0 and progress_callback:

                    progress = current / duration

                    progress_callback(progress)

        process.wait()

        if process.returncode != 0:

            raise Exception("FFmpeg failed.")
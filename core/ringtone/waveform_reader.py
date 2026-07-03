import subprocess
import numpy as np


class WaveformReader:

    @staticmethod
    def get_waveform(file_path, samples=1500):

        command = [
            "ffmpeg",
            "-i", file_path,
            "-vn",
            "-ac", "1",
            "-ar", "8000",
            "-f", "s16le",
            "-"
        ]

        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL
        )

        raw = process.stdout.read()

        process.wait()

        audio = np.frombuffer(raw, dtype=np.int16)

        if len(audio) == 0:
            return np.array([])

        # Downsample to fixed number of points
        indices = np.linspace(
            0,
            len(audio)-1,
            samples,
            dtype=int
        )

        waveform = audio[indices]

        return waveform
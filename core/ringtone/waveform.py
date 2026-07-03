import os
import wave

import matplotlib.pyplot as plt
import numpy as np


class WaveformGenerator:

    @staticmethod
    def generate(audio_file, output_image):

        with wave.open(audio_file, "rb") as wav:

            signal = np.frombuffer(
                wav.readframes(wav.getnframes()),
                dtype=np.int16
            )

        # Stereo → Mono
        if wav.getnchannels() == 2:
            signal = signal.reshape((-1, 2))
            signal = signal.mean(axis=1)

        plt.figure(figsize=(10, 2))

        plt.fill_between(
            range(len(signal)),
            signal,
            color="#1F6AA5"
        )

        plt.axis("off")

        plt.tight_layout()

        plt.savefig(
            output_image,
            dpi=150,
            bbox_inches="tight",
            pad_inches=0
        )

        plt.close()

        return output_image
import os
from audio_separator.separator import Separator


class UVREngine:

    @staticmethod
    def separate(input_file):

        output_folder = os.path.join(
            os.getcwd(),
            "output",
            "separated"
        )

        os.makedirs(output_folder, exist_ok=True)

        separator = Separator(
            output_dir=output_folder
        )

        # Load the default model
        separator.load_model()

        # Separate the audio
        separator.separate(input_file)

        return output_folder
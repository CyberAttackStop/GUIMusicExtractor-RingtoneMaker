import os
from audio_separator.separator import Separator
import logging


class SeparationLogHandler(logging.Handler):

    callback = None

    def emit(self, record):

        message = self.format(record)

        if SeparationLogHandler.callback:

            SeparationLogHandler.callback(message)


class UVREngine:

    @staticmethod
    def separate(input_file):

        output_folder = os.path.join(
            os.getcwd(),
            "output",
            "separated"
        )

        os.makedirs(output_folder, exist_ok=True)



        handler = SeparationLogHandler()

        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(message)s")
        )

        root = logging.getLogger()

        root.setLevel(logging.INFO)

        root.addHandler(handler)

        separator = Separator(
            output_dir=output_folder
        )

        # Load the default model
        separator.load_model()

        # Separate the audio
        separator.separate(input_file)

        root.removeHandler(handler)

        return output_folder
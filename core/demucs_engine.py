import subprocess
import sys
import os


class DemucsEngine:

    @staticmethod
    def separate(input_file):

        output_folder = "output"

        os.makedirs(output_folder, exist_ok=True)

        command = [
            sys.executable,          # <-- Uses the current venv Python
            "-m",
            "demucs",
            "--two-stems",
            "vocals",
            "-o",
            output_folder,
            input_file,
        ]

        process = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if process.returncode != 0:
            raise Exception(process.stderr)

        return process.stdout
import os


class PathManager:

    BASE_DIR = os.getcwd()

    OUTPUT_DIR = os.path.join(BASE_DIR, "output")

    TEMP_DIR = os.path.join(BASE_DIR, "temp")

    @staticmethod
    def create_folders():

        os.makedirs(PathManager.OUTPUT_DIR, exist_ok=True)

        os.makedirs(PathManager.TEMP_DIR, exist_ok=True)
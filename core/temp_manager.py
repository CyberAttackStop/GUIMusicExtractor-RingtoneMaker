import os
import time

from core.path_manager import PathManager


class TempManager:

    @staticmethod
    def clean(days=1):

        now = time.time()

        for file in os.listdir(PathManager.TEMP_DIR):

            path = os.path.join(
                PathManager.TEMP_DIR,
                file
            )

            if os.path.isfile(path):

                age = now - os.path.getmtime(path)

                if age > days * 86400:

                    try:
                        os.remove(path)

                    except Exception:
                        pass
import os


class FileManager:

    @staticmethod
    def get_file_info(file_path):

        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        size_mb = round(file_size / (1024 * 1024), 2)

        extension = os.path.splitext(file_name)[1].upper()

        return {
            "name": file_name,
            "path": file_path,
            "size": f"{size_mb} MB",
            "type": extension
        }
import cv2
import os
from PIL import Image


class ThumbnailEngine:

    @staticmethod
    def create_thumbnail(video_path):

        temp_folder = "temp"

        os.makedirs(temp_folder, exist_ok=True)

        output = os.path.join(temp_folder, "thumbnail.jpg")

        cap = cv2.VideoCapture(video_path)

        success, frame = cap.read()

        if success:
            cv2.imwrite(output, frame)

        cap.release()

        return output

    @staticmethod
    def load_thumbnail(image_path, size=(320, 180)):

        image = Image.open(image_path)

        image.thumbnail(size)

        return image
import subprocess
import json
import os


class FFmpegEngine:

    # Update this if your FFprobe is installed somewhere else
    FFPROBE_PATH = r"C:\ffmpeg\bin\ffprobe.exe"

    @classmethod
    def get_media_info(cls, file_path):
        """
        Returns media metadata using FFprobe.
        """

        command = [
            cls.FFPROBE_PATH,
            "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            file_path
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr)

        data = json.loads(result.stdout)

        return cls.parse_metadata(data, file_path)

    @staticmethod
    def parse_metadata(data, file_path):

        info = {
            "name": os.path.basename(file_path),
            "path": file_path,
            "size": round(os.path.getsize(file_path) / (1024 * 1024), 2),
            "duration": "--",
            "video_codec": "--",
            "audio_codec": "--",
            "resolution": "--",
            "fps": "--",
            "bitrate": "--",
            "sample_rate": "--",
            "channels": "--"
        }

        # Format information
        fmt = data.get("format", {})

        duration = fmt.get("duration")
        if duration:
            duration = float(duration)
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            info["duration"] = f"{minutes:02}:{seconds:02}"

        bitrate = fmt.get("bit_rate")
        if bitrate:
            info["bitrate"] = f"{round(int(bitrate)/1000)} kbps"

        # Stream information
        for stream in data.get("streams", []):

            if stream.get("codec_type") == "video":

                info["video_codec"] = stream.get("codec_name", "--")

                width = stream.get("width")
                height = stream.get("height")

                if width and height:
                    info["resolution"] = f"{width} × {height}"

                fps = stream.get("avg_frame_rate", "0/0")

                if fps != "0/0":
                    num, den = fps.split("/")
                    if int(den) != 0:
                        info["fps"] = f"{round(int(num)/int(den),2)}"

            elif stream.get("codec_type") == "audio":

                info["audio_codec"] = stream.get("codec_name", "--")

                sr = stream.get("sample_rate")
                if sr:
                    info["sample_rate"] = f"{sr} Hz"

                ch = stream.get("channels")
                if ch:
                    info["channels"] = str(ch)

        return info
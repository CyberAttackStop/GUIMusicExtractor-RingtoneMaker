# 🎵 GUI Music Extractor & Ringtone Maker

> A professional multimedia desktop application built with **Python** and **CustomTkinter** for media playback, audio extraction, AI-powered music separation, and waveform-based ringtone creation.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-success)
![GUI](https://img.shields.io/badge/GUI-CustomTkinter-green)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Enabled-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📖 Overview

GUI Music Extractor & Ringtone Maker is a feature-rich desktop application that combines multimedia playback, audio processing, AI-powered music source separation, and ringtone editing into a single intuitive interface.

Whether you want to extract audio from videos, separate vocals from instrumentals, preview media, or create custom ringtones using an interactive waveform editor, this application provides a modern and efficient workflow.

---

# ✨ Features

## 🎬 Media Player

- Play Video Files
- Play Audio Files
- Play / Pause / Stop Controls
- Seek Bar
- Volume Control
- Media Position Tracking

---

## 🎵 Audio Processing

- Extract Audio from Videos
- MP3 Export
- WAV Export
- Audio Conversion
- Metadata Reading

---

## 🤖 AI Music Separation

- Vocal Separation
- Instrumental Separation
- Powered by Ultimate Vocal Remover (UVR)
- Demucs AI Integration

---

## ✂️ Professional Ringtone Studio

- Interactive Waveform
- Draggable Start Marker
- Draggable End Marker
- Live Time Display
- Preview Selected Region
- Export Selected Audio
- MP3/WAV Ringtone Support

---

## 🖼 Media Utilities

- Thumbnail Generator
- Media Information
- Duration Detection
- Resolution Detection
- Bitrate Information
- Codec Detection

---

## ⚡ User Experience

- Modern CustomTkinter Interface
- Background Processing
- Progress Dialogs
- Responsive UI
- Automatic Temporary File Management

---

# 🖥 Screenshots

> Screenshots will be added in future releases.

```
Main Window

Media Player

AI Music Separation

Professional Ringtone Studio

Waveform Editor

Media Information
```

---

# 🏗 Project Structure

```text
GUIMusicExtractor-RingtoneMaker
│
├── app.py
├── gui/
│   ├── main_window.py
│   ├── ringtone_editor.py
│   ├── progress_dialog.py
│   └── ...
│
├── core/
│   ├── ffmpeg_engine.py
│   ├── player.py
│   ├── thumbnail_generator.py
│   ├── waveform_reader.py
│   ├── path_manager.py
│   ├── ringtone/
│   ├── uvr/
│   └── ...
│
├── assets/
├── temp/
├── output/
├── requirements.txt
└── README.md
```

---

# 🛠 Technologies Used

## Desktop GUI

- CustomTkinter
- Tkinter

---

## Programming Language

- Python 3.11+

---

## Audio & Video Processing

- FFmpeg
- FFprobe
- Pydub
- VLC (python-vlc)
- NumPy

---

## Artificial Intelligence

- Ultimate Vocal Remover (UVR)
- Demucs

---

## Image Processing

- Pillow (PIL)

---

## Utilities

- Threading
- JSON
- OS
- Pathlib
- Datetime
- Subprocess

---

## Version Control

- Git
- GitHub

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/CyberAttackStop/GUIMusicExtractor-RingtoneMaker.git
```

```bash
cd GUIMusicExtractor-RingtoneMaker
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install FFmpeg

Download FFmpeg and ensure both **ffmpeg.exe** and **ffprobe.exe** are available in your system PATH or update the paths inside the project.

---

## Install VLC

Install **VLC Media Player** before running the application.

---

## Run Application

```bash
python app.py
```

---

# 📦 Requirements

- Python 3.11+
- FFmpeg
- FFprobe
- VLC Media Player
- CustomTkinter
- NumPy
- Pillow
- Pydub
- python-vlc
- Torch
- Demucs
- Ultimate Vocal Remover

---

# 📈 Roadmap

## Completed

- ✅ Modern GUI
- ✅ Media Player
- ✅ Audio Player
- ✅ Video Playback
- ✅ Audio Extraction
- ✅ Thumbnail Generator
- ✅ Media Information Panel
- ✅ Volume Control
- ✅ Progress Dialog
- ✅ Background Processing
- ✅ AI Vocal Separation
- ✅ AI Instrument Separation
- ✅ Interactive Waveform
- ✅ Ringtone Studio
- ✅ Live Preview
- ✅ Export MP3/WAV

---

## Planned

- ⏳ Batch Processing
- ⏳ Drag & Drop Support
- ⏳ Playlist Manager
- ⏳ Audio Effects
- ⏳ Fade In / Fade Out
- ⏳ Theme Manager
- ⏳ Keyboard Shortcuts
- ⏳ Dark / Light Themes
- ⏳ Windows Installer (.exe)
- ⏳ Auto Update

---

# 🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Developer

**Bijoy Biju**

GitHub: https://github.com/CyberAttackStop

---

## ⭐ If you like this project

Please consider giving the repository a **Star ⭐** to support future development.
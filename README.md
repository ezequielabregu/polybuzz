# Polybuzz

## Overview

`Polybuzz` is a free speech-to-text tool that can help you transcribe notes, documents, books, reports, or blog posts simply by using your voice.

People from all over the world, including students, teachers, writers, and bloggers, use this app on a daily basis. By using this app, you can significantly reduce the amount of effort you put into writing.

`Polybuzz` is particularly helpful for individuals who have difficulty using their hands due to trauma, dyslexia, or other disabilities that limit the use of traditional input devices.

## Translation method

`Polybuzz` uses automatic speech recognition (ASR) system trained on 680,000 hours of multilingual and multitask supervised data collected from the web. We show that the use of such a large and diverse dataset leads to improved robustness to accents, background noise and technical language. Moreover, it enables transcription in multiple languages, as well as translation from those languages into English.

**Reference link:**

[Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/pdf/2212.04356.pdf)

&nbsp;

## Online demo
[https://polybuzz.ezequielabregu.com/](https://polybuzz.ezequielabregu.com/)

&nbsp;
![polybuzz](/static/polybuzz-demo.png)
![result](/static/result.png)

## Features

- Multi-language recognition
- Built-in speech recorder & player
- Audio file uploader
- Speech to text converter
- Accurate punctuation
- Download output text
- Compatible with desktop (Windows, Mac, Linux) and mobile (Android, IOS) web browsers
  
## How to run

```bash
mkdir polybuzz
git clone https://github.com/ezequielabregu/polybuzz.git
cd polybuzz
pip install -r requirements.txt
python app.py
```

Web browser address:\
[127.0.0.1:5000](http://127.0.0.1:5000/)

Requires the command-line tool ffmpeg to be installed on your system, which is available from most package managers:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

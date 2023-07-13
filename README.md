# ePub to MP3 Converter

This script converts an ePub file into an MP3 audiobook using macOS's built-in `say` command for text-to-speech synthesis and `ffmpeg` to convert AIFF files to MP3. The MP3 files are saved in a directory named after the ePub file, in the same directory where you run the script.

## Requirements

- macOS
- Python 3.6 or higher
- `ffmpeg` installed and available in the system's PATH

## Python Dependencies

The Python dependencies are listed in the `requirements.txt` file and can be installed with:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python epub2mp3.py <epub_file>
```

Replace `<epub_file>` with the name of your ePub file. Each chapter will be output as a separate MP3 file.

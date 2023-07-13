import os
import sys
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import subprocess
import time

# Function to extract text from epub file
def epub_to_text(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = item.get_content().decode('utf-8')
            soup = BeautifulSoup(content, features="html.parser")
            chapters.append(soup.get_text())
    return chapters

# Function to convert text to speech
def text_to_speech(text, epub_name, chapter_num, output_dir):
    chunk_file = os.path.join(output_dir, f"{epub_name}_{chapter_num}.aiff")
    subprocess.call(['say', text, '-o', chunk_file])
    # Convert aiff to mp3
    subprocess.call(['ffmpeg', '-i', chunk_file, os.path.join(output_dir, f"{epub_name}_{chapter_num}.mp3")])
    # Remove the aiff file
    os.remove(chunk_file)
    # Pause to allow 'say' command to process the text
    time.sleep(2)

# Check if user provided an epub file path
if len(sys.argv) != 2:
    print("Usage: python epub2mp3.py <epub_file>")
    sys.exit(1)

# Input epub file path from command line
epub_file = sys.argv[1]
epub_name = os.path.splitext(os.path.basename(epub_file))[0]
output_dir = os.path.join(os.getcwd(), epub_name)

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Extract text from epub file
text_chapters = epub_to_text(epub_file)
print(f"Extracted {len(text_chapters)} chapters")

# Convert text to speech
# This may take some time if the text is large
for idx, chapter in enumerate(text_chapters):
    print(f"Converting chapter {idx + 1}")
    text_to_speech(chapter, epub_name, idx + 1, output_dir)
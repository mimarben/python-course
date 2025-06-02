import PyPDF2
from gtts import gTTS
import os

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def text_to_speech(text, output_filename="audiobook.mp3"):
    tts = gTTS(text)
    tts.save(output_filename)
    print(f"Audio saved as {output_filename}")

def main():
    pdf_path = "sample.pdf"  # Replace with your PDF file path
    print("Extracting text from PDF...")
    text = pdf_to_text(pdf_path)

    if text.strip():
        print("Converting text to speech...")
        text_to_speech(text)
    else:
        print("No text found in PDF.")

if __name__ == "__main__":
    main()

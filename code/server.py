from flask import Flask, request, jsonify
from flask_cors import CORS
import audiotranscribe as at
import argparse
import numpy as np
import os
import speech_recognition as sr
import whisper
from moviepy.editor import VideoFileClip

from queue import Queue
from time import sleep


app = Flask(__name__)
CORS(app)

whisper_model = whisper.load_model("turbo")

print("model loaded")
@app.route("/transcribe", methods = ["POST"])
def transcribe():
    if 'videoFile' not in request.files:
        return "No video file part"
    
    file = request.files['videoFile']

    if file.filename == '':
        return "No selected file"
    
    if file:
        # Save the uploaded file to a temporary location
        temp_video_path = os.path.join("temp_videos", file.filename)
        file.save(temp_video_path)
        
        try:
            # Load the video using the file path
            video_clip = VideoFileClip(temp_video_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile("code\webapp\extracted_audio.wav")

            # Close the video and audio clips
            audio_clip.close()
            video_clip.close()

            result = whisper_model.transcribe("code\webapp\extracted_audio.wav")
            print(result["text"])

            print("Audio extraction and transcription successful!")

            words = result["text"].split(" ")
            

        finally:
            # Clean up: Remove the temporary video file
            os.remove(temp_video_path)


if __name__ == '__main__':
    os.makedirs("temp_videos", exist_ok=True)  # Ensure the temp directory exists
    app.run(host='0.0.0.0', port=5000, debug=True)
# # word_slow.py
# import time
# import sys

# phrase = "Pal ek pal mein hi tham sa gaya Tu haath mein haath jo de gaya Chalun main jahaan jaaye tu Daayein main tere, baayein tu Hoon rut main, hawayein tu Saathiya…"
# delay_between_words = 0.2  # seconds - increase for slower

# for word in phrase.split():
#     sys.stdout.write(word)
#     sys.stdout.flush()
#     time.sleep(delay_between_words)
#     # print a space after pause (gives a small "jump" effect)
#     sys.stdout.write(" ")
#     sys.stdout.flush()

# print()  # newline at end

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Backend!"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Folders for saving files
AUDIO_FOLDER = "uploads/audio"
VIDEO_FOLDER = "uploads/video"

app.config["AUDIO_FOLDER"] = AUDIO_FOLDER
app.config["VIDEO_FOLDER"] = VIDEO_FOLDER

# Create folders if they don't exist
os.makedirs(AUDIO_FOLDER, exist_ok=True)
os.makedirs(VIDEO_FOLDER, exist_ok=True)

@app.route("/podcast/upload", methods=["POST"])
def upload_podcast():
    audio = request.files.get("audio")
    video = request.files.get("video")

    if not audio and not video:
        return jsonify({"error": "No file uploaded"}), 400

    response = {}

    if audio:
        audio_filename = secure_filename(audio.filename)
        audio.save(os.path.join(AUDIO_FOLDER, audio_filename))
        response["audio"] = f"Audio uploaded: {audio_filename}"

    if video:
        video_filename = secure_filename(video.filename)
        video.save(os.path.join(VIDEO_FOLDER, video_filename))
        response["video"] = f"Video uploaded: {video_filename}"

    return jsonify(response), 200


@app.route("/podcast", methods=["GET"])
def get_podcast_info():
    return jsonify({
        "message": "Podcast route working!",
        "features": ["Audio upload", "Video upload"]
    })

if __name__ == "__main__":
    app.run(debug=True)

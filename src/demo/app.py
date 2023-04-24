from flask import Flask, render_template, request, jsonify
import os
import wave
import io
import time
import tempfile

app = Flask(__name__)
counter = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_audio', methods=['POST'])
def handle_send_audio():
    global counter
    buffer = io.BytesIO()

    data = request.data
    counter += len(data)
    buffer.write(data)

    # create tempfile with wav extension
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, "output.wav")
        print("Saving audio to", filename)
        save_audio(buffer, filename)
        print("Transcribing audio ...")
        transcript = transcribe(filename)
        
    return dict(counter=counter, filename="foo", transcript=transcript)

def transcribe(filename):
    # global transcript
    print(f'Processing {filename}...')
    import requests
    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = { "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY") }
    payload = {"model": "whisper-1"}
    files = { "file": ("output.wav", open(filename, 'rb'), 'application/octet-stream') }
    response = requests.post(url, headers=headers, data=payload, files=files)
    transcript = response.json()['text']
    print(f'Transcript: {transcript}')
    return transcript

def save_audio(buffer, filename):
    buffer.seek(0)
    # get folder of currnet python file
    folder = os.path.dirname(os.path.abspath(__file__))
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # Assuming 16-bit audio
        wf.setframerate(44100)  # Assuming 16,000 samples per second
        wf.writeframes(buffer.read())

    print(f'Audio saved to {filename}!')

if __name__ == '__main__':
    app.run(debug=True)
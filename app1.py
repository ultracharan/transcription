import streamlit as st
import speech_recognition as sr
import threading
import requests
import base64

# Set up Streamlit app
st.title("Real-Time Transcription")

# Hugging Face API details
api_url = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"
api_token = st.secrets["api_tokan"]

# Variable to store the transcription
transcription = ""

# Function to continuously record audio in the background
def record_audio():
    global transcription

    # Set up the speech recognizer
    r = sr.Recognizer()

    # Start recording audio from the microphone
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source)
            try:
                # Convert audio data to a base64-encoded string
                audio_base64 = base64.b64encode(audio.get_wav_data()).decode("utf-8")

                # Create the request payload
                data = {
                    "inputs": audio_base64,
                    "options": {"task": "automatic_speech_recognition"},
                }

                # Make a request to the Hugging Face API
                headers = {
                    "Authorization":  f"Bearer {api_token}",
                    "Content-Type": "application/json",
                }
                response = requests.post(api_url, headers=headers, json=data)

                # Check if the request was successful
                if response.status_code == 200:
                    transcription = response.json()["text"]
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                pass

# Start the background thread for recording audio
audio_thread = threading.Thread(target=record_audio)
audio_thread.daemon = True
audio_thread.start()

# Continuously display the transcription
if st.button("Start"):
    while True:
        if transcription:
        
            st.write(transcription)
            transcription = ""


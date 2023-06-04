# Real-Time Transcription

This is a Python script that utilizes Streamlit and SpeechRecognition libraries to perform real-time audio transcription. The script captures audio from the microphone and leverages the Hugging Face API to convert speech into text.

## Features

- Real-time transcription of audio input from the microphone.
- Integration with the Hugging Face API for speech-to-text conversion.
- Streamlit app interface for easy interaction.

## Prerequisites

- Python 3.7 or higher installed on your machine.
- Required Python packages: streamlit, speech_recognition, requests.
- Access to a working microphone.

## Setup and Usage

1. Clone or download the repository containing the script.

2. Install the required Python packages by running the following command:
  
       pip install -r requirements.txt

3. Obtain an API token from Hugging Face by signing up at their website (https://huggingface.co/). Once you have the token, set it as the value for the `api_token` variable in the code.

4. Run the script using the following command:

    streamlit run app.py

5. Once the Streamlit app launches in your browser, click the "Start" button to initiate the real-time transcription.

6. Begin speaking into the microphone, and the script will transcribe your speech in real-time, displaying the text on the web page.

7. To stop the transcription, simply click the "Stop" button.

## Known Limitations

- The accuracy of the transcription may vary based on factors such as audio quality and background noise.
- The script relies on the availability and reliability of the Hugging Face API for speech-to-text conversion.
- Ensure that your microphone is in good working condition and accessible by the script.
- Note that the Hugging Face API may have rate limits and usage restrictions. Refer to their documentation for further details.

## message 
The script relies on the availability and reliability of the Hugging Face API for speech-to-text conversion , so might be slow or less accurate 

 - u can use "https://github.com/ultracharan/Real-time-transcription.git" this script as it uses Google Speech Recognition API to convert speech into text. The transcribed text is displayed on the Streamlit app interface.


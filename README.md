# PythonTTSASTTDT

# PythonTTSASTTDT

A simple Python project that provides the following features:
- **Speech to Text**: Convert spoken words to text and save them to a file.
- **Text to Speech**: Convert written text to spoken audio.
- **Dictionary Lookup**: Find meanings of words using a multi-language dictionary.
- **Language Translation**: Translate text between different languages.

## Features

### 1. Speech to Text
- Uses your microphone to record speech and converts it to text.
- Saves the recognized text to `output.txt`.
- Provides audio feedback after recording.

**Run:**  
```sh
**requirements :**
pip install pyttsx3 speechrecognition PyMultiDictionary googletrans

Files
speech_to_text.py: Speech to text functionality.
text_to_speech.py: Text to speech functionality.
dictionary.py: Dictionary lookup.
translation.py: Language translation.
output.txt: Stores recognized speech text.
Notes
For speech recognition, a working microphone is required.
Internet connection is needed for translation and dictionary features

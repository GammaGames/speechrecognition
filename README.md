# speechrecognition
A script that tries its best to use the speech recognition module to transcript a text file.  
I made this because the speech_recognition module's recognize_google function doesn't like clips longer than ~30s


Usage
---
Requires pydub and speech_recognition, to install them use:

```
pip3 install pydub
pip3 install SpeechRecognition
```

To run the script use 
```
python3 sr.py <file> <length>*
```
The length param is optional and in seconds

The script will create a folder based on the file's name in the current working directory (normally the script's location) and save the split text into the folder. The text will be labeled with each text file for the corrosponding text.

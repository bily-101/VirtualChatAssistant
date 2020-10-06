# How to make a Virtual Chat Assistant In python

 Install packages


* sudo apt-get install portaudio19-dev python-pyaudio
* pip install pyaudio
* pip install SpeechRecognition 
* pip install gTTS
* pip install wikipedia


Import Librarys

```python
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
```

Put in function recording

```
def recording():    
    r = sr.Recognizer()
    with sr.Microphone() as source:  
       print('Say something!')
       audio = r.listen(source)
        data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand')
    except sr.RequestError as e:
        print('Request error from Google Speech Recognition')
     
    return data



```

Function for response

```
def response(text):
    print(text)
    myobj = gTTS(text=text, lang='en', slow=False)
    
    myobj.save('assistant_response.mp3')

    os.system('start assistant_response.mp3')
```

Function to awaken the computer or test for a response
```
def wakeWord(text):
    WAKE_WORDS = ['hey computer', 'okay computer'] 
    text = text.lower()  # Convert the text to all lower case words
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    return False
```

Function for greeting

```
def greeting(text):
    # Greeting Inputs
    GREETING_INPUTS = ['yo', 'hey', 'hola', 'greetings', 'wassup', 'hello']
    GREETING_RESPONSES = ['Hi', 'How can I help you', 'hello', 'hey there']
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'
    return ''
```

Function for knowing your name

```
def getName(text):
 wordList = text.split()# Split the text into a list of words     
 for i in range(0, len(wordList)):
   if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and             wordList[i + 1].lower() == 'is':
    return wordList[i + 2] + ' ' + wordList[i + 3]
```


Putting all functions together for the main

```
while True:
    text = record()
    response = '' 
    if (wakeWord(text) == True):
        if ('who is' in text):
            person = getName(text)
            wiki = wikipedia.summary(person, sentences=2)            
            response = response + ' ' + wiki
       
       response(response)
      ```


Then Run using 
python file
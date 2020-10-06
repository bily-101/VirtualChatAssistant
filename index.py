import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia


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

def response(text):
    print(text)
    myobj = gTTS(text=text, lang='en', slow=False)
    
    myobj.save('assistant_response.mp3')

    os.system('start assistant_response.mp3')

def greeting(text):
    # Greeting Inputs
    GREETING_INPUTS = ['yo', 'hey', 'hola', 'greetings', 'wassup', 'hello']
    GREETING_RESPONSES = ['Hi', 'How can I help you', 'hello', 'hey there']
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'
    return ''

   
def getName(text):
    wordList = text.split()# Split the text into a list of words     
    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and             wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]

    
while True:
    text = recording()
    response = '' 
    if (wakeWord(text) == True):
        if ('who is' in text):
            person = getName(text)
            wiki = wikipedia.summary(person, sentences=2)            
            response = response + ' ' + wiki
       
    response(response)
      
import speech_recognition as sr

def get_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print(response)
        audio = r.listen(source, timeout = None)

        try:
            text = r.recognize_google(audio)
            print('User input:' + text)
            return text
        except:
            return 'Sorry, could not recognize your voice'
            
if __name__ == "__main__":
    print(get_voice())
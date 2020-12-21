import speech_recognition as sr
import os
import cv2
import numpy as np

def speach_to_text():
    # convert speach to text function
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print('تحدث من فضلك!')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    word = r.recognize_google(audio , language='ar-AR')
    return word

def display_video(path,word):
    # display video function
    cap = cv2.VideoCapture(path+word+'.mp4')
    if (cap.isOpened() == False):
        print("Error opening video  file")
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

path = 'The video folder path '
dirs = os.listdir(path)
files_name=[x.split('.')[0] for x in dirs]
word = speach_to_text()
if word in files_name:
    display_video(path,word)
else:
    print(word)



import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import tkinter as tk                                    
from tkinter import *
from tkinter import scrolledtext                        #for scrolling the conversation
import threading                                        #to avoid freezing




engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
rate= engine.getProperty("rate")
engine.setProperty("rate",rate-50)
r=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        output_text.insert(tk.END,f"clearing background noises..\n")
        r.adjust_for_ambient_noise(source)
        output_text.insert(tk.END,f"Ask me anything..\n")
        engine.say("Ask me anything...")
        engine.runAndWait()
        audio=r.listen(source)

    command=""
    try:
        command=r.recognize_google(audio,language='en-in').lower()
        output_text.insert(tk.END,f"{command}\n")
                                                                #error handling
    except sr.UnknownValueError:
        output_text.insert(tk.END,f"sorry, could not understand the audio")
        engine.say("sorry, could not understand the audio")
        engine.runAndWait()
    except sr.RequestError:
            output_text.insert(tk.END,f"sorry,I can not perform this task right now")
            engine.say("sorry,I can not perfoem this task right now")
            engine.runAndWait()
    except Exception as ex:
        output_text.insert(tk.END,f"An unexpected error occured{ex}")
        engine.say(ex)
        engine.runAndWait()

    if 'chrome' in command:
        output_text.insert(tk.END,"chrome")
        engine.say("opening chrome")
        engine.runAndWait()
        webbrowser.open("https://www.google.com/")     

    elif "time" in command:
        current_time=datetime.now().strftime("%I:%M:%p")
        a="Current time is:",current_time
        output_text.insert(tk.END,f"{a}")
        engine.say(a)
        engine.runAndWait()

    elif "date" in command:
        today_date=datetime.now().strftime("%B:%d:%Y")
        a="Toaday's date is:",today_date
        output_text.insert(tk.END,f"{a}")
        engine.say(a)
        engine.runAndWait()

    elif "your name" in command:
        output_text.insert(tk.END,f"I am helix and i am created to manage your daily task on just your voice command")    
        engine.say("I am helix and i am created to manage your daily task on just your voice command")
        engine.runAndWait()

    elif "hi" in command:
        output_text.insert(tk.END,f"hey,there")  
        engine.say("hey,there")
        engine.runAndWait()
    elif "youtube" in command:
        output_text.insert(tk.END,f"sure,opening youtube..")   #tk.END is used to append the text at last
        engine.say("sure,opening youtube..")  
        engine.runAndWait()
        webbrowser.open("https://www.youtube.com/")   
        
    elif "bye" in command:
        output_text.insert(tk.END,f"it was nice assisting you, take care...")
        engine.say("it was nice assisting you, take care...")    
        engine.runAndWait()
        exit()
        
def taking_cmd():                                  
    threading.Thread(target=cmd).start()              #IT WILL STOP GUI FROM FREEZING AND HELPS IN CONTINOUS CONVERSATION WITH USERS

root=tk.Tk()    

root.title("Voice Recognition app")
frame=Frame(root,bg="GREY")
frame.pack(pady=20)
Button(root,text="speak",font="Tahoma 19 bold",borderwidth=9,fg="GREEN",command=taking_cmd).pack()

output_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD,fg="RED", width=50, height=10)
output_text.pack(pady=10)
root.mainloop()                                  #wrap=tk.word helps by wrapping the words from one line to another unless user needs to  scroll horizontly to read long lines.
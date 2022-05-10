
#Example tkinter file if we go down that route

"""
from tkinter import *
from PIL import Image, ImageTk
from itertools import count, cycle
import datetime
di = dict()
list = list()
date = datetime.date.today()

def popup_window():
    window = Toplevel()
    window.attributes('-fullscreen',True)
    label9 = Label(window, text="Type the password below then hit add",font=15)
    label9.pack(fill='x', padx=50, pady=5)

    password_text = Entry(window,font=("Garamond",15),width=40)
    password_text.pack()
    password_button = Button(window,text='Add',command=lambda:storefunc(password_text.get()))
    password_button.pack()

    button_close = Button(window, text="Close", command=window.destroy)
    button_close.pack()

def nopass():
    return f"There are no passwords stored"

def delete():
    return f"Deleted all passwords from memory"

def update_response():
    return f'Stored to computer'

def storefunc(password_text):
    list.append(password_text)
    text22['text'] = list12()
    
def elseonly():
    return "Not a valid command\n(Only accepted commands: access passwords, and store to computer)"

def button1(textentry):
        if textentry.lower() == "access passwords":
            if list[::] == 0:
                text22['text'] = nopass()
            else:
                store1 = list
                text22['text'] = format_response(store1)
        elif textentry.lower() == "store to computer":
            file = open("/Users/daxpatel/Desktop/Tkinter GUI Password/saved.txt",'a')
            di['store'] = list
            for key,value in di.items():
                opaque = value
            string = f"Stored passwords from {date}\n {opaque} \n"
            file.write(string)
            file.close()
            text22['text'] = update_response()
        elif textentry.lower() == "delete passwords":
            list.clear()
            text22['text'] = delete()
        else:
            text22['text']= elseonly()


def format_response1(store2):
    return store2
def format_response(store1):
    return store1
def list12():
    return f"New Passwords Successfully Stored"

window = Tk()

window.attributes('-fullscreen', True)
window.title("Voyager Password Tool")

backgroundimage = Canvas(window, bg = 'purple')
backgroundimage.place(relwidth=1,relheight=1)

#frame to nest answers
frame = Frame(window)
frame.place(relx=0.004, rely=0.12,relwidth=0.992, relheight=0.9)

#Label for output
text22 = Label(frame, bg='white', fg='black', font=('Garamond',20),anchor='nw',justify='left')
text22.place(relx=0.004,rely=0.12,relheight=.9,relwidth=.992)

#Top Bar Commands
textentry = Entry(window,width=50,font=("Garamond",14))
textentry.place(relx=.335, rely=.04, relheight=.042)
# Top Bar Execution Button
button = Button(window, text="Go", font=40,bg='#1b63e2', command=lambda: button1(textentry.get()))
button.place(relx=0.665, rely=0.04, relheight=.042)

#popup window button
button3 = Button(frame, text="Add New Password", font=40,bg='white', command=popup_window())
button3.place(relx=0.445, rely=0.045, relheight=.042)

#voyager logo label
logo_label = Label(window,text='Voyager',bg='white',fg='purple', font=('Aquire',40))
logo_label.place(relwidth=.17,relheight=.17,relx=.004,rely=.880)

window.mainloop()




"""
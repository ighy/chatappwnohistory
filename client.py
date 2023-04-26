import socket
import atexit
import threading
from tkinter import*
win = Tk()
win.title('Client')
win.geometry('500x500')

entry1 = Entry(win)
entry1.place(x=100,y=350)

label1 = Label(win,text='Client: ').place(x=100,y=50)
def clientsendMsg():
    clientMess = entry1.get()
    s.send(clientMess.encode())
    entry1.delete(0,END)

button1 = Button(win,text='Send',command=clientsendMsg)
button1.pack(side=BOTTOM, fill=BOTH)






host = 'localhost'
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print('Connected')
displayLabel = Label(win,text='',fg='white')
displayLabel.pack(side=TOP, fill=X)
def receiveMsg():
    while True:
        data1 = s.recv(1024)
        print(data1.decode())
        
        displayLabel.config(text=data1)
        win.update()


    def handle_exit():
        print('This runs after keyboard int.')
        s.close()

    atexit.register(handle_exit)

t2 = threading.Thread(target=receiveMsg)
t2.start()

win.mainloop()

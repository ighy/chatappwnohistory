import socket
from tkinter import*
import threading
win = Tk()
win.title('server')
win.geometry('500x500')

e1 = Entry(win)
e1.place(x=100,y=350)

l1 = Label(win,text='Server: ').place(x=100,y=50)
def sendMsg():
    entrydata = e1.get()
    conn.send(entrydata.encode())
    e1.delete(0,END)
b1 = Button(win,text='Send',command=sendMsg)
b1.pack(side=BOTTOM ,fill=BOTH)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = ''
port = 12345

s.bind((host,port))

s.listen(5)
print('Listening')
y1 = 100
conn, addr = s.accept()
print('Got a connection from: ', addr)
displayMsg = Label(win,text='',fg='white')
displayMsg.pack(side=TOP, fill=X)


def recvMsg():
    while True:
        data = conn.recv(1024)
        print(addr, ':', data.decode())
        
        displayMsg.config(text=data)
        win.update()

t1 = threading.Thread(target=recvMsg)
t1.start()
win.mainloop()
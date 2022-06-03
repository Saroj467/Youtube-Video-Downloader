from tkinter import *           #Standard GUI Library 
from pytube import YouTube       #Python library which is used for downloading videos from the web

root=Tk()  #Create an instance of Tk class It also creates a toplevel window, known
           # as the root window, which serves as the main window of the application.
root.geometry('500x300')    # used to set the window’s width and height
root.resizable(0,0)         #set the fix size of window
root.title("YouTube Video Downloader")    #Use to give the title of window

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

link=StringVar()
Label(root,text='Paste Link Here:',font='arial 15 bold').place(x=160,y=60)
link_enter=Entry(root,width=70,textvariable=link).place(x=32,y=90)

def Downloader():
    url=YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text='DOWNLOAD',font='arial 15 bold',bg='dodgerblue', padx=2,command=Downloader).place(x=180,y=150)

root.mainloop()








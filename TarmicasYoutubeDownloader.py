from pytube import YouTube
import tkinter

root = tkinter.Tk()

screen = tkinter.Entry(root)
screen.insert(0,"enter youtube video url")
screen.pack()
def downloadd():
    video=screen.get()
    YouTube(video).streams.first().download(output_path=r'C:\Users\im_bradley\Downloads')
download_button= tkinter.Button(command=downloadd(), name="Download")
download_button.pack()


root.mainloop()
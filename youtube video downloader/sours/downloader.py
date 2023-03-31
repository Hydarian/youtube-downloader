import tkinter as tk
from tkinter.ttk import *
from pytube import YouTube
from os import getcwd



def download ():
    video_quality = video_quality_var.get()
    donwload_link = download_link_var.get()
    here_dir = getcwd()
    yt = YouTube(donwload_link)
    mp4_video = yt.streams.filter(file_extension='mp4')
    mp4_download_video = mp4_video.get_by_resolution(video_quality)
    mp4_download_video.download(here_dir)
    
    

window = tk.Tk()

window.title('youtube downloader')

# window and screen size
WIDTH = 900
HEIGHT = 800
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (WIDTH/2))
y = int((screen_height/2) - (HEIGHT/2))

# set the window size and position
window.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')

download_link_var = tk.StringVar()
video_quality_var = tk.StringVar()

# set lable
input_label = tk.Label(window, text='Copy your youtube link: ', font=('Arial', 25)).place(x=270 ,y=250)

# input
input_link = tk.Entry(window, textvariable=download_link_var ,  width=50, font=('Arial', 20)).place(x=70, y=320)

# button
btn = tk.Button(window, text='Download', bg='#539165', width=10, height=2,
                 fg='white', font=('Arial', 15), command=download,).place(x=370, y=400)


# label for combobox
combo_label = tk.Label(window, text='Quality: ', font=('Arial', 19)).place(x=550, y=420)

# combobox
combo = Combobox(window, textvariable=video_quality_var, values=['360p', '480p', '720p', '1080p']).place(x=655, y=428)


window.mainloop()

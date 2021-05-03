import pytube
import pafy
import tkinter



def video(url):
    direccion = r"C:\Users\Maximo\Videos\Python\Video"
    youtube = pytube.YouTube(url)
    print(url.title)
    print("Descargando..")
    video = youtube.streams.get_highest_resolution()
    video.download(direccion)
    print("Done")

def getVideo():
    url = Cajaurl.get()
    video(url)

def getAudio():
    url = Cajaurl.get()
    audio(url)

def audio(url):
    direccion = r"C:\Users\Maximo\Videos\Python\Audio"
    video = pafy.new(url)
    audiostreams = video.audiostreams
    audiostreams[1].download(filepath = direccion)

#ventana
ventana = tkinter.Tk()
ventana.title("Youtube Downloader")
ventana.resizable(False, False)
#titulo
youtubeDownloader = tkinter.Label(ventana, text = "Di Napoli todos los derechos recervados")
youtubeDownloader.grid(row = 0, column = 0)
#cajaURL
Cajaurl = tkinter.Entry(ventana)
Cajaurl.grid(row = 1, column = 1)
#botonVideo
botonVideo = tkinter.Button(ventana, text = "Video", command = lambda: getVideo())
botonVideo.grid(row = 3, column = 0)
#botonAudio
botonAudio = tkinter.Button(ventana, text = "Audio", command = lambda: getAudio())
botonAudio.grid(row = 3, column = 2)
#Correr ventanas
ventana.mainloop()
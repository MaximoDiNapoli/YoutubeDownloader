import pytube
url = input("Ingresar url")
direccion = input("Ingresa ruta (por defecto es videos python)")
if direccion == '':
    direccion = r"C:\Users\Maximo\Videos\VideosPython"
youtube = pytube.YouTube(url)
print(url.title)
print("Descargando..")
video = youtube.streams.get_highest_resolution()
video.download(direccion)
print("a casa platita")
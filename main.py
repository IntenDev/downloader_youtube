from tkinter import *
from pytube import YuoTube

root = Tk()
root.geometry('500x300') # Размер окна
root.resizable(0,0) # Фиксируем размер
root.title('Yuotube video downloader')
# TODO: Если фонт не сработает переименовать шрифт
Label(root, text = 'Youtube Video Downloader', font = 'Arial 20 bold').pack()

# Поле для ссылки
link = StringVar()
Label(root, text = 'Вставтье линк сюда:', font = 'Arial 15 bold').place(x = 32, y = 90)

# Функция для скачивания
def Downloader():
    url = Youtube(str(link.get()))
    video = url.streams.first()
    video.dowmload()
    Label(root, text = 'DOWNLOAD', font = 'Arial 15').place(x = 100, y = 210)
Button(root, text = 'DOWNLOAD', font = 'Arial 15 bold', bg = 'pale violet red', padx = 2, command = Downoader).place(x = 180, y = 150)
root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from Scripts.Kalkulyator import window


def loade_image():
    try:
        response = request.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return Image.PhotoImage(img)
    except Exception as e:
        print(f"Произлшда ошибка: {e}")
        return None


window = Tk()
window.title("Cats!")
window.geometry("600x400")

label = Label()
label.pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()

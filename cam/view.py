import customtkinter as ctk
import cv2
from PIL import Image

class LayoutCam():
    pass

class LayoutConfig():
    pass


class MainPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Laboratoire python")
        self.geometry("1000x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.label = ctk.CTkLabel(self, text="Bonjour")
        self.label.grid(row=0, column=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

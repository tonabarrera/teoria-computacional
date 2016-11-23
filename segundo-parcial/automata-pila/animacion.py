# -*- coding: utf-8 -*-
from __future__ import print_function
import tkinter as tk

class Animacion(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, background='white')
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.centrarVentana()

    def animar(self):
        self.canvas.create_rectangle(325, 200, 400, 275,  fill = '#00cc9a')
        self.canvas.create_line(362, 150, 362, 200, arrow=tk.FIRST)
        self.canvas.create_line(362, 325, 362, 275, arrow=tk.FIRST)

    def centrarVentana(self):
        ancho, altura = 750, 500
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho)/2
        posicion_y = (altura_pantalla - altura)/2
        self.master.geometry('%dx%d+%d+%d' % (ancho, altura, posicion_x, posicion_y))

#diagrama_protocolo.py
# -*- coding: utf-8 -*-
from __future__ import print_function
import tkinter as tk

class Diagrama(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, background='white')
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.dibujarDiagrama()
        self.centrarVentana()

    def dibujarDiagrama(self):
        coord_circulo = [100, 205, 150, 255]
        self.dibujarLinea([25, 275, 100, 275])
        self.dibujarCirculo([100, 255, 150, 305])
        self.dibujar_bases()
        self.reflexiva()
        self.normal()
        self.reves()
        self.masflechas()

    def dibujarCirculo(self, coordenadas):
        self.canvas.create_oval(coordenadas)

    def dibujarLinea(self, coordenadas):
        self.canvas.create_line(coordenadas)

    def dibujar_bases(self):
        x, y = 100, 100
        for num in range(3):
            self.dibujarLinea([140, 260, 200, 180])
            self.dibujarCirculo([100+x, 255-y, 150+x, 305-y])
            self.dibujarLinea([250, 180, 360, 180])
            self.dibujarLinea([410, 180, 520, 180])
            self.dibujarLinea([140, 300, 200, 380])
            self.dibujarCirculo([100+x, 255+y, 150+x, 305+y])
            self.dibujarLinea([150+x, 380, 260+x, 380])
            x = x + 160
            if num == 2:
                self.dibujarCirculo([100+x, 255+y, 150+x, 305+y])
                self.dibujarCirculo([105+x, 260+y, 145+x, 300+y])
                self.dibujarCirculo([105+x-160, 260-y, 145+x-160, 300-y])

    def reflexiva(self):
        extra = {'start': 20, 'extend': 255}
        self.crear_arco([85, 245, 120, 275], extra)
        extra = {'start': -20, 'extend': 275}
        self.crear_arco([195, 135, 225, 165], extra)
        extra = {'start': -20, 'extend': 275}
        self.crear_arco([195, 335, 225, 365], extra)

    def normal(self):
        extra = {'start': 87, 'extend': 105}
        self.crear_arco([125, 175, 270, 310], extra)
        extra = {'start': 45, 'extend': 95}
        self.crear_arco([225, 150, 390, 250], extra)
        extra = {'start': 25, 'extend': 135}
        self.crear_arco([235, 105, 545, 300], extra)
        extra = {'start': 30, 'extend': 165}
        self.crear_arco([120, 100, 385, 350], extra)
        extra = {'start': 20, 'extend': 150}
        self.crear_arco([120, 25, 545, 450], extra)

    def reves(self):
        extra = {'start': -87, 'extend': -105}
        self.crear_arco([125, 250, 270, 390], extra)
        extra = {'start': -45, 'extend': -95}
        self.crear_arco([225, 310, 390, 410], extra)
        extra = {'start': -25, 'extend': -135}
        self.crear_arco([235, 260, 545, 455], extra)
        extra = {'start': -25, 'extend': -165}
        self.crear_arco([125, 205, 385, 455], extra)
        extra = {'start': -24, 'extend': -150}
        self.crear_arco([123, 115, 550, 520], extra)
        extra = {'start': -20, 'extend': -150}
        self.crear_arco([123, 50, 730, 580], extra)
        extra = {'start': -20, 'extend': -145}
        self.crear_arco([235, 200, 730, 500], extra)

    def masflechas(self):
        self.dibujarLinea([545, 205, 545, 355])
        self.dibujarLinea([235, 200, 545, 355])
        self.dibujarLinea([235, 200, 700, 355])
        self.dibujarLinea([235, 200, 385, 355])
        self.dibujarLinea([545, 205, 230, 355])
        self.dibujarLinea([385, 205, 230, 355])
        self.dibujarLinea([235, 200, 230, 355])


    def crear_arco(self, coordenadas, extra=None):
        self.canvas.create_arc(coordenadas, start=extra['start'], extent=extra['extend'], style='arc')

    def centrarVentana(self):
        ancho, altura = 900, 605
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho)/2
        posicion_y = (altura_pantalla - altura)/2
        self.master.geometry('%dx%d+%d+%d' % (ancho, altura, posicion_x, posicion_y))

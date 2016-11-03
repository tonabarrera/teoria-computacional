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
        self.puntos()
        self.letras()

    def letras(self):
        self.canvas.create_text(125, 150+130, text='A')
        self.canvas.create_text(225, 100+80, text='B')
        self.canvas.create_text(385, 100+80, text='C')
        self.canvas.create_text(545, 100+80, text='D')
        self.canvas.create_text(225, 250+130, text='E')
        self.canvas.create_text(385, 250+130, text='F')
        self.canvas.create_text(545, 250+130, text='G')
        self.canvas.create_text(705, 250+130, text='H')

    def dibujarCirculo(self, coordenadas):
        self.canvas.create_oval(coordenadas)

    def dibujarLinea(self, coord):
        self.canvas.create_line(coord)
        self.canvas.create_oval(coord[2]-3, coord[3]-3, coord[2]+3, coord[3]+3, fill='black')

    def dibujar_bases(self):
        x, y = 100, 100
        for num in range(3):
            self.dibujarLinea([140, 260, 200, 185])
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
        extra = {'start': -30, 'extend': -160}
        self.crear_arco([125, 205, 385, 455], extra)
        extra = {'start': -24, 'extend': -150}
        self.crear_arco([123, 115, 550, 520], extra)
        extra = {'start': -20, 'extend': -150}
        self.crear_arco([123, 50, 730, 580], extra)
        extra = {'start': -20, 'extend': -145}
        self.crear_arco([235, 200, 730, 500], extra)

    def masflechas(self):
        self.dibujarLinea([545, 205, 555, 355])

        self.dibujarLinea([545, 355, 235, 200])
        self.dibujarLinea([700, 355, 235, 200])
        self.dibujarLinea([385, 355, 235, 200])
        self.dibujarLinea([545, 205, 240, 360])
        self.dibujarLinea([385, 205, 240, 360])
        self.dibujarLinea([230, 355,235, 200])

    def crear_arco(self, coord, extra=None):
        self.canvas.create_arc(coord, start=extra['start'], extent=extra['extend'], style='arc')

    def puntos(self):
        self.canvas.create_oval(123, 250, 129, 257, fill='black')
        self.canvas.create_oval(124, 301, 131, 308, fill='black')
        self.canvas.create_oval(204, 361, 211, 368, fill='black')
        self.canvas.create_oval(242, 389, 249, 396, fill='black')
        self.canvas.create_oval(204, 161, 211, 168, fill='black')

        self.canvas.create_oval(242, 163, 249, 170, fill='black')

    def centrarVentana(self):
        ancho, altura = 880, 605
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho)/2
        posicion_y = (altura_pantalla - altura)/2
        self.master.geometry('%dx%d+%d+%d' % (ancho, altura, posicion_x, posicion_y))

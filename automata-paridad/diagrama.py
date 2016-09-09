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
        self.dibujarFlecha([10, 100, 50, 100])
        self.dibujarCirculo([55, 55, 145, 145])
        for x in range(4):
            if x == 0:
                coordenadas = [50, 50, 150, 150]

                text_circulo = 'q%s' % x
                self.dibujarFlechaHorizontal(coordenadas[:])
                self.dibujarFlechaVertical(coordenadas[:])
            elif x == 1:
                coordenadas = [350, 50, 450, 150]
                text_circulo = 'q%s' % x
                self.dibujarFlechaVertical(coordenadas[:])
            elif x == 2:
                coordenadas = [50, 350, 150, 450]
                text_circulo = 'q%s' % x
                self.dibujarFlechaHorizontal(coordenadas[:])
            elif x == 3:
                coordenadas = [350, 350, 450, 450]
                text_circulo = 'q%s' % x

            else:
                print('Na')

            self.dibujarCirculo(coordenadas)
            self.canvas.create_text(coordenadas[0]+50, coordenadas[1]+50, font=('15'), text=text_circulo)

    def dibujarCirculo(self, arg):
        circulo = self.canvas.create_oval(arg)

    def dibujarFlechaHorizontal(self, coordenadas):
        coordenadas[0] += 85
        coordenadas[2] += 215
        x = ((coordenadas[2] - coordenadas[0])/2) + coordenadas[0]

        self.canvas.create_text(x, coordenadas[1]-10, font=('15'), text='1')
        self.canvas.create_text(x, coordenadas[3]-10, font=('15'), text='1')

        self.canvas.create_arc(coordenadas, start=25, extent=130, style='arc')
        self.canvas.create_arc(coordenadas, start=-25, extent=-130, style='arc')

        self.canvas.create_oval(coordenadas[2]-5-15, coordenadas[1]-5+25, coordenadas[2]+5-15, coordenadas[1]+5+25, fill = 'black')
        self.canvas.create_oval(coordenadas[0]-5+10, coordenadas[3]-5-30, coordenadas[0]+5+10, coordenadas[3]+5-30, fill = 'black')

    def dibujarFlechaVertical(self, coordenadas):
        coordenadas[1] += 85
        coordenadas[3] += 215

        y = ((coordenadas[3] - coordenadas[1])/2) + coordenadas[1]

        self.canvas.create_text(coordenadas[0]+10, y, font=('15'), text='0')
        self.canvas.create_text(coordenadas[2]-10, y, font=('15'), text='0')

        self.canvas.create_arc(coordenadas, start=-65, extent=130, style='arc')
        self.canvas.create_arc(coordenadas, start=115, extent=130, style='arc')

        self.canvas.create_oval(coordenadas[0]-5+30, coordenadas[3]-5-220, coordenadas[0]+5+30, coordenadas[3]+5-220, fill = 'black')
        self.canvas.create_oval(coordenadas[2]-5-30, coordenadas[1]-5+220, coordenadas[2]+5-30, coordenadas[1]+5+220, fill = 'black')

    def dibujarFlecha(self, coordenadas):
        linea = self.canvas.create_line(coordenadas)
        self.canvas.create_text(coordenadas[0]+15, coordenadas[1]-10, text='Inicio')
        self.canvas.create_oval(coordenadas[2]-5, coordenadas[1]-5, coordenadas[2]+5,coordenadas[1]+5, fill = 'black')

    def centrarVentana(self):
        ancho, altura = 500, 500
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho)/2
        posicion_y = (altura_pantalla - altura)/2
        self.master.geometry('%dx%d+%d+%d' % (ancho, altura, posicion_x, posicion_y))

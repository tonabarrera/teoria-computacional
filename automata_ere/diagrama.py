# -*- coding: utf-8 -*-
from __future__ import print_function
import tkinter as tk

class Diagrama(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, background='white')
        self.pack(fill=tk.BOTH, expand=1)
        self.dibujarDiagrama()
        self.centrarVentana()

    # def iniciar_UI(self):
    #     self.master.title('Automata ere')
    #
    #     self.quit = tk.Button(self, text="Salir", fg="red", command=root.destroy)
    #     self.quit.pack(side="top")

    def dibujarDiagrama(self):
        canvas = tk.Canvas(self)

        flecha_cero = self.crear_flecha(canvas, [10, 150, 50, 150])
        arco_uno = self.crear_arco(canvas, [10, 50, 100, 150])
        coordenadas = [50, 100, 150, 200]
        estado_cero = self.crear_circulo(canvas, coordenadas)

        flecha_cero_uno = self.crear_flecha(canvas, [150, 150, 210, 150])

        coordenadas = [210, 100, 310, 200]
        estado_uno = self.crear_circulo(canvas, coordenadas)

        flecha_uno_dos = self.crear_flecha(canvas, [310, 150, 210+150, 150])

        coordenadas = [210 + 150, 100, 310+150, 200]
        estado_dos = self.crear_circulo(canvas, coordenadas)

        flecha_dos_tres = self.crear_flecha(canvas, [310+150, 150, 210+300, 150])

        coordenadas = [210 + 300, 100, 310 + 300, 200]
        estado_tres = self.crear_circulo(canvas, coordenadas)

        coordenadas = [215+300, 105, 305+300, 195]
        circulo_interior = self.crear_circulo(canvas, coordenadas)
        canvas.delete(circulo_interior)

        canvas.pack(fill=tk.BOTH, expand=1)

    def crear_circulo(self, canvas, coordenadas):
        circulo = canvas.create_oval(coordenadas)
        return circulo

    def crear_flecha(self, canvas, coordenadas):
        linea = canvas.create_line(coordenadas)
        canvas.create_oval(coordenadas[2]-4, coordenadas[1]-4, coordenadas[2]+4,coordenadas[1]+4, fill = 'black')
        return linea

    def crear_arco(self, canvas, coordenadas):
        arco = canvas.create_arc(coordenadas, extent=270, start = 0, style='arc')
        return arco

    def centrarVentana(self):
        ancho, altura = 700, 350
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho)/2
        posicion_y = (altura_pantalla - altura)/2
        self.master.geometry('%dx%d+%d+%d' % (ancho, altura, posicion_x, posicion_y))

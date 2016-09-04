# -*- coding: utf-8 -*-
from __future__ import print_function
import tkinter as tk

class Diagrama(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, background='white')
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.dibujarDiagrama()
        self.centrarVentana()

    # def iniciar_UI(self):
    #     self.quit = tk.Button(self, text="Salir", fg="red", command=root.destroy)
    #     self.quit.pack(side="top")

    def dibujarDiagrama(self):
        canvas = tk.Canvas(self, bg='white')
        datos = {}
        datos['coordenadas'] = [100, 100, 200, 200]
        datos['canvas'] = canvas
        self.circulos_flechas(datos)

        self.crear_arco(canvas, [150, 50, 300, 150])
        canvas.create_text(150+75, 50-15, text='No e ni r')
        self.crear_arco(canvas, [320, 20, 585, 190])
        canvas.create_text(320+130, 50-10, text='e')
        # reflexiva
        extra = {'start': 30, 'extend': 235}
        self.crear_arco(canvas, [80, 90, 135, 150], extra)
        canvas.create_text(80-5, 90, text='No e')
        self.crear_arco(canvas, [230, 90, 285, 150], extra)
        canvas.create_text(230, 90, text='e')

        #de cabeza
        extra = {'start': 0, 'extend': -180}
        self.crear_arco(canvas, [150, 100, 600, 300], extra)
        canvas.create_text(600-220, 300-10, text='No e ni r')
        self.crear_arco(canvas, [175, 140, 430, 250], extra)
        canvas.create_text(430-120, 300-40, text='No e')
        self.crear_arco(canvas, [450, 170, 585, 225], extra)
        canvas.create_text(585-50, 225+10, text='r')

        canvas.pack(fill=tk.BOTH, expand=1)

    def circulos_flechas(self, arg):
        coordenadas = arg['coordenadas']
        canvas = arg['canvas']
        for x in range(4):
            self.escribirTexto(canvas, x, coordenadas)
            self.dibujarCirculo(canvas, coordenadas)
            self.dibujarFlecha(canvas, [coordenadas[0]-50, 150, coordenadas[2]-100, 150])
            coordenadas[0] += 150
            coordenadas[2] += 150

        print('cordenada', coordenadas[0])
        self.dibujarCirculo(canvas, [coordenadas[0]-150+5, 105, coordenadas[2]-155, 195]) # circulo interior

    def escribirTexto(self, canvas, x, coordenadas):
        text = ''
        text_flecha =''
        if x == 0:
            text = 'q%s' % x
            text_flecha = ''
        elif x == 1:
            text = 'q%s' % x
            text_flecha = 'e'
        elif x == 2:
            text = 'q%s' % x
            text_flecha = 'r'
        elif x == 3:
            text = 'q%s' % x
            text_flecha = 'e'
        else:
            print('otro')

        canvas.create_text(coordenadas[0]+50, coordenadas[1]+50, font=('15'), text=text)
        canvas.create_text(coordenadas[0]-25, coordenadas[1]+40, text=text_flecha)

    def dibujarCirculo(self, canvas, coordenadas):
        circulo = canvas.create_oval(coordenadas)

    def dibujarFlecha(self, canvas, coordenadas):
        linea = canvas.create_line(coordenadas)
        canvas.create_oval(coordenadas[2]-7, coordenadas[1]-7, coordenadas[2]+7,coordenadas[1]+7, fill = 'black')

    def crear_arco(self, canvas, coordenadas, extra=None):
        if extra != None:
            arco = canvas.create_arc(coordenadas, start=extra['start'], extent=extra['extend'], style='arc')
            if extra['extend'] == -180:
                canvas.create_oval(coordenadas[0]-7, 100+100-7, coordenadas[0]+7, 100+100+7, fill = 'black')
        else:
            arco = canvas.create_arc(coordenadas, start=0, extent=180, style='arc')
            canvas.create_oval(coordenadas[0]-7, 100-7, coordenadas[0]+7, 100+7, fill = 'black')

    def centrarVentana(self):
        ancho, altura = 700, 350
        ancho_pantalla = self.winfo_screenwidth()
        altura_pantalla = self.winfo_screenheight()
        posicion_x = (ancho_pantalla - ancho)/2
        posicion_y = (altura_pantalla - altura)/2
        self.master.geometry('%dx%d+%d+%d' % (ancho, altura, posicion_x, posicion_y))

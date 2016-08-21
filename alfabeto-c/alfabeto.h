#ifndef __ALFABETO__
#define __ALFABETO__

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static const char ALFABETO[2] = {'0', '1'};
int iniciar();
int abrir_archivo(FILE **);
int generar_palabras();
int random_k();
int random_manual();

#endif

#ifndef __ARBOL__
#define __ARBOL__

#include <stdio.h>
#include <stdlib.h>

struct Nodos{
  int dato[3];
  struct Nodos *siguiente;
};

typedef struct Nodos Nodo;

struct Arbol{
  int elemento[3];
  struct Arbol *arbolA;
  struct Arbol *arbolB;
  struct Arbol *arbolC;
  Nodo *primero;
};
int insertar(struct Arbol **, int[3], Nodo *, int);
int crear_arbol(struct Arbol **, int[3], Nodo *);
void imprimir_arbol(struct Arbol *, int);

#endif

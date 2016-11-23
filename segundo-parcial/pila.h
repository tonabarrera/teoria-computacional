#ifndef __PILA_H_
#define __PILA_H_

#include <stdio.h>
#include <stdlib.h>

struct Nodos {
  char dato;
  struct Nodos *siguiente;
};

typedef struct Nodos Nodo;

typedef struct Pila {
  Nodo *tope;
} Pila;

void iniciar_pila(Pila *);
void push(Pila *, char);
void pop(Pila *);
void recursivo(Nodo *);
void recorrer(Pila *);
#endif

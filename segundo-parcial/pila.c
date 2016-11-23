#include "pila.h"

void iniciar_pila(Pila *pila) {
  pila->tope = NULL;
}

void recorrer(Pila *pila) {
  recursivo(pila->tope);
}

void recursivo(Nodo *nodo) {
  if(nodo->siguiente != NULL){
    printf("%d\n", nodo->dato);
    recursivo(nodo->siguiente);
  }
}

void push(Pila *pila, char valor) {
  Nodo *temporal = NULL;
  temporal = (Nodo *) malloc(sizeof(Nodo));
  if(temporal == NULL)
    return;

  temporal->dato = valor;
  temporal->siguiente = pila->tope;
  pila->tope = temporal;
}

void pop(Pila *pila) {
  Nodo *temporal = NULL;
  temporal = (Nodo *) malloc(sizeof(Nodo));
  if(temporal == NULL)
    return;
  temporal = pila->tope;
  pila->tope = temporal->siguiente;

}

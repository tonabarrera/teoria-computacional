#include "arbol.h"
int insertar(struct Arbol **arbol, int valor[3], Nodo *lista, int continuar) {
    int valor_aux[3];
    struct Arbol *arbol_nuevo = NULL;
    if(arbol == NULL) {
        return -1; //No existe
    }
    int existe_arbol_nuevo = crear_arbol(&arbol_nuevo, valor, lista);
    if(existe_arbol_nuevo==-1) {
        return -1; // No existe
    }
    if (*arbol == NULL) {
        *arbol = arbol_nuevo; //Raiz
    }
    if (continuar == 0){
        //printf("Termino");
        return 1;
    }
    if (valor[1] > 0 && valor[2] > 0) {
        int repetido =0;
        valor_aux[1] = valor[1] - 1;
        valor_aux[2] = valor[2] - 1;
        valor_aux[0] = valor[0] + 2;
        Nodo *mas = arbol_nuevo->primero;
        while(mas != NULL){
            if((mas->dato[0] == valor_aux[0])&&(mas->dato[1] == valor_aux[1])&&(mas->dato[2] == valor_aux[2])) {
                repetido = 1;
                break;
            }
            mas = mas->siguiente;
        }
        if (repetido == 0){
            insertar(&((*arbol)->arbolA), valor_aux, arbol_nuevo->primero, 1);
        } else{
            insertar(&((*arbol)->arbolA), valor_aux, arbol_nuevo->primero, 0);
        }
    }
    if (valor[0] > 0 && valor[2] > 0) {
        int repetido =0;
        valor_aux[0] = valor[0] - 1;
        valor_aux[2] = valor[2] - 1;
        valor_aux[1] = valor[1] + 2;
        Nodo *mas = arbol_nuevo->primero;
        while(mas != NULL){
            if((mas->dato[0] == valor_aux[0])&&(mas->dato[1] == valor_aux[1])&&(mas->dato[2] == valor_aux[2])) {
                repetido = 1;
                break;
            }
            mas = mas->siguiente;
        }
        if (repetido == 0){
            insertar(&((*arbol)->arbolB), valor_aux, arbol_nuevo->primero, 1);
        } else{
            insertar(&((*arbol)->arbolB), valor_aux, arbol_nuevo->primero, 0);
        }
    }
    if (valor[0] > 0 && valor[1] > 0) {
        int repetido =0;
        valor_aux[0] = valor[0] - 1;
        valor_aux[1] = valor[1] - 1;
        valor_aux[2] = valor[2] + 2;
        Nodo *mas = arbol_nuevo->primero;
        while(mas != NULL){
            if((mas->dato[0] == valor_aux[0])&&(mas->dato[1] == valor_aux[1])&&(mas->dato[2] == valor_aux[2])) {
                repetido = 1;
                break;
            } else{
            }
            mas = mas->siguiente;
        }
        if (repetido == 0){
            insertar(&((*arbol)->arbolC), valor_aux, arbol_nuevo->primero, 1);
        } else{
            insertar(&((*arbol)->arbolC), valor_aux, arbol_nuevo->primero, 0);
        }
        
    }
    return 1;
}

int crear_arbol(struct Arbol **nuevo, int valor[3], Nodo *lista) {
    struct Arbol *auxiliar = NULL;
    auxiliar = (struct Arbol*)malloc(sizeof(struct Arbol));
    if (auxiliar == NULL) {
        return -1;
    }
    auxiliar->arbolA = NULL;
    auxiliar->arbolB = NULL;
    auxiliar->arbolC = NULL;
    auxiliar->elemento[0] = valor[0];
    auxiliar->elemento[1] = valor[1];
    auxiliar->elemento[2] = valor[2];
    auxiliar->primero = NULL;

    while(lista != NULL){
        Nodo **final_lista = &(auxiliar->primero);
        while(*final_lista != NULL){
            final_lista = &((*final_lista)->siguiente);
        }

        Nodo *temporal = NULL;
        temporal = (Nodo *) malloc(sizeof(Nodo));
        if (temporal == NULL){
            printf("Temporal es null");
        }
        temporal->dato[0] = lista->dato[0];
        temporal->dato[1] = lista->dato[1];
        temporal->dato[2] = lista->dato[2];
        temporal->siguiente = NULL;

        *final_lista = temporal;
        lista = lista->siguiente;
    }

    Nodo **final = &(auxiliar->primero);
    while(*final != NULL){
        final = &((*final)->siguiente);
    }

    Nodo *temporal = NULL;
    temporal = (Nodo *) malloc(sizeof(Nodo));
    if (temporal == NULL){
        printf("Temporal es null");
    }
    temporal->dato[0] = valor[0];
    temporal->dato[1] = valor[1];
    temporal->dato[2] = valor[2];
    temporal->siguiente = NULL;

    *final = temporal;
    *nuevo = auxiliar;
    return 1;
}
void imprimir_arbol(struct Arbol *arbol, int n){
    int contador = 0;
    if(arbol->arbolA != NULL){
        imprimir_arbol(arbol->arbolA, n);
    } else {
        contador = contador +1;
    }

    if(arbol->arbolB != NULL){
        imprimir_arbol(arbol->arbolB, n);
    } else {
        contador = contador +1;
    }
    if(arbol->arbolC != NULL){
        imprimir_arbol(arbol->arbolC, n);
    } else {
        contador = contador +1;
    }
    if (contador == 3){
        FILE *archivo = NULL;
        archivo = fopen("resultado.txt", "a");
        Nodo *mi_nodo = arbol->primero;
        while(mi_nodo !=NULL){
            fprintf(archivo, "[%d,", mi_nodo->dato[0]);
            fprintf(archivo, "%d,", mi_nodo->dato[1]);
            fprintf(archivo, "%d]", mi_nodo->dato[2]);
            fputc(' ', archivo);
            if(mi_nodo->siguiente ==NULL){
                if(mi_nodo->dato[0] == n || mi_nodo->dato[1] == n || mi_nodo->dato[2] == n){
                    fputs("--Falla-- ", archivo);
                }
            }
            mi_nodo = mi_nodo->siguiente;
        }
        fputs("\n", archivo);
        fclose(archivo);
    }
    
}

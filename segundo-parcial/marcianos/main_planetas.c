#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "arbol.h"
int menu() {
    int opcion;
    printf("Que quieres hacer?\n1.-Manual\n2.-Automatico\n3.-Salir\n");
    scanf(" %d", &opcion);
    return opcion;
}

int menu_continuar() {
    int opcion;
    printf("Intentar otra vez?\nSi = 1 NO = 0\n");
    scanf(" %d", &opcion);
    return opcion;
}

int random_longitud() {
    //numero = rand () % (N-M+1) + M;  Está entre M y N
    int longitud = 1 + rand() % (1000 + 1 - 1);
    return longitud;
}

void iniciar(int n){
    FILE *archivo = NULL;
    archivo = fopen("resultado.txt", "w");
    fprintf(archivo, "El numero de elementos es:%d \n", n);
    fclose(archivo);
    srand(time(NULL));
    
    int a = 0;
    int b = 0;
    int c = 0;

    while(1){
        a = n-b;
        while(1){
            int numero[3];
            struct Arbol *arbol_prueba = NULL;
            Nodo *lista = NULL;
            archivo = fopen("resultado.txt", "a");
            numero[0] = a;
            numero[1] = b;
            numero[2] = c;
            insertar(&arbol_prueba, numero, lista, 1);
            fputs("Combinacion: ", archivo);
            fprintf(archivo, "[%d,", numero[0]);
            fprintf(archivo, "%d,", numero[1]);
            fprintf(archivo, "%d]\n", numero[2]);
            fclose(archivo);
            imprimir_arbol(arbol_prueba, n);
            a = a-1;
            c = c+1;
            if (a<0){
                break;
            }
        }
        b = b+1;
        c = 0; 
        if (b == n+1){
            break;
        }
    }
}

int main(int argc, char const *argv[]) {
    int continuar = 1;
    int manual = 1;
    int longitud = 0;
    while(continuar) {
        manual = menu();
        if (manual == 1) {
            printf("%s\n", "Ingresa el numero de elementos  en el intervalo [0-1000]: ");
            scanf("%d", &longitud);
        } else if (manual == 2) {
            longitud = random_longitud();
        } else {
            break;
        }
        printf("El numero de elementos es: %d\n", longitud);
        iniciar(longitud);
        printf("Proceso terminado, revisar archivo resultado.txt\n");
        continuar = menu_continuar();
    }
    return 0;
}

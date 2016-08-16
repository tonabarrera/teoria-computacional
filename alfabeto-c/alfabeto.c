#include "alfabeto.h"

int iniciar() {
    int n = 2;
    FILE *archivo = NULL;
    fclose(archivo);
    return 1;
}

int abrir_archivo(FILE *archivo) {
    archivo = fopen("palabras.txt", "w");
    if (archivo == NULL) {
        printf("%s\n", "No se pudo abrir");
        exit(0);
    }
    return 1;
}

int prueba(){
    printf("%s\n", "Prueba");
    return 1;
}

#include "alfabeto.h"

int iniciar() {
    FILE *archivo = NULL;
    int k = 25;
    int longitud_palabra;
    int j;
    int m;
    int continuar = 1;
    int *palabra_temporal = NULL;

    abrir_archivo(&archivo);
    fputs("S = {e", archivo);

    for (longitud_palabra = 1; longitud_palabra <= k; longitud_palabra++) {
        palabra_temporal = (int*) calloc(longitud_palabra, sizeof(int));
        if(palabra_temporal == NULL) {
            printf("%s\n", "Error en el calloc");
            exit(0);
        }
        while(continuar) {
            fputc(',', archivo);
            for(j = 0; j < longitud_palabra; ++j) {//2 //00
                fputc(ALFABETO[palabra_temporal[j]], archivo);
            }
            for(m = 0; m < longitud_palabra; m++) {
                palabra_temporal[m] += 1;
                if(palabra_temporal[m]> 1) {
                    palabra_temporal[m] = 0;
                } else {break;}
            }
            if(m >= longitud_palabra) {
                free(palabra_temporal);
                break;
            }
        }
        printf("Va en la: %d\n", longitud_palabra);
    }

    fputs("}", archivo);
    fclose(archivo);
    return 1;
}

int abrir_archivo(FILE **archivo) {
    *archivo = fopen("palabras.txt", "w");
    if (*archivo == NULL) {
        printf("%s\n", "No se pudo abrir");
        exit(0);
    }
    return 1;
}

int prueba(){
    printf("%s\n", "Prueba");
    return 1;
}

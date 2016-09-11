#include "alfabeto.h"

int generar_palabras(int potencia_k) {
    FILE *archivo = NULL;
    int long_cadena;
    int i;
    int posicion;
    int *cadena_aux = NULL;

    abrir_archivo(&archivo);
    fputs("S = {e", archivo);

    for (long_cadena = 1; long_cadena <= potencia_k; long_cadena++) {
        cadena_aux = (int*) calloc(long_cadena, sizeof(int));
        if(cadena_aux == NULL) {
            printf("%s\n", "Error en el calloc");
            exit(0);
        }
        while(CONTINUAR) {
            fputc(',', archivo);
            for(i = 0; i < long_cadena; i++) {
                fputc(cadena_aux[i] + '0', archivo);
            }
            for(posicion = 0; posicion < long_cadena; posicion++) {
                cadena_aux[posicion] += 1;
                if(cadena_aux[posicion] > 1) {
                    cadena_aux[posicion] = 0;
                } else {
                    break;
                }
            }
            if(posicion >= long_cadena) {
                free(cadena_aux);
                break;
            }
        }
        printf("Va en 2^%d\n", long_cadena);
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

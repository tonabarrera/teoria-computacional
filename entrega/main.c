#include "alfabeto.h"

int iniciar();
int menu();
int menu_continuar();
int random_potencia_k();

int main(int argc, char const *argv[]) {
    printf("%s\n", "***************Alfabeto****************");
    iniciar();
    return 0;
}

int iniciar() {
    srand(time(NULL));
    int continuar = 1;
    int potencia_k = 1;
    int manual = 1;
    while(continuar) {
        manual = menu();
        if (manual == 1) {
            printf("%s\n", "Ingresa el valor de k: ");
            scanf("%d", &potencia_k);
        } else if (manual == 2) {
            potencia_k = random_potencia_k();
        } else {
            break;
        }
        printf("El valor de k es: %d\n", potencia_k);
        generar_palabras(potencia_k);
        printf("%s\n", "Cadenas guardadas en el archivo palabras.txt");
        continuar = menu_continuar();
    }
    printf("\n%s\n", "Saliendo...");
    return 1;
}

int menu_continuar() {
    int opcion;
    printf("Intentar otra vez?\nSi = 1 NO = 0\n");
    scanf(" %d", &opcion);
    return opcion;
}

int menu() {
    int opcion;
    printf("Que quieres hacer?\n1.-Manual\n2.-Automatico\n3.-Salir\n");
    scanf(" %d", &opcion);
    return opcion;
}

int random_potencia_k() {
    //numero = rand () % (N-M+1) + M;
    // Cambiar el valor del random k a 1000
    int potencia_k = 1 + rand() % (1000 + 1 - 1);
    return potencia_k;
}

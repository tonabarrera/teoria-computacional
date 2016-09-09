#include "alfabeto.h"

int iniciar();
int random_potencia_k();
int random_manual_continuar();

int main(int argc, char const *argv[]) {
    iniciar();
    return 0;
}

int iniciar() {
    srand(time(NULL));
    int continuar = 1;
    int potencia_k = 1;
    int manual = 1;
    while(continuar) {
        manual = random_manual_continuar();
        if (manual) {
            printf("%s\n", "Ingresa el valor de k: ");
            scanf("%d", &potencia_k);
        } else {
            potencia_k = random_potencia_k();
        }
        generar_palabras(potencia_k);
        continuar = random_manual_continuar();
    }
    return 1;
}

int random_potencia_k() {
    //numero = rand () % (N-M+1) + M;
    // Cambiar el valor del random k a 1000
    int potencia_k = 1 + rand() % (10 + 1 - 1);
    return potencia_k;
}

int random_manual_continuar() {
    return (rand() % 2);
}

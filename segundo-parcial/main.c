#include "stack.h"
int main(int argc, char const *argv[]) {
    Stack *pila = NULL;
    pila = (Stack *) malloc(sizeof(Stack));
    init_stack(pila);
    printf("Vacia? %d\n", empty(pila));
    push(pila, 'X');
    printf("Vacia? %d\n", empty(pila));
    printf("Valor %c\n", pop(pila));

    return 0;
}

#include "stack.h"

void init_stack(Stack *stack) {
    stack->top = NULL;
}

int empty(Stack *stack){
    if(stack->top == NULL)
        return 1;
    else
        return 0;
}

void push(Stack *stack, char val) {
    Node *temp = NULL;
    temp = (Node *) malloc(sizeof(Node));
    if(temp == NULL)
        return;

    temp->data = val;
    temp->next = stack->top;
    stack->top = temp;
}
//
// void recorrer(Stack *stack) {
//   recursivo(stack->top);
// }
//
// void recursivo(Node *nodo) {
//   if(nodo->siguiente != NULL){
//     printf("%d\n", nodo->dato);
//     recursivo(nodo->siguiente);
//   }
// }
//


//

char pop(Stack *stack) {
    Node *temp = NULL;
    char val = 'E';
    if(empty(stack)){
        return 'E';
    }
    temp = (Node *) malloc(sizeof(Node));
    if(temp == NULL){
        return 'E';
    }

    temp = stack->top;
    stack->top = temp->next;
    val = temp->data;
    free(temp);
    temp = NULL;
    return val;
}

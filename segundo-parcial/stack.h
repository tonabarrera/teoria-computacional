#ifndef __STACK_H_
#define __STCAK_H_

#include <stdio.h>
#include <stdlib.h>

struct Node {
  char data;
  struct Node *next;
};

typedef struct Node Node;

typedef struct Stack {
  Node *top;
} Stack;
void init_stack(Stack *);
void push(Stack *, char);
char pop(Stack *);
int empty(Stack *);
#endif

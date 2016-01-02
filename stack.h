#ifndef STACK_H
#define STACK_H

#define STACK_SIZE 100


typedef struct stack
{
  int elements[100];
  int top;
  int underflow;
  int overflow;
} stack;


stack * make_stack();
int stack_empty(stack*);
void stack_push(stack*, int);
int stack_pop(stack*);

#endif /* STACK_H */

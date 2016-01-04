#ifndef STACK_H
#define STACK_H

#define STACK_SIZE 100

typedef struct doubleStack
{
  int elements[STACK_SIZE];
  int leftTop;
  int rightTop;
  int leftUnderflow;
  int rightUnderflow;
  int collision;
} doubleStack;

void initialize_doubleStack(doubleStack*);
void doubleStack_pushLeft(doubleStack*, int);
void doubleStack_pushRight(doubleStack*, int);
int doubleStack_popLeft(doubleStack*);
int doubleStack_popRight(doubleStack*);
int doubleStack_emptyLeft(doubleStack*);
int doubleStack_emptyRight(doubleStack*);

typedef struct stack
{
  int elements[STACK_SIZE];
  int top;
  int underflow;
  int overflow;
} stack;

stack * make_stack();
int stack_empty(stack*);
void stack_push(stack*, int);
int stack_pop(stack*);


typedef struct genericStack
{
  void* elements[STACK_SIZE];
  int top;
  int underflow;
  int overflow;
} genericStack;

void genericStack_initialize(genericStack*);
int genericStack_empty(genericStack*);
void genericStack_push(genericStack*, void*);
void* genericStack_pop(genericStack*);

#endif /* STACK_H */

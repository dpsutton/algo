/* #include <stdio.h> */
#include <stdlib.h>
#include "stack.h"

/* #define STACK_SIZE 100 */

int stack_empty(stack* stack) {
  return stack->top == -1;
}

void stack_push(stack* stack, int element) {
  stack->top++;
  stack->elements[stack->top] = element;
}

int stack_pop(stack* stack) {
  if (stack_empty(stack)) {
    stack->underflow = 1;
    return 0;
  }
  int value = stack->elements[stack->top];
  stack->top--;
  return value;
}
stack * make_stack() {

  stack *new_stack = malloc(sizeof *new_stack);
  new_stack->top = -1;
  new_stack->underflow = 0;
  return new_stack;
}

void initialize_doubleStack(doubleStack* stack) {
  stack->leftTop = 0;
  stack->rightTop = STACK_SIZE;
  stack->collision = stack->leftUnderflow = stack->rightUnderflow = 0;
}

void doubleStack_pushLeft(doubleStack* s, int e) {
  s->leftTop++;
  if (s->leftTop == s->rightTop) {
    s->collision = 1;
    return;
  }
  s->elements[s->leftTop] = e;
}

void doubleStack_pushRight(doubleStack* s, int e) {
  s->rightTop--;
  if (s->leftTop == s->rightTop) {
    s->collision = 1;
    return;
  }
  s->elements[s->rightTop] = e;
}

int doubleStack_popLeft(doubleStack* s) {
  int e = s->elements[s->leftTop];
  s->leftTop--;
  if (s->leftTop < 0) {
    s->leftUnderflow = 1;
    return 0;
  }
  return e;
}

int doubleStack_popRight(doubleStack *s) {
  int e = s->elements[s->rightTop];
  s->rightTop++;
  if (s->rightTop > STACK_SIZE) {
    s->rightUnderflow = 1;
    return 0;
  }
  return e;
}

int doubleStack_emptyLeft(doubleStack* s) {
  return s->leftTop == 0;
}

int doubleStack_emptyRight(doubleStack* s) {
  return s->rightTop == STACK_SIZE;
}

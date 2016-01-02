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

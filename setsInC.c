#include <stdio.h>
#include <stdlib.h>
#include "stack.h"
#include "queue.h"

void testEqual(char*, int, int);
#define KRED  "\x1B[31m"
#define KGRN  "\x1B[32m"
#define KNRM  "\x1B[0m"
#define KBLU  "\x1B[34m"
#define KCYN  "\x1B[36m"


void testStack();
void testQueue();

int main()
{
  testStack();
  testQueue();

  printf("%s\n", KNRM);
  return 0;
}

void testQueue() {
  printf("Testing Queues:\n");
  queue* q = make_queue();
  testEqual("empty queue underflow = 0", 0, q->underflow);

  queue_enqueue(q, 1);
  testEqual("first stays at zero", 0, q->head);
  testEqual("tail moves to 1", 1, q->tail);

  for (int i = 0; i < QUEUE_SIZE; i++) {
    queue_enqueue(q, 3);
  }
  queue_enqueue(q, 3);
  testEqual("wrap around to 1", 1, q->tail);
  testEqual("but we have wrapped over good values", 1, q->caughtHead);

  free(q);
  q = make_queue();

  queue_enqueue(q, 1);
  queue_enqueue(q, 2);
  queue_enqueue(q, 3);
  int first = queue_dequeue(q);
  int second = queue_dequeue(q);
  int third = queue_dequeue(q);

  testEqual("comes out in right order", 1, first);
  testEqual("comes out in right order", 3, third);
  testEqual("knows it is empty now", 1, queue_empty(q));
}

void testStack() {
  printf("Testing Stacks:\n");
  stack *stack = make_stack();
  testEqual("empty stack knows its empty", 1, stack_empty(stack));
  testEqual("new stack has underflow = 0", 0, stack->underflow);

  stack_push(stack, 1);
  testEqual("can push to stack", 1, stack->elements[0]);

  stack_push(stack, 2);
  int out = stack_pop(stack);
  testEqual("can pop from stack", 2, out);

  out = stack_pop(stack);
  testEqual("pops in correct order", 1, out);

  out = stack_pop(stack);
  testEqual("invalid pop returns zero", 0, out);
  testEqual("sets underflow on stack", 1, stack->underflow);

  free(stack);

  printf("%s\n", KNRM);
}
void testEqual(char* testName, int expected, int actual) {
  printf("%s%s:\t", KCYN, testName);
  if (expected == actual)
    printf("%stest passed\n", KGRN);
  else {
    printf("%stest failed\n", KRED);
    printf("%sExpected:\t%s%d\t", KNRM, KGRN, expected);
    printf("%sActual:\t%s%d\n", KNRM, KRED, actual);

  }
}

#include <stdlib.h>
#include <stdio.h>
#include "stack_queue_tests.h"
#include "test.h"
#include "../sets/stack.h"
#include "../sets/queue.h"


void testQueue() {
  printTestHeader("Testing Queues:");
  queue* q = make_queue();
  testEqual("empty queue underflow = 0", 0, q->underflow);

  queue_enqueue(q, 1);
  testEqual("first stays at zero", 0, q->head);
  testEqual("tail moves to 1", 1, q->tail);

  for (int i = 0; i < QUEUE_SIZE; i++) {
    queue_enqueue(q, 3);
  }

  testEqual("wrap around to 1", 1, q->tail);
  testEqual("but we have wrapped over good values", 1, q->caughtHead);

  free(q);
  q = make_queue();

  queue_enqueue(q, 1);
  queue_enqueue(q, 2);
  queue_enqueue(q, 3);
  int first = queue_dequeue(q);
  queue_dequeue(q);
  int third = queue_dequeue(q);

  testEqual("comes out in right order", 1, first);
  testEqual("comes out in right order", 3, third);
  testEqual("knows it is empty now", 1, queue_empty(q));
  testEqual("does not think it has caught head", 0, q->caughtHead);

  queue_dequeue(q);
  testEqual("knows it underflows", 1, q->underflow);

  free(q);
  printf("%s\n", KNRM);

}

void testStack() {
  printTestHeader("Testing Stacks:");
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

  printSubHeader("double stack");

  doubleStack *db = malloc(sizeof(doubleStack));
  initialize_doubleStack(db);
  testEqual("double stack correctly initialized", STACK_SIZE, db->rightTop);
  testEqual("left empty at init", 1, doubleStack_emptyLeft(db));
  testEqual("right empty at init", 1, doubleStack_emptyRight(db));

  doubleStack_pushLeft(db, 1);
  testEqual("left pushed onto left", 1, db->elements[db->leftTop]);

  doubleStack_pushRight(db, 2);
  testEqual("right pushed correctly", 2, db->elements[db->rightTop]);

  testEqual("left not empty after push", 0, doubleStack_emptyLeft(db));
  testEqual("right not empty after push", 0, doubleStack_emptyRight(db));


  int left = doubleStack_popLeft(db);
  int right = doubleStack_popRight(db);
  testEqual("left popped correctly", 1, left);
  testEqual("right popped correctly", 2, right);

  testEqual("not underflow left", 0, db->leftUnderflow);
  testEqual("not underflow right", 0, db->rightUnderflow);
  doubleStack_popLeft(db);
  doubleStack_popRight(db);
  testEqual("underflow left", 1, db->leftUnderflow);
  testEqual("underflow right", 1, db->rightUnderflow);

  initialize_doubleStack(db);
  testEqual("no collision after init", 0, db->collision);
  for (int i = 0; i < STACK_SIZE; ++i) {
    doubleStack_pushLeft(db, 4);
    doubleStack_pushRight(db, 5);
  }
  testEqual("collision after filling", 1, db->collision);

  free(db);
  printf("%s\n", KNRM);
}


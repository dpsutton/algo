#include "queue.h"
#include <stdlib.h>
#include <stdio.h>

queue* make_queue() {
  queue *q = malloc(sizeof(queue));
  q->head = q->tail = 0;
  q->underflow = q->caughtHead = 0;
  return q;
}

void queue_enqueue(queue* q, int e) {
  q->elements[q->tail] = e;

  int tail = q->tail++;
  if (tail == QUEUE_SIZE)
    q->tail = 0;
  if (tail = q->head) {
    /* we have wrapped around to the head and are now overwriting good
       values */
    q->caughtHead = 1;
    return;
  }
    
}

int queue_dequeue(queue* q) {
  if (queue_empty(q)) {
    q->underflow = 1;
    return 0;
  }
  int element = q->elements[q->head];
  q->head++;
  if (q->head == QUEUE_SIZE)
    q->head = 0;
  return element;
}

int queue_empty(queue* q) {
  return q->head == q->tail;
}

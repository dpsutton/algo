#ifndef QUEUE_H
#define QUEUE_H

#define QUEUE_SIZE 100

typedef struct queue
{
  int elements[QUEUE_SIZE];
  int head;
  int tail;
  int underflow;
  int caughtHead;
} queue;

queue* make_queue();
void queue_enqueue(queue*, int);
int queue_dequeue(queue*);
int queue_empty();

#endif /* QUEUE_H */

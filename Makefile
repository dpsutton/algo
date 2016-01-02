# I am a comment, and I want to say that the variable CC will be
# the compiler to use.
CC=gcc
# Hey!, I am comment number 2. I want to say that CFLAGS will be the
# options I'll pass to the compiler.
CFLAGS=-c -Wall -g

all: Sets

Sets: stack.o queue.o
	$(CC) setsInC.c stack.o queue.o -o sets

queue.o: queue.c
	$(CC) $(CFLAGS) queue.c

stack.o: stack.c
	$(CC) $(CFLAGS) stack.c

clean:
	rm *o sets

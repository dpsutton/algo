# I am a comment, and I want to say that the variable CC will be
# the compiler to use.
CC=gcc
# Hey!, I am comment number 2. I want to say that CFLAGS will be the
# options I'll pass to the compiler.
CFLAGS=-c -Wall -g
SUBS = test.o stack.o queue.o linked_list.o tree.o

all: Sets

Sets: $(SUBS)
	$(CC) setsInC.c $(SUBS) -o sets

tree.o: tree.c
	$(CC) $(CFLAGS) tree.c

test.o: test.c
	$(CC) $(CFLAGS) test.c

linked_list.o: linked_list.c
	$(CC) $(CFLAGS) linked_list.c

queue.o: queue.c
	$(CC) $(CFLAGS) queue.c

stack.o: stack.c
	$(CC) $(CFLAGS) stack.c

clean:
	rm *o sets

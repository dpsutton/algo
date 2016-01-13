# I am a comment, and I want to say that the variable CC will be
# the compiler to use.
CC=gcc
# Hey!, I am comment number 2. I want to say that CFLAGS will be the
# options I'll pass to the compiler.
CFLAGS=-c -Wall -g
SUBS = test stack queue linked_list tree
OFILES := $(foreach file, $(SUBS), $(file).o)

all: Sets

Sets: $(SUBS)
	$(CC) -Wall -g setsInC.c $(OFILES) -o sets

tree: tree.c
	$(CC) $(CFLAGS) tree.c

test: test.c
	$(CC) $(CFLAGS) test.c

linked_list: linked_list.c
	$(CC) $(CFLAGS) linked_list.c

queue: queue.c
	$(CC) $(CFLAGS) queue.c

stack: stack.c
	$(CC) $(CFLAGS) stack.c

clean:
	rm *o sets

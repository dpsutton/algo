# I am a comment, and I want to say that the variable CC will be
# the compiler to use.
CC=gcc
# Hey!, I am comment number 2. I want to say that CFLAGS will be the
# options I'll pass to the compiler.
CFLAGS=-c -Wall -g
SUBS = stack queue linked_list tree
CODEFILES := $(foreach file, $(SUBS), sets/$(file).o)

TESTS = tree_tests linked_list_tests stack_queue_tests test
TESTFILES := $(foreach file, $(TESTS), test/$(file).o)


ALL: Algo

Algo: $(CODEFILES) $(TESTFILES)
	$(CC) -Wall -g test/setsInC.c $(CODEFILES) $(TESTFILES) -o algo

%.o: %.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm algo
	rm $(shell find ./ -name *.o)

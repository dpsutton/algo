#ifndef TEST_H
#define TEST_H

#define KRED  "\x1B[31m"
#define KGRN  "\x1B[32m"
#define KNRM  "\x1B[0m"
#define KBLU  "\x1B[34m"
#define KCYN  "\x1B[36m"

void printTestHeader(char*);
void printSubHeader(char*);
void testEqual(char*, int, int);
void testPointer(char*, void*, void*);

#endif /* TEST_H */

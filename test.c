#include <stdio.h>
#include "test.h"


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

void testPointer(char* testName, void* expected, void* actual) {
  printf("%s%s:\t", KCYN, testName);
  if (expected == actual)
    printf("%stest passed\n", KGRN);
  else {
    printf("%stest failed\n", KRED);
    printf("%sExpected:\t%s%p\t", KNRM, KGRN, expected);
    printf("%sActual:\t%s%p\n", KNRM, KRED, actual);

  }
}

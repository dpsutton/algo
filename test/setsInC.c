#include <stdio.h>
#include <stdlib.h>
#include "../sets/stack.h"
#include "../sets/queue.h"
#include "../sets/linked_list.h"
#include "test.h"
#include "../sets/tree.h"
#include "linked_list_tests.h"
#include "stack_queue_tests.h"
#include "tree_tests.h"

int main()
{
  testStack();
  testQueue();
  testLinkedList();
  testTree();

  printf("%s\n", KNRM);
  return 0;
}

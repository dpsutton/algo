#include <stdio.h>
#include <stdlib.h>
#include "../sets/stack.h"
#include "../sets/queue.h"
#include "../sets/linked_list.h"
#include "test.h"
#include "../sets/tree.h"
#include "linked_list_tests.h"
#include "stack_queue_tests.h"


void testTree();


int main()
{
  testStack();
  testQueue();
  testLinkedList();
  testTree();

  printf("%s\n", KNRM);
  return 0;
}

void testTree()
{
  printTestHeader("Testing Trees:");
  printSubHeader("Recursive visiting tree");
  tree one = {1, NULL, NULL, NULL};
  tree two = {2, &one, NULL, NULL};
  tree four = {4, NULL, NULL, NULL};
  tree three = {3, &two, &four, NULL};
  printSubHeader("Recursive descent through tree");
  tree_visitRecursive(&three);
  printSubHeader("iterative journey through tree");
  tree_visitIterative(&three);
}





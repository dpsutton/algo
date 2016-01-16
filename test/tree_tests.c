#include <stdlib.h>
#include "tree_tests.h"
#include "test.h"
#include "../sets/tree.h"

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

#include <stdio.h>
#include "tree.h"

void printNode(tree*);

void tree_visitRecursive(tree* n)
{
  if (!n) return;
  tree_visitRecursive(n->left);
  printNode(n);
  tree_visitRecursive(n->right);
}

void tree_visitIterative(tree* n)
{
  printf("not implemented yet");
}

void printNode(tree* n)
{
  if (!n)
    printf("leaf node\n");
  else
    printf("node value:\t%d\n", n->x);
}

#include <stdio.h>
#include "tree.h"
#include "stack.h"

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
  genericStack s;
  genericStack_initialize(&s);
  genericStack_push(&s, n);
  tree* current = NULL;
  while (!(genericStack_empty(&s)))
    {
      current = genericStack_pop(&s);
      if(current->right)
        genericStack_push(&s, current->right);
      if (current->left)
        genericStack_push(&s, current->left);
      
      printNode(current);
    }
}

void printNode(tree* n)
{
  if (!n)
    printf("leaf node\n");
  else
    printf("node value:\t%d\n", n->x);
}

#include <stdio.h>
#include "tree.h"
#include "stack.h"
#include "test.h"

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
      if (current) {
        if(current->right)
          genericStack_push(&s, current->right);
        if (current->left)
          genericStack_push(&s, current->left);
      }
      printNode(current);
    }
}

void printNode(tree* n)
{
  if (!n->left && !n->right)
    printf("%sleaf node value: \t %d %s \n", KRED, n->x, KNRM);
  else
    printf("%snode value:\t%d%s\n", KBLU, n->x, KNRM);
}

#ifndef TREE_H
#define TREE_H

typedef struct treeNode
{
  int x;
  struct treeNode* left;
  struct treeNode* right;
} tree;

void tree_visitRecursive(tree*);
void tree_visitIterative(tree*);

#endif /* TREE_H */

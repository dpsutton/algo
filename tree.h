#ifndef TREE_H
#define TREE_H

typedef struct treeNode
{
  int x;
  struct treeNode* left;
  struct treeNode* right;
  struct treeNode* parent;
} tree;


#endif /* TREE_H */

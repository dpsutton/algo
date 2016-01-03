#ifndef LINKED_LIST_H
#define LINKED_LIST_H

typedef struct listNode
{
  int key;
  struct listNode* next;
  struct listNode* previous;
} listNode;

typedef struct singleNode
{
  int key;
  struct singleNode* next;
} singleNode;

typedef struct singleList
{
  struct singleNode* head;
} singleList;

void linkedList_makeSingle(singleList*);
void linkedList_insertSingle(singleList*, singleNode*);
singleNode* linkedList_deleteSingle(singleList*, singleNode*);
void linkedList_reverseSingle(singleList*);

typedef struct linked_list
{
  /* nil next is head, and previous is tail */
  listNode* nil;
} linkedList;

void linkedList_makeList(linkedList*);
listNode* linkedList_listSearch(linkedList*, int);
void linkedList_listInsert(linkedList*, listNode*);
void linkedList_listDelete(linkedList*, listNode*);

#endif /* LINKED_LIST_H */

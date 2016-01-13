#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

void linkedList_makeList(linkedList* ll) {
  ll->nil = malloc(sizeof(listNode));
  ll->nil->next = ll->nil->previous = ll->nil;
}

listNode* linkedList_listSearch(linkedList* l, int key) {
  listNode* current = l->nil->next;
  while(current != l->nil && current->key != key) {
    current = current->next;
  }
  return current;
}

void linkedList_listInsert(linkedList* l, listNode* e) {
  e->next = l->nil->next;
  l->nil->next->previous = e;
  l->nil->next = e;
  e->previous = l->nil;
}

void linkedList_listDelete(linkedList* l, listNode* e) {
  e->previous->next = e->next;
  e->next->previous = e->previous;
}

void linkedList_makeSingle(singleList* l)
{
  l->head = NULL;
}

void linkedList_insertSingle(singleList* l, singleNode* n)
{
  n->next = l->head;
  l->head = n;
}

singleNode* linkedList_deleteSingle(singleList* l, singleNode* n)
{
  singleNode* current = l->head;
  singleNode* previous = NULL;
  while(current && current != n)
    {
      previous = current;
    }
  if (current != NULL)
    {
      if (previous)
        previous->next = current->next;
      else
        l->head = current->next;
    }
  return current;
}

void linkedList_reverseSingle(singleList* l)
{
  singleNode* current = l->head;
  singleNode* previous = l->head;
  singleNode* next = NULL;
  if (!current || current->next)
    return; /* empty list and single list are already reversed */
  previous->next = NULL; /* the new tail */
  current = current->next;
  while (current)
    {
      next = current->next;
      current->next = previous;
      previous = current;
      current = next;
    }
  l->head = current;
}

void genericList_initialize(genericList* l, comparison_function compare)
{
  l->nil = malloc(sizeof(genericNode));
  l->nil->next = l->nil->previous = l->nil;
  l->compare = compare;
}

void genericList_insert(genericList* l, genericNode* node)
{
  node->next = l->nil->next;
  l->nil->next->previous = node;
  l->nil->next = node;
  node->previous = l->nil;
}

genericNode* genericList_search(genericList* l, void* key)
{
  genericNode* current = l->nil->next;
  while (current != l->nil)
    {
      if (l->compare(current, key))
        return current;
    }
  return NULL;
}

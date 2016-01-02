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

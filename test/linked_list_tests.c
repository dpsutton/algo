#include <stdlib.h>
#include <stdio.h>
#include "../sets/linked_list.h"
#include "test.h"

int compareInteger(genericNode*, void* );


void testLinkedList() {
  printTestHeader("Testing Linked Lists:");
  printSubHeader("Doubly linked list");
  linkedList* ll = malloc(sizeof(linkedList));
  linkedList_makeList(ll);
  testPointer("nil value next points to itself", ll->nil, ll->nil->next);
  testPointer("nil value previous points to itself", ll->nil, ll->nil->previous);

  listNode* searching = linkedList_listSearch(ll, 3);
  testPointer("should not find and be null", ll->nil, searching);

  listNode* newElement = malloc(sizeof(listNode));
  newElement->key = 3;
  linkedList_listInsert(ll, newElement);
  testPointer("should insert as the new head", newElement, ll->nil->next);

  listNode* found = linkedList_listSearch(ll, 3);
  testPointer("should find and return new node", newElement, found);

  linkedList_listDelete(ll, newElement);
  testPointer("should successfully delete the new element", ll->nil, ll->nil->next);
  free(ll);

  printSubHeader("singly linked list");
  singleList* single = malloc(sizeof(singleList));
  linkedList_makeSingle(single);

  singleNode one = {1, NULL};
  linkedList_insertSingle(single, &one);

  testPointer("shoudl add single node", &one, single->head);

  singleNode* deleted = linkedList_deleteSingle(single, &one);
  testPointer("delete returns address of deleted", &one, deleted);
  testPointer("delete sets head back to null when empty", NULL, single->head);

  deleted = linkedList_deleteSingle(single, &one);
  testPointer("delete when not present returns null", NULL, deleted);

  singleNode two = {2, NULL};
  singleNode three = {3, NULL};
  linkedList_insertSingle(single, &one);
  linkedList_insertSingle(single, &two);
  linkedList_insertSingle(single, &three);
  linkedList_reverseSingle(single);
  testPointer("new head is third element", &three, single->head);
  testPointer("second is still two", &two, single->head->next);
  testPointer("third is one", &one, single->head->next->next);
  testPointer("and third points to null", NULL, one.next);
  free(single);

  printSubHeader("generic linked list");
  genericList* l = malloc(sizeof(genericList));
  int firstNodeValue = 1;
  genericNode gen1 = {&firstNodeValue, NULL, NULL };
  int secondNodeValue = 2;
  genericNode gen2 = {&secondNodeValue, NULL, NULL};

  printSubHeader("check the comparison function");
  int comparisonResult = compareInteger(&gen1, &firstNodeValue);
  testEqual("these void pointers aren't that scary",
            1, comparisonResult);

  comparison_function compare = compareInteger;
  genericList_initialize(l, *compare);

  genericList_insert(l, &gen1);
  testPointer("inserted firstNodeValue", &gen1, l->nil->next);
  testPointer("can find it as well",
              &gen1, genericList_search(l, &firstNodeValue));
  testPointer("it set the next node to l->nil",
              l->nil, gen1.next);
  testPointer("it set the previous node to l->nil",
              l->nil, gen1.previous);
  genericList_insert(l, &gen2);
  testPointer("it can add another node (sets as next)",
              &gen2, l->nil->next);
  testPointer("l->nil->next->next is the first inserted element",
              &gen1, l->nil->next->next);
  testPointer("it can still find the original node",
              &gen1, genericList_search(l, &firstNodeValue));

  free(l);
  printf("%s\n", KNRM);
}

int compareInteger(genericNode* n, void* k)
{
  int *x = (int*)k;
  return *(int*)n->value == *x;
}

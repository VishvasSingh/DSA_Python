"""
Difficulty: MEDIUM

https://leetcode.com/problems/design-linked-list/description/

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node,
and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node
in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the index th node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion,
the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the index th node in the linked list. If index
equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater
than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the index th node in the linked list, if the index is valid.


Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3


Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""

class LinkedListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next



class MyLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def get(self, index: int) -> int:
        if index >= self._length:
            return -1

        elif index == self._length - 1:
            return self._tail.val

        curr_index = 0
        curr_node = self._head
        while curr_index < index:
            curr_node = curr_node.next
            curr_index += 1

        return curr_node.val

    def addAtHead(self, val: int) -> None:
        new_node = LinkedListNode(val=val, next=self._head)
        self._head = new_node
        self._length += 1
        if self._tail is None:
            self._tail = self._head


    def addAtTail(self, val: int) -> None:
        new_node = LinkedListNode(val=val, next=None)
        if self._tail:
            self._tail.next = new_node
            self._tail = new_node
        else:
            self._tail = new_node

        if self._head is None:
            self._head = self._tail

        self._length += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self._length:
            raise IndexError('Index is out of linked list range')

        if index == 0:
            self.addAtHead(val)

        elif index == self._length:
            self.addAtTail(val)

        else:
            curr_node = self._head
            curr_index = 0
            while curr_index < index - 1:
                curr_node = curr_node.next
                curr_index += 1

            new_node = LinkedListNode(val)
            next_node = curr_node.next
            curr_node.next = new_node
            new_node.next = next_node
            self._length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self._length:  # Changed to silent return per LeetCode spec
            return

            # Case 1: Deleting Head
        if index == 0:
            self._head = self._head.next
            if self._length == 1:  # If list becomes empty, tail must be None
                self._tail = None

            # Case 2: Deleting Middle or Tail
        else:
            curr_node = self._head
            # Stop at the node BEFORE the one we want to delete
            for _ in range(index - 1):
                curr_node = curr_node.next

            # Delete the node
            curr_node.next = curr_node.next.next

            # Case 3: If we just deleted the last node, update tail
            if index == self._length - 1:
                self._tail = curr_node

        self._length -= 1

    def print_list(self):
        curr = self._head
        values = ''
        while curr is not None:
            values += f"{curr.val} "
            curr = curr.next

        print(values)



if __name__ == '__main__':
    # my_linked_list = MyLinkedList()
    # my_linked_list.addAtHead(1)
    # my_linked_list.addAtIndex(1,2)
    # my_linked_list.addAtIndex(2,3)
    # my_linked_list.addAtIndex(3, 4)
    # my_linked_list.addAtIndex(4, 5)
    # my_linked_list.addAtTail(6)
    # my_linked_list.print_list()
    # my_linked_list.deleteAtIndex(2)
    # my_linked_list.print_list()
    # print(my_linked_list.get(5))

    ## test case 2
    # my_linked_list = MyLinkedList()
    # my_linked_list.addAtHead(1)
    # my_linked_list.print_list()
    # my_linked_list.deleteAtIndex(0)
    # my_linked_list.print_list()
    # print(my_linked_list.get(5))

    ##test case 3
    my_linked_list = MyLinkedList()
    my_linked_list.addAtHead(1)
    my_linked_list.addAtTail(3)
    my_linked_list.addAtIndex(1, 2)
    print(my_linked_list.get(1))
    my_linked_list.deleteAtIndex(0)
    print(my_linked_list.get(0))



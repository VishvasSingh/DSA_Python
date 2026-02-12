from utils.list_node import ListNode, ListBuilder

"""
DIFFICULTY: EASY

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""

def reverse_list(head: ListNode) -> ListNode:
    if head is None:
        return None

    prev = None

    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


if __name__ == '__main__':
    values = [1,2,3,4,5]
    head = ListBuilder.build_list(values)
    head.print_list()
    new_head = reverse_list(head)
    new_head.print_list()
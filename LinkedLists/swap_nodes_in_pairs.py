from utils.list_node import ListNode, ListBuilder
from typing import Optional

"""
DIFFICULTY: MEDIUM

https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]



Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

"""

def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    first_node = head
    second_node = head.next
    new_head = second_node
    connecting_node = None

    while first_node is not None and second_node is not None:
        second_node.next, first_node.next = first_node, second_node.next
        if connecting_node:
            connecting_node.next = second_node

        connecting_node = first_node
        first_node = first_node.next
        second_node = first_node.next if first_node else None

    return new_head



if __name__ == "__main__":
    vals = [1,2,3,4,5, 6]
    head = ListBuilder.build_list(vals)
    new_head = swap_pairs(head)
    new_head.print_list()
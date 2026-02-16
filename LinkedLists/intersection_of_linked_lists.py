from utils.list_node import ListNode
from typing import Optional

"""
DIFFICULTY: EASY

https://leetcode.com/problems/intersection-of-two-linked-lists/description/

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


"""


def get_intersection_node(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    O(M+N) time and O(N) space

    visited_nodes = set()
    curr = headA
    while curr is not None:
        visited_nodes.add(curr)
        curr = curr.next

    curr = headB
    while curr is not None:
        if curr in visited_nodes:
            return curr

        visited_nodes.add(curr)
        curr = curr.next

    return None

    """

    """
    Optimized approach:
    O(M+N) time and O(1) space.
    """

    pA, pB = headA, headB

    # Loop until they point to the same node (or both are None)
    while pA != pB:
        # If pA reaches the end, jump to headB. Otherwise, move next.
        pA = headB if pA is None else pA.next

        # If pB reaches the end, jump to headA. Otherwise, move next.
        pB = headA if pB is None else pB.next

    return pA


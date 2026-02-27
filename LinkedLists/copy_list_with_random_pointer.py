"""
DIFFICULTY: MEDIUM

https://leetcode.com/problems/copy-list-with-random-pointer/description/

A linked list of length n is given such that each node contains an additional random pointer, which could point to
any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node
has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the pointers in the original list and copied list represent
the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding
two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val,
random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not
point to any node.
Your code will only be given the head of the original linked list.

EXAMPLE 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]


"""
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: Optional[Node] = None) -> Node:
    old_and_new_nodes_mapping = {}
    old_and_random_nodes_mapping = {}
    curr_node = head
    prev_node = None
    new_head = None
    while curr_node is not None:
        new_node = Node(curr_node.val)
        if prev_node:
            prev_node.next = new_node

        if new_head is None:
            new_head = new_node

        old_and_new_nodes_mapping[curr_node] = new_node
        if curr_node.random is not None:
            old_and_random_nodes_mapping[curr_node] = curr_node.random

        prev_node = new_node
        curr_node = curr_node.next

    curr_old = head
    curr_new = new_head
    while curr_old is not None:
        if curr_old in old_and_random_nodes_mapping:
            new_random_node = old_and_new_nodes_mapping.get(old_and_random_nodes_mapping.get(curr_old))
            curr_new.random = new_random_node

        else:
            curr_new.random = None

        curr_new = curr_new.next
        curr_old = curr_old.next

    return new_head





if __name__ == "__main__":
    copy_random_list()
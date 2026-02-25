from utils.list_node import ListNode, ListBuilder

"""
DIFFICULTY: MEDIUM

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?


"""

def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    curr_ptr = head
    advance_ptr = head

    for _ in range(n):
        if advance_ptr is None:
            raise IndexError('Index is out of range')
        advance_ptr = advance_ptr.next

    if advance_ptr is None: # this is the case when n is equal to length of linked list & we need to remove head
        head = curr_ptr.next
        del curr_ptr
        return head

    while advance_ptr.next is not None:
        curr_ptr = curr_ptr.next
        advance_ptr = advance_ptr.next

    to_be_deleted = curr_ptr.next
    curr_ptr.next = to_be_deleted.next
    del to_be_deleted

    return head



if __name__ == '__main__':
    values = [1,2,3,4,5]
    head = ListBuilder.build_list(values)
    head.print_list()
    new_head = remove_nth_from_end(head, 6)
    new_head.print_list()

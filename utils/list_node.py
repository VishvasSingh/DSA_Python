from typing import List

"""
List Node definition

"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


    def print_list(self):
        curr = self
        values = ''
        while curr is not None:
            values += f"{curr.val} "
            curr = curr.next

        print(values)




class ListBuilder:

    @staticmethod
    def build_list(values: List[int]) -> ListNode:
        prev_node: ListNode = None
        head = None
        for val in values:
            curr_node = ListNode(val)

            if prev_node is not None:
                prev_node.next = curr_node

            if head is None:
                head = curr_node

            prev_node = curr_node

        return head
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
            Prints values of all the nodes in a list
        :return:
        """
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
            adds value at the end of linked list
        :param value:
        :return:
        """
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node

        else:
            self.head = new_node
            self.tail = new_node

        self.length += 1

        return True

    def pop(self):
        """
            Removes the last element from the linked list and returns its value
        :return: removed value or None
        """

        if self.head and self.head.next:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next

            popped_node = self.tail
            temp.next = None
            self.tail = temp
            self.length -= 1

            return popped_node

        elif self.head and self.head.next is None:
            popped_node = self.head
            self.head = self.tail = None
            self.length -= 1

            return popped_node

        else:
            return None

    def prepend(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node

        else:
            # linked list is empty
            self.head = new_node
            self.tail = new_node

        self.length += 1

        return True

    def pop_first(self):
        if not self.head:
            return None

        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

        return popped_node

    def get(self, index: int):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set(self, index: int, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True

        return False

    def insert(self, index: int, value):
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True






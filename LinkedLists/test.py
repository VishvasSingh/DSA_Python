from linkedlist import LinkedList


link_list = LinkedList(4)

for i in range(3):
    link_list.append(i)

link_list.print_list()

link_list.set(2, 103)

link_list.print_list()

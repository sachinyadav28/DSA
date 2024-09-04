"""
*** Linked Lists Programmes
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        # If list is empty, set tail to new node
        if self.tail is None:
            self.tail = temp

    def insert_at_tail(self, data):
        temp = Node(data)
        # If list is empty, set head and tail to new node
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def insert_at_position(self, position, data):
        # If we want to add at first postion
        if position == 0:
            return self.insert_at_head(data)

        temp = self.head
        count = 0     # Considering list start at 0 index
        while count < position - 1:
            temp = temp.next
            count += 1

        # If we want to add at last position
        if temp.next is None:
            return self.insert_at_tail(data)

        # Create node for new data
        node_to_insert = Node(data)
        node_to_insert.next = temp.next
        temp.next = node_to_insert

    def delete_node_at_postion(self, position):
        # removing head of the list
        if position == 0:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            # TODO: define delete
            # remove at any postion or at end
            pass

    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(None)



ll = LinkedList()

ll.insert_at_tail(20)
ll.insert_at_tail(22)
ll.insert_at_tail(32)
ll.insert_at_tail(44)

ll.insert_at_position(4, 11)

ll.print_ll()

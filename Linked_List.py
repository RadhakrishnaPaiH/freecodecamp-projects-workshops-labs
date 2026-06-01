class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element  # stores the value/data of the node
            self.next = None        # pointer to the next node (initially None)

    def __init__(self):
        self.length = 0     # keeps track of number of nodes in the list
        self.head = None    # first node in the list

    def is_empty(self):
        return self.length == 0  # list is empty if length is 0

    def add(self, element):
        node = self.Node(element)  # create a new node

        if self.is_empty():
            # if list is empty, new node becomes the head
            self.head = node
        else:
            # otherwise, traverse to the last node
            current_node = self.head

            # move until we reach the last node
            while current_node.next is not None:
                current_node = current_node.next

            # link last node to the new node
            current_node.next = node

        # increase list size after adding a node
        self.length += 1

    def remove(self, element):
        previous_node = None          # keeps track of node before current
        current_node = self.head      # start from the head

        # search for the node containing the element
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next

        # if element not found, do nothing
        if current_node is None:
            return

        # if node to remove is not the head
        elif previous_node is not None:
            previous_node.next = current_node.next
        else:
            # if removing the head node
            self.head = current_node.next

        # decrease list size after removal
        self.length -= 1


# ------------------ Testing ------------------

my_list = LinkedList()

print(my_list.is_empty())  # True, list has no elements yet

my_list.add(1)
my_list.add(2)

print(my_list.is_empty())  # False, list now has elements
print(my_list.length)      # 2

my_list.remove(1)

print(my_list.length)      # 1 (since 1 was removed)

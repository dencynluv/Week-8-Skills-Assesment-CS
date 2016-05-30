# Linked list with Node/LinkedList classes


class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node %s>" % self.data


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        """Add node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:  #meaning its pointing to a node
            self.tail.next = new_node #point the tail to the new node

        self.tail = new_node

    def remove_node_by_index(self, index):
        """Remove node with given index."""

        prev = None
        node = self.head
        i = 0

        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1

        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next

    def find_node(self, data):
        """Is a matching node in the list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def print_list(self):
        """Print all items in the list::

            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('fish')

            >>> ll.print_list()
            dog
            cat
            fish
        """

        # FIXME

        current = self.head #initialize temp

        while current is not None: #while there is a node
            print current.data #print the data in that node
            current = current.next # set the pointer to the next node 
            # and loop again until there are no more nodes (ll becomes false)


    def get_node_by_index(self, idx):
        """Return a node with the given index::

            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('fish')

            >>> ll.get_node_by_index(0)
            <Node dog>

            >>> ll.get_node_by_index(2)
            <Node fish>
        """

        # FIXME

        current = self.head #Initialize temp

        count = 0 #Index of the current node

        while current: #loop until end of linked list is not reached
            if count == idx: #if the count matches the index passed
                return current.data #return the data at that node

            count += 1 #set the count to increment by 1 each time it goes through the loop.
            current = current.next #set current to the next node

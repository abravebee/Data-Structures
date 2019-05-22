"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
    # replaces head of the list with a new value 
    # that is passed in
        current_head = self.head
        new_head = ListNode(value)
        
        if not self.head and not self.tail:
            self.head = new_head
            self.tail = new_head

        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1
        pass

    def remove_from_head(self):
    # removes the head node and 
    # returns the value stored in it
        # if empty
        if not self.head and not self.tail:
            return None
        # elif single item
        prev_head = self.head
        if self.head == self.tail or self.head.next == None:
            # set head and tail to None    
            self.head == None
            self.tail == None       
        else:
            # set next value to head
            self.head.delete()
            self.head = prev_head.next
        # decrement length
        return prev_head.value
        self.length -= 1    
        pass

    def add_to_tail(self, value):
    # replaces the tail of the list 
    # with a new value that is passed in
        new_tail = ListNode(value)
        if not self.tail:
            self.head = new_tail
            self.tail = new_tail
        else:
            # insert new node after tail
            self.tail.insert_after(value)
            # set tail to new node
            self.tail = self.tail.next
        self.length += 1
        pass

    def remove_from_tail(self):
    # removes the tail node and 
    # returns the value stored in it
        # if empty
        if not self.tail:
            return None
        prev_tail = self.tail
        if self.tail == self.head or self.tail.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail.delete()
            self.tail = self.tail.prev
        self.length -=1
        return prev_tail.value
        pass

    def move_to_front(self, node):
    # takes a reference to a node in the list and 
    # moves it to the front of the list, 
    # shifting all other list nodes down
        # delete current node (next/prev values will change)
        node.delete()
        # add_to_head(value)
        self.add_to_head(node.value)
        pass

    def move_to_end(self, node):
    # takes a reference to a node in the list and 
    # moves it to the end of the list, 
    # shifting all other list nodes up
        # delete current node (next/prev vals will change)
        node.delete()
        self.length -= 1
        # add_to_tail(value)
        self.add_to_tail(node.value)
        pass

    # takes a reference to a node in the list and 
    # removes it from the list. 
    # The deleted node's `previous` and `next` pointers 
    # should point to each afterwards
    def delete(self, node):
        # if empty list...
        if not self.head and not self.tail: 
            return None
        # if list of one...
        if self.head == self.tail:
            self.head == None
            self.tail == None
        if self.head == node:
            self.head = node.next
            node.delete()
        if self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        self.length -= 1
        pass
        
    def get_max(self):
        # returns the maximum value in the list
        if self.head == None:
            return None
        else:
            item = self.head
            max = self.head
            while item:
                if item.value > max.value:
                    max = item
                item = item.next
            return max.value
        pass

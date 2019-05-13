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
        new_head = ListNode(value, None, current_head)
        
        if self.head == None:
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
        # if empty i.e. self.head and self. tail are null
            # return None
        # elif single item
            # set head and tail to None
            # decrement length
        # else
            # delete head
            # set next value to head
            # decrement length
        pass

    def add_to_tail(self, value):
    # replaces the tail of the list 
    # with a new value that is passed in
        # if empty list
            # set head and tail to new node
        # else
            # insert new node after tail
            # set tail to new node
            # increment length
        pass

    def remove_from_tail(self):
    # removes the tail node and 
    # returns the value stored in it
        # if empty
        #   return None
        # elif single list
        #   set head and tail to None
        # else
        #   delete tail
        #   set tail to old tail's prev    
        
        pass

    def move_to_front(self, node):
    # takes a reference to a node in the list and 
    # moves it to the front of the list, 
    # shifting all other list nodes down
        pass

    def move_to_end(self, node):
        # takes a reference to a node in the list and 
        # moves it to the end of the list, 
        # shifting all other list nodes up
        pass

    def delete(self, node):
        # takes a reference to a node in the list and 
        # removes it from the list. 
        # The deleted node's `previous` and `next` pointers 
        # should point to each afterwards
        if self.head == None:
            return
        else:
            item = self.head
            while item:
                if node == item.value:
                    self.delete(node)
                else:
                    item = item.next
        self.length -= 1
        pass
        
    def get_max(self):
        # returns the maximum value in the list
        
        pass

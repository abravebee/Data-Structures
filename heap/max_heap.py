class Heap:
    def __init__(self):
        self.storage = []

    # adds the input value into the heap; 
    # this method should ensure that the inserted value is in the correct spot in the heap
    def insert(self, value):
        self.storage.append(value)
        index = len(self.storage) - 1
        self._bubble_up(index)
        pass

    # removes and returns the 'topmost' value from the heap; 
    # this method needs to ensure that the heap property is maintained after the topmost element has been removed.
    def delete(self):
        if len(self.storage) == 0:
            return
        elif len(self.storage) == 1:
            return self.storage.pop()
        
        top = self.storage[0]
        self.storage[0] = self.storage.pop()
        self._sift_down(0)
        return top
        pass

    #returns the maximum value in the heap 
    # IN CONSTANT TIME
    def get_max(self):
        return self.storage[0]
        pass

    #  returns the number of elements stored in the heap.
    def get_size(self):
        return len(self.storage)
        pass

    # moves the element at the specified index "up" the heap 
    # by swapping it with its parent 
    # if the parent's value is less than the value at the specified index.
    def _bubble_up(self, index):
        length = self.get_size()
        if index <= 0 or index > length-1:
            return
        parentIndex = (index-1) / 2
        # parentIndex = math.ceil((index-1)/2)
        if parentIndex > length-1 or parentIndex < 0:
            return
        if self.storage[index] > self.storage[parentIndex]:
            hold = self.storage[index]
            self.storage[index] = self.storage[parentIndex]
            self.storage[parentIndex] = hold
            self._bubble_up(parentIndex)
        pass

    # grabs the indices of this element's children 
    # and determines which child has a larger value. 
    # If the larger child's value is larger than the parent's value, 
    # the child element is swapped with the parent
    def _sift_down(self, index):
        length = self.get_size()
        leftChild = index * 2 + 1
        rightChild = index * 2 + 2
        if leftChild > length-1 or rightChild > length-1:
            return
        if self.storage[leftChild] > self.storage[rightChild]:
            largestChild = leftChild
        else:
            largestChild = rightChild
        if self.storage[largestChild] > self.storage[index]:
            hold = self.storage[index]
            self.storage[index] = self.storage[largestChild]
            self.storage[largestChild] = hold
            self._sift_down(largestChild)
        pass

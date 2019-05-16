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
        pass

    #returns the maximum value in the heap 
    # IN CONSTANT TIME
    def get_max(self):
        return self.storage.pop()
        pass

    #  returns the number of elements stored in the heap.
    def get_size(self):
        return len(self.storage)
        pass

    # moves the element at the specified index "up" the heap 
    # by swapping it with its parent 
    # if the parent's value is less than the value at the specified index.
    def _bubble_up(self, index):
        print(f"index: {index}, self.storage: {len(self.storage) - 1}")
        if index < 1 or index > len(self.storage)-1:
            print(f"{index} < 1 or {index} > {len(self.storage) - 1}")
            pass
        parentIndex = (index-1) // 2
        if parentIndex > len(self.storage) or parentIndex < 0:
            return
        while self.storage[index] and self.storage[parentIndex]:
            while self.storage[index] > self.storage[parentIndex]:
                hold = self.storage[index]
                self.storage[index] = self.storage[parentIndex]
                self.storage[parentIndex] = hold
                index += 1
                self._bubble_up(index)
        return
        pass

    # grabs the indices of this element's children 
    # and determines which child has a larger value. 
    # If the larger child's value is larger than the parent's value, 
    # the child element is swapped with the parent
    def _sift_down(self, index):
        pass

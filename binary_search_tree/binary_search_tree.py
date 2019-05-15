class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        pass

# searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
    def contains(self, target):
        # compare target to root
        if target == self.value:
            print(f"target {target} == self.value {self.value}")
            return True
        # if it's smaller, check left side
        elif target < self.value:
            print(f"target {target} < self.value {self.value}")
            # first check that there is a left side; if not, return False
            if not self.left:
                print("no self.left")
                return False
            # else, if it doesn't match the left side, call contains on left side with same target
            elif target != self.left:
                print(f"target {target} != self.left {self.left}")
                return self.left.contains(target)
            else:
                print(f"target {target} == self.left {self.left}")
                return True
        # else, check right side
        elif target > self.value:
            print(f"target {target} > self.value {self.value}")
            # first check that there is a right side; if not, return False
            if not self.right:
                print("no self.right")
                return False
            # else, if it doesn't match the right side, call contains on right side with same target
            elif target != self.right:
                print(f"target {target} != self.right {self.right}")
                return self.right.contains(target)
            else:
                print(f"target {target} == self.right {self.right}")
                return True            
        pass

# returns the maximum value in the binary search tree.
    def get_max(self):
        # find rightmost node
        max = self
        while max.right:
            max = max.right
        return max.value
        pass

# performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. 
# There is a myriad of ways to perform tree traversal; in this case any of them should work. 
    def for_each(self, cb):
        pass
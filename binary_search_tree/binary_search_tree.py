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
        # Inorder
        # if self:
        #     if self.left:
        #         self.left.for_each(cb)
        #     cb(self.value)
        #     if self.right:
        #         self.right.for_each(cb)
        # Preorder
        # if self:
        #     cb(self.value)
        #     if self.left:
        #         self.left.for_each(cb)
        #     if self.right:
        #         self.right.for_each(cb)
        # Postorder
        # if self:
        #     if self.left:
        #         self.left.for_each(cb)
        #     if self.right:
        #         self.right.for_each(cb)
        #     cb(self.value)
        pass

'''
Tree Traversal

    Inorder: Left, Root, Right
        Non decreasing/increasing order
            
            inorder(tree)
                Traverse the left subtree: inorder(left-subtree)
                Visit the root
                Traverse the right subtree: inorder(right-subtree)
                Base: if tree is None

    Preorder: Root, Left, Right
        Create a copy of the tree. Get prefix expression of an expression tree.

            preorder(tree)
                Visit the root
                Traverse the left subtree: preorder(left-subtree)
                Traverse the right subtree: preorder(right-subtree)
                Base: if tree is None

    Postorder: Left, Right, Root
        Delete the tree. Get the postfix expression of an expression tree.

            postorder(tree)
                Traverse the left subtree: postorder(left-subtree)
                Traverse the right subtree: postorder(right-subtree)
                Visit the root
                Base: if tree is None

    Level Order (Breadth First):

            height(node)
                Compute height of left subtree: height(left-subtree)
                Compute height of right subtree: height(right-subtree)
                Return increment of larger height
                Base: if node is None, return 0 (do not increment, do not recurse)

'''
class node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1

    def isLeaf(self):
        return not self.left and not self.right
import node as node

class BST:
    def __init__(self, rootval):
        if rootval == None:
            self.root = None
        else:
            self.root = node.Node(rootval)
        self.traversecount = 0
    
    def insertRec(self, val):
        return self.insertRecHelper(val, self.root, None, False)

    def insertRecHelper(self, val, node, prev, left):
        if not node:
            if self.root == None:
                self.root = node.Node(val)
                return
            if left:
                prev.left = node.Node(val)
                prev.left.parent = prev
                return prev.left
            prev.right = node.Node(val)
            prev.right.parent = prev
            return prev.right

        if val < node.val:
            return self.insertRecHelper(val, node.left, node, True)
        return self.insertRecHelper(val, node.right, node, False)

    def deleteRec(self, val):
        return self.deleteRecHelper(val, self.root, False)
    
    def deleteRecHelper(self, val, node, l):
        if not node:
            return node
        if val < node.val:
            return self.deleteRecHelper(val, node.left, True)
        elif val > node.val:
            return self.deleteRecHelper(val, node.right, False)
        else:
            if node.isLeaf():
                if not node.parent:
                    self.root = None
                elif l:
                    node.parent.left = None
                else:
                    node.parent.right = None
                    
            elif node.left and not node.right:
                if node == self.root:
                    self.root = node.left
                    self.root.parent = None
                    
                elif node.parent.left == node:
                    node.parent.left = node.left
                    node.parent.left.parent = node.parent
                    
                elif node.parent.right == node:
                    node.parent.right = node.left
                    node.parent.right.parent = node.parent
                    
            elif node.right and not node.left:
                if node == self.root:
                    self.root = node.right
                    self.root.parent = None
                    
                elif node.parent.left == node:
                    node.parent.left = node.right
                    node.parent.left.parent = node.parent
                    
                elif node.parent.right == node:
                    node.parent.right = node.right
                    node.parent.right.parent = node.parent
                    
            else:
                next = self.findNextRec(node)
                node.val = next.val
                self.deleteRecHelper(next.val, node.right, False)

    def findNextRec(self, node):
        return self.findNextRecHelper(node, 0, node.val)

    def findNextRecHelper(self, node, func, vala):
        if func == 0 and vala == self.findMaxRec().val:
            print("No higher value found!")
            return None
            
        if func == 0:
            if not node.right:
                return self.findNextRecHelper(node.parent, 2, vala)
            return self.findNextRecHelper(node.right, 1, vala)
            
        if func == 1:
            if not node.left:
                return node
            return self.findNextRecHelper(node.left, 1, vala)
            
        if func == 2:
            if node.val >= vala:
                return node
            return self.findNextRecHelper(node.parent, 2, vala)

    def findPrevRec(self, node):
        return self.findPrevRecHelper(node, 0, node.val)

    def findPrevRecHelper(self, node, func, vala):
        if func == 0 and vala == self.findMinRec().val:
            print("No lower value found!")
            return None
        if func == 0:
            if not node.left:
                return self.findPrevRecHelper(node.parent, 2, vala)
            return self.findPrevRecHelper(node.left, 1, vala)
            
        if func == 1:
            if not node.right:
                return node
            return self.findPrevRecHelper(node.right, 1, vala)
            
        if func == 2:
            if node.val <= vala:
                return node
            return self.findPrevRecHelper(node.parent, 2, vala)

    def findMaxRec(self):
        return self.findMaxRecHelper(self.root)
    
    def findMaxRecHelper(self, node):
        if not node.right:
            return node
        return self.findMaxRecHelper(node.right)

    def findMinRec(self):
        return self.findMinRecHelper(self.root)

    def findMinRecHelper(self, node):
        if not node.left:
            return node
        return self.findMinRecHelper(node.left)

    def insertIter(self, val):
        node = self.root
        if self.root == None:
            self.root = node.Node(val)
            return self.root

        while True:
            prev = node
            if val < node.val:
                if node.left:
                    node = node.left
                    self.traversecount += 1
                    continue
                node.left = node.Node(val)
                node.left.parent = prev
                return node.left
                
            if node.right:
                node = node.right
                self.traversecount += 1
                continue
                
            node.right = node.Node(val)
            node.right.parent = prev
            return node.right

    def deleteIter(self, val):
        node = self.root
        left = False

        while node.val != val:
            if val < node.val:
                node = node.left
                left = True
                
            else:
                node = node.right
                left = False
                
        if node.isLeaf():
            if not node.parent:
                self.root = None
            elif left:
                node.parent.left = None
            else:
                node.parent.right = None
                
        elif node.left and not node.right:
            if node == self.root:
                self.root = node.left
                self.root.parent = None
                
            else:
                self.jumpPointLeft(node)
                
        elif node.right and not node.left:
            if node == self.root:
                self.root = node.right
                self.root.parent = None
                
            else:
                self.jumpPointRight(node)
                
        else:
            next = self.findNextIter(node)
            node.val = next.val
            if next.isLeaf():
                if next.parent.right == next:
                    next.parent.right = None
                else:
                    next.parent.left = None
                    
            elif next.left and next.right:
                next.parent.right = next.right
                next.parent.right.parent = next.parent
                store = next.left
                newnode = next.parent.right
                while newnode.left:
                    newnode = newnode.left
                newnode.left = store
                store.parent = newnode
                
            elif next.left:
                self.jumpPointLeft(next)
            elif next.right:
                self.jumpPointRight(next)
        
    def jumpPointLeft(self, node):
        if node.parent.left == node:
            node.parent.left = node.left
            node.parent.left.parent = node.parent
            
        elif node.parent.right == node:
            node.parent.right = node.left
            node.parent.right.parent = node.parent
    
    def jumpPointRight(self, node):
        if node.parent.left == node:
            node.parent.left = node.right
            node.parent.left.parent = node.parent
            
        elif node.parent.right == node:
            node.parent.right = node.right
            node.parent.right.parent = node.parent


    def findNextIter(self, node):
        val = node.val
        if val == self.findMaxIter().val:
            print("No higher value found!")
            return None
            
        if not node.right:
            node = node.parent
            while node and node.val < val:
                node = node.parent
            return node
            
        else:
            node = node.right
            while node.left:
                node = node.left
            return node

    def findPrevIter(self, node):
        val = node.val
        if val == self.findMinIter().val:
            print("No lower value found!")
            return None
            
        if not node.left:
            node = node.parent
            while node and node.val >= val:
                node = node.parent
            return node
            
        else:
            node = node.left
            while node.right:
                node = node.right
            return node

    def findMaxIter(self):
        node = self.root
        while node.right:
            node = node.right
        return node

    def findMinIter(self):
        node = self.root
        while node.left:
            node = node.left
            
        return node

    def inOrder(self):
        print("INORDER TRAVERSAL")
        return self.inOrderHelper(self.root)

    def inOrderHelper(self, node):
        if not node:
            return
        self.inOrderHelper(node.left)
        print(node.val)
        self.inOrderHelper(node.right)
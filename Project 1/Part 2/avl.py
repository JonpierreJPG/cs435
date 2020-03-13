# Jonpierre Grajales
# Project 1 Part 2

import node as node

class AVL:
    def __init__(self, rootval):
        if rootval == None:
            self.root = None
        else:
            self.root = node.Node(rootval)
        self.traversecount = 0

    def balanceFactor(self, node):
        if node.right and not node.left:
            return 0 - node.right.height
        elif not node.right and node.left:
            return node.left.height
        elif not node.right and not node.right:
            return 0
        return node.left.height - node.right.height

    def setHeight(self, node):
        while node:
            if not node.left and not node.right:
                node.height = 1
            elif node.left and not node.right:
                node.height = node.left.height + 1
            elif not node.left and node.right:
                node.height = node.right.height + 1
            else:
                node.height = max(node.left.height, node.right.height) + 1
            node = node.parent

    def balance(self, node):
        while node:
            if self.balanceFactor(node) > 1 and self.balanceFactor(node.left) > 0:
                self.leftleft(node)
               
            elif self.balanceFactor(node) > 1 and self.balanceFactor(node.left) < 0:
                self.leftright(node)
                
            elif self.balanceFactor(node) < -1 and self.balanceFactor(node.right) > 0:
                self.rightleft(node)
                
            elif self.balanceFactor(node) < -1 and self.balanceFactor(node.right) < 0:
                self.rightright(node)
            
            node = node.parent

    def leftleft(self, node):
        newroot = node.left
        parent = node.parent
        if node.left.right:
            store = node.left.right
            store2 = node.right
            newroot.right = node.Node(node.val)
            newroot.right.parent = node.left
            if parent:
                if parent.left == node:
                    parent.left = newroot
                    newroot.parent = parent
                elif parent.right == node:
                    parent.right = newroot
                    newroot.parent = parent
                    
            else:
                newroot.parent = None
            newroot.right.left = store
            if store:
                store.parent = newroot.right
            newroot.right.right = store2
            if store2:
                store2.parent = newroot.right
            node.left = None
            node.right = None
            
        else:
            store2 = node.right
            newroot.right = node.Node(node.val)
            newroot.right.parent = node.left
            if parent:
                if parent.right == node:
                    parent.right = newroot
                    newroot.parent = parent
                elif parent.left == node:
                    parent.left = newroot
                    newroot.parent = parent
                    
            newroot.right.right = store2
            
            if store2:
                store2.parent = newroot.right
            node.left = None
            node.parent = None
            
        self.setHeight(newroot.right)
        
        if newroot:
            newroot.parent = parent
            if not newroot.parent:
                self.root = newroot

    def leftright(self, node):
        leftnode = node.left
        parent = leftnode.parent
        if leftnode.right:
            store = leftnode.right.left
            store2 = leftnode.left
            newroot = leftnode.right
            
            if parent:
                if parent.left == leftnode:
                    parent.left = newroot
                    newroot.parent = parent
                elif parent.right == leftnode:
                    parent.right = newroot
                    newroot.parent = parent
                    
            node.left = newroot
            newroot.parent = node
            leftnode.parent = None
            leftnode.right = None
            newroot.left = node.Node(leftnode.val)
            newroot.left.parent = newroot
            newroot.left.left = store2
            if store2:
                store2.parent = newroot.left
            newroot.left.right = store
            if store:
                store.parent = newroot.left
        self.leftleft(node)

    def rightright(self, node):
        newroot = node.right
        parent = node.parent
        if node.right.left:
            store = node.right.left
            store2 = node.left
            newroot.left = node.Node(node.val)
            newroot.left.parent = node.right
            
            if parent:
                if parent.left == node:
                    parent.left = newroot
                    newroot.parent = parent
                elif parent.right == node:
                    parent.right = newroot
                    newroot.parent = parent
                    
            else:
                newroot.parent = None
            newroot.left.right = store
            if store:
                store.parent = newroot.left
            newroot.left.left = store2
            if store2:
                store2.parent = newroot.left
            node.right = None
            node.left = None
            
        else:
            store2 = node.left
            newroot.left = node.Node(node.val)
            newroot.left.parent = node.right
            if parent:
                if parent.right == node:
                    parent.right = newroot
                    newroot.parent = parent
                elif parent.left == node:
                    parent.left = newroot
                    newroot.parent = parent
                    
            newroot.left.left = store2
            
            if store2:
                store2.parent = newroot.left
            node.right = None
            node.parent = None
        self.setHeight(newroot.left)
        
        if newroot:
            newroot.parent = parent
            if not newroot.parent:
                self.root = newroot

    def rightleft(self, node):
        leftnode = node.right
        parent = leftnode.parent
        if leftnode.left:
            store = leftnode.left.right
            store2 = leftnode.right
            newroot = leftnode.left
            if parent:
                if parent.left == leftnode:
                    parent.left = newroot
                    newroot.parent = parent
                elif parent.right == leftnode:
                    parent.right = newroot
                    newroot.parent = parent
                    
            node.right = newroot
            newroot.parent = node
            leftnode.parent = None
            leftnode.left = None
            newroot.right = node.Node(leftnode.val)
            newroot.right.parent = newroot
            newroot.right.right = store2
            
            if store2:
                store2.parent = newroot.right
            newroot.right.left = store
            if store:
                store.parent = newroot.right
        self.rightright(node)

    def insertIter(self, val):
        node = self.root
        levelcount = 1
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
                self.setHeight(node)
                self.balance(node)
                return node.left
                
            if node.right:
                node = node.right
                self.traversecount += 1
                continue
            node.right = node.Node(val)
            node.right.parent = prev
            self.setHeight(node)
            self.balance(node)
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
                self.setHeight(node.parent)
                self.balance(node.parent)
            else:
                node.parent.right = None
                self.setHeight(node.parent)
                self.balance(node.parent)
        elif node.left and not node.right:
            if node == self.root:
                self.root = node.left
                self.root.parent = None
                self.setHeight(self.root)
                self.balance(self.root)
            else:
                self.jumpLeft(node)
        elif node.right and not node.left:
            if node == self.root:
                self.root = node.right
                self.root.parent = None
                self.setHeight(self.root)
                self.balance(self.root)
            else:
                self.jumpRight(node)
        else:
            next = self.finodeNextIter(node)
            node.val = next.val
            if next.isLeaf():
                if next.parent.right == next:
                    next.parent.right = None
                else:
                    next.parent.left = None
                self.setHeight(next.parent)
                self.balance(next.parent)
            elif next.left and next.right:
                next.parent.right = next.right
                next.parent.right.parent = next.parent
                store = next.left
                newnode = next.parent.right
                while newnode.left:
                    newnode = newnode.left
                newnode.left = store
                store.parent = newnode
                self.setHeight(store)
                self.balance(store)
            elif next.left:
                self.jumpLeft(next)
            elif next.right:
                self.jumpRight(next)
        
    def jumpLeft(self, node):
        if node.parent.left == node:
            node.parent.left = node.left
            node.parent.left.parent = node.parent
            self.setHeight(node.parent.left)
            self.balance(node.parent.left)
            
        elif node.parent.right == node:
            node.parent.right = node.left
            node.parent.right.parent = node.parent
            self.setHeight(node.parent.right)
            self.balance(node.parent.right)
    
    def jumpRight(self, node):
        if node.parent.left == node:
            node.parent.left = node.right
            node.parent.left.parent = node.parent
            self.setHeight(node.parent.left)
            self.balance(node.parent.left)
            
        elif node.parent.right == node:
            node.parent.right = node.right
            node.parent.right.parent = node.parent
            self.setHeight(node.parent.right)
            self.balance(node.parent.right)


    def finodeNextIter(self, node):
        val = node.val
        if val == self.finodeMaxIter().val:
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

    def finodePrevIter(self, node):
        val = node.val
        if val == self.finodeMinIter().val:
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

    def finodeMaxIter(self):
        node = self.root
        while node.right:
            node = node.right
        return node

    def finodeMinIter(self):
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
        print(node.val, node.height)
        self.inOrderHelper(node.right)

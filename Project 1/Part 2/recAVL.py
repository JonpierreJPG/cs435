# Jonpierre Grajales
# Project 1 Part 2

class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def isLeaf(self):
        return not self.left and not self.right

class recAVL:
    def __init__(self, rootval):
        if rootval == None:
            self.root = None
        else:
            self.root = nd.Node(rootval)

    def getHeight(self, node):
        if node is None:
            return 0
        
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)

        if (leftHeight > rightHeight):
            return leftHeight + 1
        return rightHeight + 1

    def getBalance(self, node):
        if node.right and not node.left:
            return 0 - self.getHeight(node.right)
            
        elif not node.right and node.left:
            return self.getHeight(node.left)
            
        elif not node.right and not node.right:
            return 0
            
        return self.getHeight(node.left) - self.getHeight(node.right)

    def balance(self, node):
        while node:
            if self.getBalance(node) > 1 and self.getBalance(node.left) > 0:
                self.leftleft(node)
                
            elif self.getBalance(node) > 1 and self.getBalance(node.left) < 0:
                self.leftright(node)
                
            elif self.getBalance(node) < -1 and self.getBalance(node.right) < 0:
                self.rightright(node)
                
            elif self.getBalance(node) < -1 and self.getBalance(node.right) > 0:
                self.rightleft(node)
            node = node.parent

    def leftleft(self, node):
        newroot = node.left
        parent = node.parent
        if node.left.right:
            temp = node.left.right
            temp2 = node.right
            newroot.right = Node(node.val)
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
            newroot.right.left = temp
            if temp:
                temp.parent = newroot.right
            newroot.right.right = temp2
            if temp2:
                temp2.parent = newroot.right
            node.left = None
            node.right = None
        else:
            temp2 = node.right
            newroot.right = Node(node.val)
            newroot.right.parent = node.left
            if parent:
                if parent.right == node:
                    parent.right = newroot
                    newroot.parent = parent
                elif parent.left == node:
                    parent.left = newroot
                    newroot.parent = parent
            newroot.right.right = temp2
            if temp2:
                temp2.parent = newroot.right
            node.left = None
            node.parent = None
        if newroot:
            newroot.parent = parent
            if not newroot.parent:
                self.root = newroot

    def leftright(self, node):
        leftnode = node.left
        parent = leftnode.parent
        if leftnode.right:
            temp = leftnode.right.left
            temp2 = leftnode.left
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
            newroot.left = Node(leftnode.val)
            newroot.left.parent = newroot
            newroot.left.left = temp2
            if temp2:
                temp2.parent = newroot.left
            newroot.left.right = temp
            if temp:
                temp.parent = newroot.left
        self.leftleft(node)
        
def rightleft(self, node):
        leftnode = node.right
        parent = leftnode.parent
        if leftnode.left:
            temp = leftnode.left.right
            temp2 = leftnode.right
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
            newroot.right = Node(leftnode.val)
            newroot.right.parent = newroot
            newroot.right.right = temp2
            if temp2:
                temp2.parent = newroot.right
            newroot.right.left = temp
            if temp:
                temp.parent = newroot.right
        self.rightright(node)

    def rightright(self, node):
        newroot = node.right
        parent = node.parent
        if node.right.left:
            temp = node.right.left
            temp2 = node.left
            newroot.left = Node(node.val)
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
            newroot.left.right = temp
            if temp:
                temp.parent = newroot.left
            newroot.left.left = temp2
            if temp2:
                temp2.parent = newroot.left
            node.right = None
            node.left = None
        else:
            temp2 = node.left
            newroot.left = Node(node.val)
            newroot.left.parent = node.right
            if parent:
                if parent.right == node:
                    parent.right = newroot
                    newroot.parent = parent
                elif parent.left == node:
                    parent.left = newroot
                    newroot.parent = parent
            newroot.left.left = temp2
            if temp2:
                temp2.parent = newroot.left
            node.right = None
            node.parent = None
        if newroot:
            newroot.parent = parent
            if not newroot.parent:
                self.root = newroot

    def insertRec(self, val):
        return self.insertRecHelper(val, self.root, None, False)

    def insertRecHelper(self, val, node, prev, l):
        if not node:
            if self.root == None:
                self.root = Node(val)
                return
            if l:
                prev.left = Node(val)
                prev.left.parent = prev
                self.balance(prev)
                return prev.left
            prev.right = Node(val)
            prev.right.parent = prev
            self.balance(prev)
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
                    self.balance(node.parent)
                else:
                    node.parent.right = None
                    self.balance(node.parent)
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
                self.balance(node.parent)
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
                self.balance(node.parent)
            else:
                suc = self.findNextRec(node)
                node.val = suc.val
                self.deleteRecHelper(suc.val, node.right, False)

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

    def inOrder(self):
        print("INORDER TRAVERSAL")
        return self.inOrderHelper(self.root)

    def inOrderHelper(self, node):
        if not node:
            return
        self.inOrderHelper(node.left)
        print(node.val)
        self.inOrderHelper(node.right)

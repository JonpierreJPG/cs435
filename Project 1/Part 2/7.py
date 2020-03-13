# Jonpierre Grajales
# Project 1 Part 2

import node as node
import genarray as gen
import bst as bst
import avl as avl
from datetime import datetime

avl = avl.AVL(None)
bst = bst.BST(None)
array = gen.getSortedArray(10000)
now = datetime.now()
FMT = '%H:%M:%S'

print("Creating BST, PLEASE WAIT")
bstStart = now.strftime("%H:%M:%S")

for val in array:
    bst.insertIter(val)

for val in array:
    bst.deleteIter(val)
    
now = datetime.now()
bstFinish = now.strftime("%H:%M:%S")

BSTtdelta = datetime.strptime(bstStart, FMT) - datetime.strptime(bstFinish, FMT)
print("BST runtime was: ", BSTtdelta, "seconds")

print("Creating AVL, PLEASE WAIT")
now = datetime.now()
avlStart = now.strftime("%H:%M:%S")

for val in array:
    avl.insertIter(val)

for val in array:
    avl.deleteIter(val)

now = datetime.now()
avlFinish = now.strftime("%H:%M:%S")

AVLtdelta = datetime.strptime(avlStart, FMT) - datetime.strptime(avlFinish, FMT)
print("AVL runtime was: ", AVLtdelta, "seconds")

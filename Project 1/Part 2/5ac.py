import node as node
import genarray as gen
import bst as bstt
import avl as avlt
from datetime import datetime

avl = avlt.AVL(None)
bst = bstt.BST(None)
array = gen.getRandomArray(10000)

print("RECURSIVE RUNNING...")
for val in array:
    avl.insertIter(val)
    bst.insertRec(val)
print("RECURSIVE DONE!")


avl = avlt.AVL(None)
bst = bstt.BST(None)
array = gen.getRandomArray(10000)

print("ITERATIVE RUNNING...")
for val in array:
    avl.insertIter(val)
    bst.insertIter(val)
print("ITERATIVE DONE!")

# Jonpierre Grajales
# Project 1 Part 2

import node as node
import genarray as gen
import bst as bstt
import avl as avlt

avl = avlt.AVL(None)
bst = bstt.BST(None)
array = gen.getRandomArray(10000)

print("RANDOM ARRAY")
for val in array:
    avl.insertIter(val)
    bst.insertIter(val)

print('BST total traverses: %s' % bst.traversecount)
print('AVL total traverses: %s' % avl.traversecount)


avl = avlt.AVL(None)
bst = bstt.BST(None)
array = gen.getSortedArray(10000)

print('\nSORTED ARRAY')
for val in array:
    avl.insertIter(val)
    bst.insertIter(val)

print('BST total traverses: %s' % bst.traversecount)
print('AVL total traverses: %s' % avl.traversecount)

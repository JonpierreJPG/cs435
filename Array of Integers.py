# Jonpierre Grajales
# Professor Rengesh
# CS 435
# Project 1 - Part 1
import random

def getRandomArray(n):
  array = []

  while len(array) < n:
    num = random.randint(-100, 100)

    if num not in array:
      array.append(num)

  return array

def getSortedRand(array):
  array.sort()
  return array

def getSortedArray(n):
  return [x for x in range(n, 0, -1)]

array = []
array = getRandomArray(10)
print(array)

sortedRand = getSortedRand(array)
print(sortedRand)

sortedArray = getSortedArray(random.randint(5, 40))
print(sortedArray)


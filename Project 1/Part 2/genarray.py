import random

def getRandomArray(n):
    array = []
    
    while len(array) < n:
        num = random.randint(0, n*10)
        if num not in array:
            array.append(num)
            
    return array

def getSortedArray(n):
    return [array.sort()]
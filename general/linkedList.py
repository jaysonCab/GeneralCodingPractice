'''
READ - O(n)
INSERT - O(1)
DELETE - O(1)
'''

# class linkedListNode:
#     def __init__ (self, value, nextNode = None):
#         self.value = value
#         self.nextNode = nextNode

# node1 = linkedListNode('3')
# node2 = linkedListNode('7')
# node3 = linkedListNode('10')
# currentNode = node1

# node1.nextNode = node2
# node2.nextNode = node3

# while True:
#     print(f'{currentNode.value} --> ')

#     if currentNode.nextNode is None:
#         break

#     currentNode = currentNode.nextNode

# print(currentNode)






# class LinkedListNode():
#     def __init__(self, value, nextNode = False):
#         self.value = value
#         self.nextNode = nextNode

# point1 = LinkedListNode(1)
# point2 = LinkedListNode(2)
# point3 = LinkedListNode(3)

# point1.nextNode = point2
# point2.nextNode = point3

# # Dont forget to innitialize what is the first node, kind of like DummyNode
# currentNode = point1
# values = []

# while currentNode:
#     values.append(currentNode.value)
#     currentNode = currentNode.nextNode

# print(values)


# ------------------------------------ DECEMBER 19th
# class linkedListNode():

#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next

# node1 = linkedListNode(5)
# node2 = linkedListNode(10)
# node3 = linkedListNode(15)

# origin = node1

# node1.next = node2
# node2.next = node3

# while origin:
#     print(origin.value)
#     origin = origin.next

# ---------------------------------------------------------------------
# December 20th, 2024

# class linkedListNode():
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next

# node1 = linkedListNode(1)
# node2 = linkedListNode(3)
# node3 = linkedListNode(2)

# currentNode = node1

# node1.next = node2
# node2.next = node3

# newList = []

# while currentNode:
#     newList.append(currentNode.value)
#     currentNode = currentNode.next

# print(newList)

# ----------------------------------------------------

# class linkedListNode():

#     def __init__(self, value, next = False):
#         self.value = value
#         self.next = next

# node1 = linkedListNode(93)
# node2 = linkedListNode(12)
# node3 = linkedListNode(34)
# node4 = linkedListNode('Chicken')

# currentNode = node1
# node1.next = node2
# node2.next = node3
# node3.next = node4

# listing = []

# while currentNode:
#     listing.append(currentNode.value)
#     currentNode = currentNode.next

# print(listing)

# ----------------------------------------------------

# class LinkedListNode():
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next

# node1 = LinkedListNode(1)
# node2 = LinkedListNode(3)
# node3 = LinkedListNode(5)

# node1.next = node2
# node2.next = node3

# currentNode = node1
# listing = []

# while currentNode:
#     listing.append(currentNode.value)
#     currentNode = currentNode.next

# print(listing)

# -----------------------------------------------
# December 21st, 2024

# class LinedListNode():
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next

# node1 = LinedListNode(1)
# node2 = LinedListNode(3)
# node3 = LinedListNode(6)

# currentNode = node1

# node1.next = node2
# node2.next = node3
# newList = []

# while currentNode:
#     newList.append(currentNode.value)
#     currentNode = currentNode.next

# print(newList)

# ------------------------------------------------------------------------

# class LinkedListNode():
#     def __init__(self, value, next = False):
#         self.value = value
#         self.next = next

# node1 = LinkedListNode(1)
# node2 = LinkedListNode(3)
# node3 = LinkedListNode(5)

# currentNode = node1

# node1.next = node2
# node2.next = node3
# listing = []

# while currentNode:
#     listing.append(currentNode.value)
#     currentNode = currentNode.next

# print(listing)

# --------------------------------------------------------------------------------------

# class LinkedListNode():
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next
    
# node1 = LinkedListNode(25)
# node2 = LinkedListNode(1)
# node3 = LinkedListNode(54)

# node1.next = node2
# node2.next = node3

# currentNode = node1
# listing = []

# while currentNode:
#     listing.append(currentNode.value)
#     currentNode = currentNode.next

# print(listing)

# ------------------------------------------------------------------------------------------
# December 22nd, 2024

# class LinkedListNode():
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next

# node1 = LinkedListNode(2)
# node2 = LinkedListNode(34)
# node3 = LinkedListNode(28)

# node1.next = node2
# node2.next = node3

# currentNode = node1
# listing = []

# while currentNode:
#     listing.append(currentNode.value)
#     currentNode = currentNode.next

# print(listing)

# --------------------------------------------------------------------------------------------

# class LinkedListNode():
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next

# node1 = LinkedListNode(10)
# node2 = LinkedListNode(20)
# node3 = LinkedListNode(30)

# node1.next = node2
# node2.next = node3

# currentNode = node1
# listing = []

# while currentNode:
#     listing.append(currentNode.value)
#     currentNode = currentNode.next

# print(listing)

# -------------------------------------------------------------------------------------------
# December 24th, 2024

# class LinkedListNode():
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next

# node1 = LinkedListNode(1)
# node2 = LinkedListNode(4)
# node3 = LinkedListNode(8)

# node1.next = node2
# node2.next = node3

# currnetNode = node1
# listing = []

# while currnetNode:
#     listing.append(currnetNode.value)
#     currnetNode = currnetNode.next

# print(listing)

# -------------------------------------------------------------------------------------------
# January 6th, 2025

# SORTING A LINKED LIST
# class LinkedListNode():
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next

# node1 = LinkedListNode(5)
# node2 = LinkedListNode(1)
# node3 = LinkedListNode(8)

# current = node1

# node1.next = node2
# node2.next = node3
# array = []

# while current:
#     array.append(current.value)
#     current = current.next

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1
        
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
        
#         return array

# sortedArray = mergeSort(array)
# current = node1

# i = 0
# while current:
#     current.value = sortedArray[i]
#     i += 1
#     current = current.next
# current = node1

# while current:
#     print(current.value)
#     current = current.next

# -------------------------------------------------------------------------------------------------------------------

# SORTING A LINKED LIST
# class LinkedListNode():
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next

# node1 = LinkedListNode(5)
# node2 = LinkedListNode(1)
# node3 = LinkedListNode(8)

# current = node1

# node1.next = node2
# node2.next = node3
# array = []

# while current:
#     array.append(current.value)
#     current = current.next

# array.sort()
# current = node1

# i = 0
# while current:
#     current.value = array[i]
#     i += 1
#     current = current.next
# current = node1

# while current:
#     print(current.value)
#     current = current.next

# ------------------------- May 31st, 2025
class linkedListNode():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

node1 = linkedListNode(3)
node2 = linkedListNode(5)
node3 = linkedListNode(19)

current = node1

node1.next = node2
node2.next = node3

while current:
    print(current.value)
    current = current.next

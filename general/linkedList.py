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


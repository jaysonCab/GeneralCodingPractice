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



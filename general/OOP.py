'''
__init__ is a special operator, when creating an object, __init__ is expected argumenets to be given
If no __init__, they are just regular methods
'''

# class human:
#     def __init__(self, name, nextPosition = None):
#         self.name = name
#         self.nextPosition = nextPosition

#     def noise(self):
#         print('BARK')

# human1 = human('Sheesh')
# human1.nextPosition = '22'
# print(human1.name)
# print(human1.nextPosition)

# human1.noise()

# current = human1
# print(current)

# -------------------------------------------------------------------

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

# -------------------------------------------------------------------

# class human():
#     def __init__(self, shape):
#         self.shape = shape
#         print(self.shape)

#     def barking(self):
#         print('Bark')

# human1 = human('Fat')

# human1.barking()

# -------------------------------------------------------------------

# class linkedList():

#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next
    
# node1 = linkedList(5)
# node2 = linkedList('Beef')
# node3 = linkedList((3,4,5))

# node1.next = node2
# node2.next = node3

# currentNode = node1
# listers = []

# while currentNode:
#     listers.append(currentNode.value)
#     currentNode = currentNode.next

# print(listers)

# ------------------------------------

# class banking():
#     def addition(self, inputMoney):
#         self.inputMoney = inputMoney
#         self.__balance = inputMoney * 2
#         print(self.__balance)

# bank1 = banking()
# bank1.addition(900)
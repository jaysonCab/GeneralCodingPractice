# Dec 8th, 2024

# STACK -----------------------------------------------------------------
'''
Important information about stacks is the ability to push an element onto the stack
    --> stackList.append(VARIABLE)
Also pop an element from a stack | This will return something so you can assign
    --> element = stacList.pop()
        eg: print(element)

FILO: Append and Pop with no pop parameter, will remove the most recent entry or last item in the list
'''


    # PLAYING WITH SIMPLE STACK
# stackList = []
# stackList.append(5)
# stackList.append(10)
# stackList.append(15)
# print(stackList)

# element = stackList.pop()
# print(stackList)
# print(element)


    # LOOKING AT LAST ELEMENT
# stackList = [1,2,3,4,5]
# print(stackList[-1])


# QUEUE -----------------------------------------------------------------
'''
A queue is basically the same as a stack but instead of leaving the pop() blank, you pass in the parameter 0
The problem when you pop from the front, is that every item in the list needs to move up one spot so it is O(n)
To fix this, try and from collections import deque
    Regular library is called collections
'''


#    # Simple append and pop(0) in a queue
# stackList = []
# stackList.append(5)
# stackList.append(10)
# stackList.append(15)
# print(stackList)

# element = stackList.pop(0)
# print(f'The stackList is {stackList} and the popped element is {element}')


#    # Avoids having to move the entire list if something is popped at position 0
# from collections import deque
# data = deque('123512416243')

# data.append('5')
# data.popleft

# print(list(data))

# December 27th, 2024 | I just want to pop from the front again
queue = [1,2,3,4]
nice = queue.pop(0)

print(nice)
print(queue)

# CUSTOM STACK AND QUEUE CLASSES -----------------------------------------------------------------
'''
Simple class and object creation
Placing a variable with an underscore means it is meant to be private
'''

# class Stack:
#     def __init__(self):
#         self._data = []

#     def push(self, data):
#         self._data.append(data)
#         print(self._data)

#     def pop(self):
#         return self._data.pop()
    
#     def peek(self):
#         return self._data[-1]
    
# stack1 = Stack()
# stack1.push(10)
# stack1.push(20)
# stack1.push(30)

# elementPeek = stack1.peek()
# print(elementPeek)

# element = stack1.pop()

# print(element)
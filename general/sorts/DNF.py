# December 22nd, 2024 -- Jayson's attempt at DNF

# def dnf(array):
#     lowPointer = 0
#     midPointer = 0
#     highPointer = len(array) - 1

#     while midPointer <= highPointer:
#         if array[midPointer] == 2:
#             array[midPointer], array[highPointer] = array[highPointer], array[midPointer]
#             highPointer -= 1
#             if array[midPointer] != 0:
#                 midPointer += 1
#         elif array[midPointer] == 0:
#             array[midPointer], array[lowPointer] = array[lowPointer], array[midPointer]
#             lowPointer += 1
#             midPointer += 1
#         else:
#             midPointer += 1
    
#     return array

# print(dnf([0, 1, 2]))

# WAIT IT'S LIKE IM KIND OF THE GOAT || Nvm all use cases didn't work

# ---------------------------------------------------------------------------------------

# def dnf(array):
#     lowPointer = 0
#     midPointer = 0
#     highPointer = len(array) - 1

#     while midPointer <= highPointer:
#         if array[midPointer] == 2:
#             array[midPointer], array[highPointer] = array[highPointer], array[midPointer]
#             highPointer -= 1
        
#         elif array[midPointer] == 1:
#             midPointer += 1

#         else:
#             array[midPointer], array[lowPointer] = array[lowPointer], array[midPointer]
#             lowPointer += 1
#             midPointer += 1

#     return array

# print(dnf([2, 1, 2]))

# -------------------------------------------------------------------------------------

# def DutchNationalFlag(array):
#     lowPointer = 0
#     midPointer = 0
#     highPointer = len(array) - 1

#     while midPointer <= highPointer:
        
#         match array[midPointer]:
#             case 2:
#                 array[midPointer], array[highPointer] = array[highPointer], array[midPointer]
#                 highPointer -= 1
            
#             case 0:
#                 array[midPointer], array[lowPointer] = array[lowPointer], array[midPointer]
#                 lowPointer += 1
#                 midPointer += 1

#             case 1:
#                 midPointer += 1

#     return array

# print(DutchNationalFlag([1,0,0,2,1,2,2, 1, 2]))

# -----------------------------------------------------------------------------------------

# def DutchNationalFlag(array):
#     lowPointer = 0
#     midPointer = 0
#     highPointer = len(array) - 1

#     while midPointer <= highPointer:
#         match array[midPointer]:
#             case 2:
#                 array[midPointer], array[highPointer] = array[highPointer], array[midPointer]
#                 highPointer -= 1

#             case 0:
#                 array[midPointer], array[lowPointer] = array[lowPointer], array[midPointer]
#                 midPointer += 1
#                 lowPointer += 1

#             case 1:
#                 midPointer += 1

#     return array

# print(DutchNationalFlag([1,0,0,2,1,2,2, 1, 2]))

# ----------------------------------------------------------------------------------------
# December 23rd, 2024

# def DNF(array):
#     lowPosition = 0
#     midPosition = 0
#     highPosition = len(array) - 1

#     while midPosition <= highPosition:

#         match array[midPosition]:
#             case 2:
#                 array[midPosition], array[highPosition] = array[highPosition], array[midPosition]
#                 highPosition -= 1

#             case 0:
#                 array[midPosition], array[lowPosition] = array[lowPosition], array[midPosition]
#                 lowPosition += 1
#                 midPosition += 1

#             case 1:
#                 midPosition += 1

#     return array

# print(DNF([1,0,0,2,1,2,2, 1, 2]))

# ----------------------------------------------------------------------------------------------

# def DNF(array):
#     lowPosition = 0
#     midPosition = 0
#     highPosition = len(array) - 1

#     while midPosition <= highPosition:
#         match array[midPosition]:
#             case 2:
#                 array[midPosition], array[highPosition] = array[highPosition], array[midPosition]
#                 highPosition -= 1

#             case 0:
#                 array[midPosition], array[lowPosition] = array[lowPosition], array[midPosition]
#                 lowPosition += 1
#                 midPosition += 1
            
#             case 1:
#                 midPosition += 1

#     return array

# print(DNF([1,0,0,2,1,2,2, 1, 2]))

# ----------------------------------------------------------------------------------------------
# December 24th, 2024

# def DNF(array):
#     left = 0
#     middle = 0
#     right = len(array) - 1

#     while middle <= right:
#         match array[middle]:
#             case 2:
#                 array[middle], array[right] = array[right], array[middle]
#                 right -= 1
#             case 0:
#                 array[middle], array[left] = array[left], array[middle]
#                 left += 1
#                 middle += 1
#             case 1:
#                 middle += 1
    
#     return array

# print(DNF([1,0,0,2,1,2,2, 1, 2]))

# -----------------------------------------------------------------------------------------------

# def DNF(array):
#     lowPosition = 0
#     midPoisition = 0
#     highPosition = len(array) - 1

#     while midPoisition <= highPosition:
#         match array[midPoisition]:
#             case 2:
#                 array[midPoisition], array[highPosition] = array[highPosition], array[midPoisition]
#                 highPosition -= 1

#             case 0:
#                 array[midPoisition], array[lowPosition] = array[lowPosition], array[midPoisition]
#                 midPoisition += 1
#                 lowPosition += 1

#             case 1:
#                 midPoisition += 1

#     return array

# print(DNF([1,0,0,2,1,2,2, 1, 2]))

# -------------------------------------------------------------------------------------------















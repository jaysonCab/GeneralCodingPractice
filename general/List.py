# February 4th, 2025

# Rotate to the right 4 positions
list = [1,2,3,4,5,6,7,8]
k = 4

def rotate(left, right):
    while left < right:
        list[left], list[right] = list[right], list[left]
        left += 1
        right -= 1

left, right = 0, len(list) - 1
rotate(left, right)

left, right = 0, k - 1
rotate(left, right)

left, right = k, len(list) - 1
rotate(left, right)

print(list)
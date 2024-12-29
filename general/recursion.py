# December 27th, 2024

# def walk(stepCount):
#     if stepCount != 0:
#         walk(stepCount-1)
#         print(f'Youve taken {stepCount} number of steps')

#     else:
#         return
    
# walk(100)

# ------------------------------------------------------------------------
# Sum all non negative numbers 

# def summation(number):
#     if number >= 1:
#         return number + summation(number - 1)
#     else:
#         return number

# print(summation(5))

# ------------------------------------------------------------------------

# def fibbonacci(index):
#     if index <= 0:
#         return 0
#     elif index == 1:
#         return 1
#     else:
#         return fibbonacci(index-2) + fibbonacci(index-1)
    
# print(fibbonacci(3))

# -------------------------------------------------------------------------


'''
RECURSION BACKTRACKING
Exhaustive search, brute force technique. If you want to see ALL solutions?
    Subset leetcode question

Subsets is difficult, maybe have to do tree traversal problems first
'''
# December 29th, 2024

def subsets(nums):
    #always start with res and sol for recursive backtracking questions for the most part
    #result is what is returned at the end, and solution is one at a time
    res, sol = [], []
    
    def backtrack(index):
        # base case, like a leaf node
        if index == len(nums):
            res.append(sol[:])
            return

        # if it isn't a leaf node, dont pick nums[i]
        backtrack(index+1)

        # pick nums[i]
        sol.append(nums[index])
        backtrack(index+1)
        sol.pop()

    backtrack(0)
    return res

print(subsets([1,2,3]))
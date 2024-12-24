'''
Sliding windows are substrings or sub arrays
They need to be contiguous, no skipping or empty spaces
So I guess kadanes algorithm can be considered an array sliding window problem
'''

# December 23rd, Jayson Try on Own Sliding Window Substring
# Beat 6.85% of pepole, obviously slow

# def substring(string):
#     biggest = 0
#     current = 0
#     setting = set()
    
#     for i in range(len(string)): # i is left

#         for j in range(i, len(string)):
#             if string[j] not in setting: # j is right
#                 current = (j-i) + 1
#                 if current > biggest:
#                     biggest = current
                
#                 setting.add(string[j])
#             else:
#                 setting.clear()
#                 break
    
#     return biggest

# string = "abcabcbb"
# print(substring(string))

# -------------------------------------------------------------------------------------------

# def longestSubstring(string):
#     left = 0
#     totalLongest = 0
#     sett = set()

#     for i in range(len(string)):

#         # If item is in sett, therefore it is invalid
#         while string[i] in sett:

#             # Remove the item at value left
#             sett.remove(string[left])
#             left += 1

#         # If item is not in sett, then its valid!
#         currentLongest = (i - left) + 1
#         totalLongest = max(currentLongest, totalLongest)
#         sett.add(string[i])
    
#     return totalLongest

# string = "pwwkew"
# print(longestSubstring(string))

# -------------------------------------------------------------------------------------------
# Proper solution, previous was not O(n)

# def slidingWindow(array):
#     left = 0
#     totalMaximum = 0
#     sett = set()

#     for right in range(len(array)):
#         while array[right] in sett:
#             sett.remove(array[right])
#             left += 1
        
#         currentMaximum = right - left + 1
#         totalMaximum = max(currentMaximum, totalMaximum)
#         sett.add(array[right]) 
    
#     return totalMaximum

# string = "abcabcbb"
# print(slidingWindow(string))

# -------------------------------------------------------------------------------------

# def greatestSegment(array):
#     left = 0
#     maxTotal = 0
#     sett = set()

#     for right in range(len(array)):
#         while array[right] in sett:
#             sett.remove(array[left])
#             left += 1

#         currentMax = (right - left) + 1
#         maxTotal = max(currentMax, maxTotal)
#         sett.add(array[right])

#     return maxTotal

# string = "pwwkew"
# print(greatestSegment(string))

# ---------------------------------------------------------------------------------------------

# def greatestSegment(array):
#     left = 0
#     maxTotal = 0
#     sett = set()

#     for right in range(len(array)):
#         while array[right] in sett:
#             sett.remove(array[left])
#             left += 1

#         currentTotal = right - left + 1
#         maxTotal = max(currentTotal, maxTotal)
#         sett.add(array[right])

#     return maxTotal

# string = "pwwkew"
# print(greatestSegment(string))

# -----------------------------------------------------------------------------------------------

# def slidingWindow(array):
#     left = 0
#     maxTotal = 0
#     sett = set()

#     for right in range(len(array)):
#         while array[right] in sett:
#             sett.remove(array[left])
#             left += 1
        
#         currentTotal = right - left + 1
#         maxTotal = max(currentTotal, maxTotal)
#         sett.add(array[right])

#     return maxTotal

# string = "pwwkew"
# print(slidingWindow(string))

# ------------------------------------------------------------------------------------------------
# December 24th, 2024

# def slidingWindow(array):
#     left = 0
#     maxTotal = 0
#     sett = set()

#     for right in range(len(array)):
#         while array[right] in sett:
#             sett.remove(array[left])
#             left += 1

#         currentTotal = right - left + 1
#         maxTotal = max(currentTotal, maxTotal)
#         sett.add(array[right])

#     return maxTotal

# string = "pwwkew"
# print(slidingWindow(string))

# ------------------------------------------------------------------------------------------------

# def slidingWindow(array):
#     left = 0
#     maxTotal = float('-inf')
#     sett = set()

#     for right in range(len(array)):
#         while array[right] in sett:
#             sett.remove(array[left])
#             left += 1

#         currentTotal = right - left + 1
#         maxTotal = (currentTotal, maxTotal)
#         sett.add(array[right])

#     return maxTotal        

# -------------------------------------------------------------------------------------------














# -------------------------------------------------------------------------------------------------

'''
PREVIOUS WAS WITH A VARIABLE LENGTH WINDOW
THIS IS WITH A CONSTANT WINDOW
'''

# -------------------------------------------------------------------------------------------------
# December 24th, 2024

# def slidingWindow(nums, k):
#     total = 0

#     for i in range(k):
#         total += nums[i]

#     maxAverage = total / k

#     for i in range(k, len(nums)):
#         total += nums[i]
#         total -= nums[i-k]

#         average = total / k
#         maxAverage = max(average, maxAverage)

#     return maxAverage

# nums = [1,12,-5,-6,50,3]
# k = 4
# print(slidingWindow(nums,k))

# ----------------------------------------------------------------------------------------

'''
https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python/606c0aead051520044f094db

2. Find the odd int 
Given an list of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

Example 1:
Input: [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
Output: 5

Example 2:
Input: [1,1,2,-2,5,2,4,4,-1,-2,5]
Output: -1

Example 3:
Input: [10]
Output: 10
'''    

def find_it(nums):
  for i in nums:
    if nums.count(i) % 2 != 0:
      return i
    
nums = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(find_it(nums))
nums = [1,1,2,-2,5,2,4,4,-1,-2,5]
print(find_it(nums))
nums = [1,1,2,-2,5,2,4,4,-1,-2,5]
print(find_it(nums))

nums = [1,1,2,-2,5,2,4,4,-1,-2,5]
print(find_it(nums))

'''
https://leetcode.com/problems/two-sum/
3. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''    

# def two_sum(nums, target):
#   # I != J, because it says bring 2 nums
#   for i in range(len(nums)):
#     # cannot use the same index twice
#     for j in range(len(nums)):
#       # nums[i] + nums[j] == target
#       if i != j and nums[i] + nums[j] == target:
#         return [i, j]

def two_sum(nums, target):
  table = {}
  for i, num in enumerate(nums):
    # target - num = who would match us
    match_buddy = target - num
    if match_buddy not in table:
      table[num] = i
    else:
      return [table[match_buddy], i]


nums = [2,7,11,15]
target = 9
print(two_sum(nums, target))
nums = [3,2,4]
target = 6
print(two_sum(nums, target))
nums = [3,3]
target = 6
print(two_sum(nums, target))
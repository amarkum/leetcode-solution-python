"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            required_number = target - nums[i]
            for j in range(i + 1, len(nums)):
                if required_number == nums[j]:
                    return [i, j]


nums = [2, 7, 11, 15]
target = 9
two_sum = TwoSum()
print(two_sum.twoSum(nums, target))

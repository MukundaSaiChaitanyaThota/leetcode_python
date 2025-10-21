# 2239. Find Closest Number to Zero
# Given an integer array nums of size n, return the number with the smallest absolute value.
# If there are multiple answers, return the largest one.

from typing import List

# Time complexity O(n)
# Space complexity O(1)
def findClosestNumber(nums: List[int]) -> int:
    closest = nums[0]
    for i in range(len(nums)):
        if abs(closest) > abs(nums[i]):
            closest = nums[i]
    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest


if __name__ == "__main__":
    nums1 = [-4,-2,1,4,8]
    print(findClosestNumber(nums1))  # Output: 1

    nums2 = [2,-1,1]
    print(findClosestNumber(nums2))  # Output: 1
# Two sum problem solution
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# solved using two methods: brute force and hashmap
# Brute force method has O(n^2) time complexity - run two nested loops
# Hashmap method has O(n) time complexity - use a dictionary to store the numbers and their indices

from typing import List

#method using brute force
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            
# another method using hashmap
def twoSumHashMap(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i


# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))  # Output: [0, 1]
    print(twoSumHashMap(nums, target))  # Output: [0, 1]
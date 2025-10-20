
# 26. Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

from typing import List

# def removeDuplicates( nums: List[int]) -> int:
#     i=0
#     while i < len(nums):
#         if i<len(nums)-1 and nums[i] == nums[i+1]:
#             nums.pop(i+1)
#             i-=1
#         i+=1
#     return len(nums)

# ANOTHER METHOD
def removeDuplicates( nums: List[int]) -> int:
    if not nums:
        return 0  # Handle empty array case
    j = 0  # Pointer for the position of the last unique element
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return j + 1  # The length is last index + 1

if __name__ == "__main__":
    nums1 = [1,1,2]
    k1 = removeDuplicates(nums1)
    print(k1)  # Output: 2
    print(nums1[:k1])  # Output: [1,2]

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = removeDuplicates(nums2)
    print(k2)  # Output: 5
    print(nums2[:k2])  # Output: [0,1,2,3,4]
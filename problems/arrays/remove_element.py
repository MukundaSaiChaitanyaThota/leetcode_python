# 27. Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
from typing import List

def removeElement( nums: List[int], val: int) -> int:
    j=0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j+=1
    return j


if __name__ == "__main__":
    nums1 = [3,2,2,3]
    val1 = 3
    k1 = removeElement(nums1, val1)
    print(k1)  # Output: 2
    print(nums1[:k1])  # Output: [2,2]

    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    k2 = removeElement(nums2, val2)
    print(k2)  # Output: 5
    print(nums2[:k2])  # Output: [0,1,3,0,4]
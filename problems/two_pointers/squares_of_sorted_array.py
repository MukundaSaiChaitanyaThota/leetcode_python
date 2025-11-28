# 977. Squares of a Sorted Array
# Problem: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

from typing import List

# time complexity: O(n2)
# space complexity: O(n)
def sortedSquares(nums: List[int]) -> List[int]:
    start=0
    end=len(nums)-1
    output=[]
    while start<=end:
        if abs(nums[start]) > abs(nums[end]):
            output.insert(0,nums[start] * nums[start])
            start+=1
        else:
            output.insert(0,nums[end] * nums[end])
            end-=1
    return output

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def sortedSquares(nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1
        result.reverse()

        return result


if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    print(sortedSquares(nums))  # Output: [0,1,9,16,100]

    nums = [-7,-3,2,3,11]
    print(sortedSquares(nums))  # Output: [4,9,9,49,121]
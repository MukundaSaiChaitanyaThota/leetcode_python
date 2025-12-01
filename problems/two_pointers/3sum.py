# 3sum Problem
# Problem: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Note: The solution set must not contain duplicate triplets.

from typing import List

# Time Complexity: O(n^2)
# Space Complexity: O(1) (excluding the space for the output)
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result=[]
    for i in range(len(nums)):
        if nums[i]>0:
            return result
        if i>0 and nums[i]==nums[i-1]:
            continue
        j=i+1
        k=len(nums)-1
        while j<k:
            cur_sum=nums[i]+nums[j]+nums[k]
            if cur_sum==0:
                result.append([nums[i],nums[j],nums[k]])
                j,k=j+1,k-1
                while j<k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k]==nums[k+1]:
                    k-=1
            elif cur_sum<0:
                j+=1
            else:
                k-=1
    return result

if __name__ == "__main__":
    # Example usage:
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]

    nums = [0, 1, 1]
    print(threeSum(nums))  # Output: []
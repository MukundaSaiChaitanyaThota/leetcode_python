# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation


from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    left=[]
    right=[]
    ans=[]
    l_value=1
    r_value=1
    for i in range(len(nums)):
        if i>0:
            l_value*=nums[i-1]
        left.append(l_value)
    for j in range(len(nums),0,-1):
        if j<(len(nums)):
            r_value*=nums[j]
        print(r_value)
        right.insert(0,r_value)
    print(right)
    for k in range(len(nums)):
        ans.append(left[k]*right[k])
    return ans

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(productExceptSelf(nums))  # Output: [24,12,8,6]
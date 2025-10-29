# 228 Summary Ranges 
# You are given a sorted unique integer array nums. A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
# That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b

from typing import List
def summaryRanges( nums: List[int]) -> List[str]:
    start=0
    res=[]
    for i in range(len(nums)):
        if i == len(nums)-1:
            if start==i:
                res.append(f"{nums[start]}")
            else:
                res.append(f"{nums[start]}->{nums[i]}")
            break
        if nums[i+1]==nums[i]+1:
            continue
        else:
            if start==i:
                res.append(f"{nums[start]}")
            else:
                res.append(f"{nums[start]}->{nums[i]}")
            start=i+1
    return res

if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    print(summaryRanges(nums))  # Output: ["0->2","4->5","7"]

    nums = [0,2,3,4,6,8,9]
    print(summaryRanges(nums))  # Output: ["0","2->4","6","8->9"]
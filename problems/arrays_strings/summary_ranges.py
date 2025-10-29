# 228 Summary Ranges 

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

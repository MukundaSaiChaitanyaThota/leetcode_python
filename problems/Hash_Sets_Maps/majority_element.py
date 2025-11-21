

from collections import defaultdict
from typing import List

def majorityElement(nums: List[int]) -> int:
    half=len(nums)//2
    counter=defaultdict(int)
    for n in nums:
        counter[n]+=1
        if counter[n]>half:
            return n
        

# another method:
def majorityElement2(nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums)//2]

if __name__ == "__main__":
    nums = [3,2,3]
    print(majorityElement(nums))  # Output: 3

    nums = [2,2,1,1,1,2,2]
    print(majorityElement(nums))  # Output: 2
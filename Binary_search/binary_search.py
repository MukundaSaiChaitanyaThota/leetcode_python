from typing import List

def search(nums: List[int], target: int) -> int:
    low=0
    high=len(nums)-1
    while low<=high:
        mid = (low+high)//2
        if target < nums[mid]:
            high = mid-1
        elif target > nums[mid]:
            low = mid+1
        else:
            return mid
    return -1

if __name__ == "__main__":
    # Example usage:
    nums = [-1,0,3,5,9,12]
    target = 2
    result = search(nums, target)
    print(f"Target {target} found at index: {result}")  # Output should be: Target 2 found at index: -1
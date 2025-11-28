# 167. Two Sum II - Input Array Is Sorted
# Problem: Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers (index1, index2) as an integer array answer of size 2, where 1 <= index1 < index2 <= numbers.length.
# You may assume that each input would have exactly one solution and you may not use the same element twice.

from typing import List
def twoSum( numbers: List[int], target: int) -> List[int]:
    start=0
    end=len(numbers)-1

    while start<end:
        summ=numbers[start]+numbers[end]
        if summ==target:
            return [start+1,end+1]
        elif summ < target:
            start+=1
        else:
            end-=1

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(twoSum(numbers, target))  # Output: [1,2]

    numbers = [2,3,4]
    target = 6
    print(twoSum(numbers, target))  # Output: [1,3]

    numbers = [-1,0]
    target = -1
    print(twoSum(numbers, target))  # Output: [1,2]
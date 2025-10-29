# 771. Jewels and Stones
# Given strings jewels and stones, where jewels represents the types of stones that are jewels, and stones represents the stones you have. 
# Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# time complexity: O(n + m)
# space complexity: O(m)
def numJewelsInStones( jewels: str, stones: str) -> int:
    stones_dict={}
    result=0
    for char in stones:
        if char in stones_dict.keys():
            stones_dict[char]+=1
        else:
            stones_dict[char]=1
    for char in jewels:
        if char in stones_dict.keys():
            result+=stones_dict[char]
    return result

if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"
    print(numJewelsInStones(jewels, stones))  # Output: 3

    jewels = "z"
    stones = "ZZ"
    print(numJewelsInStones(jewels, stones))  # Output: 0
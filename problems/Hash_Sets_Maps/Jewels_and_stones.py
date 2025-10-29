# 771. Jewels and Stones

def numJewelsInStones(self, jewels: str, stones: str) -> int:
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

# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

from collections import defaultdict

# time complexity: O(n)
# space complexity: O(1)
def isAnagram(s: str, t: str) -> bool:
    if len(s)!=len(t): return False
    counter=defaultdict(int)
    for c in s:
        counter[c]+=1
    for c in t:
        if c not in counter.keys():
            return False
        if counter[c]==1:
            del counter[c]
        else:
            counter[c]-=1
    return True

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))  # Output: True

    s = "rat"
    t = "car"
    print(isAnagram(s, t))  # Output: False
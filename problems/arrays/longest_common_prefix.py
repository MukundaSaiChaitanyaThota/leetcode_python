#longest common prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string ""

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    prefix=strs[0]
    for s in strs[1:]:
        i=0
        while i<len(prefix) and i<len(s) and prefix[i] ==s[i]:
            i+=1
        prefix=prefix[:i]
        if not prefix:
            return ""
    return prefix

    


if __name__ == "__main__":
    strs1 = ["flower","flow","flight"]
    strs2 = ["ab","a"]
    print(longestCommonPrefix(strs1))  # Output: "fl"
    print(longestCommonPrefix(strs2))  # Output: "a"
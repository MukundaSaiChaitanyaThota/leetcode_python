# 392. Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string 
# by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
#  (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Time complexity O(n)
# Space complexity O(1)
def isSubsequence(s: str, t: str) -> bool:
    A = len(s)
    i=0
    if s == "":
        return True
    for char in t:
        if char == s[i]:
            i+=1
        if i == A:
            return True
    return False

if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s, t))  # Output: True

    s = "b"
    t = "abc"
    print(isSubsequence(s, t))  # Output: False


# 28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

def strStr(haystack: str, needle: str) -> int:
    m = len(haystack)
    n = len(needle)
    for i in range(m):
        j=0
        for k in range(i,m):
            if haystack[k] == needle[j]:
                j+=1
            else:
                break
            if j==n:
                return i
    return -1
    
if __name__ == "__main__":
    print(strStr("sadbutsad", "sad"))
    print(strStr("leetcode", "leeto"))
    
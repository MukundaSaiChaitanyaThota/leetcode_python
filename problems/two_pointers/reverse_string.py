# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    start=0
    end=len(s)-1
    while start<end:
        s[start],s[end]=s[end],s[start]
        start+=1
        end-=1
    return s


if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    print(reverseString(s))  # Output: ["o","l","l","e","h"]

    s = ["H","a","n","n","a","h"]
    print(reverseString(s))  # Output: ["h","a","n","n","a","H"]
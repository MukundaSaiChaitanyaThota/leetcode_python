# 125 Valid Palindrome
# Problem: Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
def isPalindrome(s: str) -> bool:
    start=0
    end=len(s)-1

    while start<end:
        if not s[start].isalnum():
            start+=1
            continue
        if not s[end].isalnum():
            end-=1
            continue

        if s[start].lower() != s[end].lower():
            return False
        else:
            start+=1
            end-=1

    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))  # Output: True  

    s = "race a car"
    print(isPalindrome(s))  # Output: False 
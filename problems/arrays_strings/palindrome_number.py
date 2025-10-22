# Palindrome Number
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

def isPalindrome(x: int) -> bool:
    reverse = 0
    copy = x
    while x>0:
        rem = x%10
        reverse = (reverse*10)+rem
        x//=10
    return reverse == copy

# another method using string conversion
def isPalindrome_String(x: int) -> bool:
    s = str(x)
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
    x = 121
    print(isPalindrome(x))  # Output: True
    print(isPalindrome_String(x))  # Output: True
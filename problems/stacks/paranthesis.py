# LeetCode Problem: Valid Parentheses
# Problem: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def isValid(s: str) -> bool:
    open_brkt={
        ']':'[',
        '}':'{',
        ')':'('
        }
    # closed_brkt=[']',,')']
    stk=[]
    for bkt in s:
        if bkt not in open_brkt:
            stk.append(bkt)
        else:
            if len(stk) ==0:
                return False
            else:
                cur=stk.pop()
                if cur != open_brkt[bkt]:
                    return False
    if len(stk) != 0:
        return False
    else:
            return True
        
if __name__ == "__main__":
    # Example usage:
    s = "()"
    print(isValid(s))  # Output: True

    s = "()[]{}"
    print(isValid(s))  # Output: True

    s = "(]"
    print(isValid(s))  # Output: False
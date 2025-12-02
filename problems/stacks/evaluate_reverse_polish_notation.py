# Evaluate Reverse Polish Notation
# Given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation, evaluate the expression.
# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
# Note that division between two integers should truncate toward zero.
# It is guaranteed that the given RPN expression is always valid.
# That means the expression would always evaluate to a result, and there will not be any division by zero.

from typing import List
from math import ceil, floor

def evalRPN(tokens: List[str]) -> int:
    stk = []
    for t in tokens:
        if t in "+-*/":
            b, a = stk.pop(), stk.pop()
            if t == "+":
                stk.append(a + b)
            elif t == "-":
                stk.append(a - b)
            elif t == "*":
                stk.append(a * b)
            else:
                division = a / b
                if division < 0:
                    stk.append(ceil(division))
                else:
                    stk.append(floor(division))
        else:
            stk.append(int(t))
    return stk[0]



if __name__ == "__main__":
    # Example usage:
    tokens = ["2", "1", "+", "3", "*"]
    print(evalRPN(tokens))  # Output: 9

    tokens = ["4", "13", "5", "/", "+"]
    print(evalRPN(tokens))  # Output: 6

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(evalRPN(tokens))  # Output: 22

    
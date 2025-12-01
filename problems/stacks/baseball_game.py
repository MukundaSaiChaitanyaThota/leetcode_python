# LeetCode Problem: Baseball Game
# Problem: You are keeping score for a baseball game with strange rules. 
# The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.
# At the beginning of the game, you start with an empty record. 
# You are given a list of strings operations where operations[i] is the ith operation you must apply to the record and is one of the following:
# An integer x - Record a new score of x.  
# "+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
# "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
# "C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.


from typing import List

def calPoints(operations: List[str]) -> int:
    stk=[]
    for char in operations:
        if char == "+":
            stk.append(stk[-1]+stk[-2])
        elif char == "D":
            stk.append(stk[-1]*2)
        elif char == "C":
            stk.pop()
        else:
            stk.append(int(char))
    return sum(stk)

if __name__ == "__main__":
    # Example usage:
    operations = ["5","2","C","D","+"]
    print(calPoints(operations))  # Output: 30

    operations = ["5","-2","4","C","D","9","+","+"]
    print(calPoints(operations))  # Output: 27
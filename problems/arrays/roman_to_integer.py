# Convert a Roman numeral to an integer.

def romanToInt(s: str) -> int:
    sym_value_pair = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    sum=0
    i=0
    while i < len(s):
        cur = sym_value_pair[s[i]]
        if i < len(s)-1:
            if cur >= sym_value_pair[s[i+1]]:
                sum+=cur
                i+=1
            else:
                sum+= ( sym_value_pair[s[i+1]] - cur)
                i+=2
        else:
            sum+=cur
            i+=1
    return sum
    

if __name__ == "__main__":
    print(romanToInt("III"))      # 3
    print(romanToInt("IV"))       # 4
    print(romanToInt("IX"))       # 9
    print(romanToInt("LVIII"))    # 58
    print(romanToInt("MCMXCIV"))  # 1994
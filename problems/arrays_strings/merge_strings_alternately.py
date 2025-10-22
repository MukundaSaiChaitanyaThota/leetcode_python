# 1768. Merge Strings Alternately
# Given two strings word1 and word2, merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

#Method1
# time complexity O(n)
# space complexity O(n)
def mergeAlternately( word1: str, word2: str) -> str:
    a=len(word1)
    b=len(word2)
    res=""
    for i in range(min(a,b)):
        res+=word1[i]
        res+=word2[i]
    if a<b:
        res+=word2[a:]
    else:
        res+=word1[b:]
    return res

# Method2
# time complexity O(n)
# space complexity O(n)
def mergeAlternately(word1: str, word2: str) -> str:
    A=len(word1)
    B=len(word2)
    res=[]
    a,b = 0,0
    word = 1
    while a<A and b<B:
        if word == 1:
            res.append(word1[a])
            a+=1
            word=2
        else:
            res.append(word2[b])
            b+=1
            word=1
    while a<A:
        res.append(word1[a])
        a+=1
    while b<B:
        res.append(word2[b])
        b+=1
    return ''.join(res)

def test_mergeAlternately():
    assert mergeAlternately("abc", "pqrstu") == "apbqcrstu"
    assert mergeAlternately("ab", "pqrs") == "apbqrs"

if __name__ == "__main__":
    print(mergeAlternately("abc", "pqrstu")) # Output: "apbqcrstu"
    print(mergeAlternately("ab", "pqrs")) # Output: "apbqrs"
    
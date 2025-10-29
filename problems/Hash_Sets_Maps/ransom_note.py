# 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# time complexity: O(n + m)
# space complexity: O(m)

def canConstruct(ransomNote: str, magazine: str) -> bool:
    mag_char_dict={}
    for char in magazine:
        if char not in mag_char_dict.keys():
            mag_char_dict[char]=1
        else:
            mag_char_dict[char]+=1
    
    for char in ransomNote:
        if char not in mag_char_dict.keys():
            return False
        elif mag_char_dict[char]==0:
            return False
        else:
            mag_char_dict[char]-=1
    return True

if __name__ == "__main__":
    ransomNote = "a"
    magazine = "b"
    print(canConstruct(ransomNote, magazine))  # Output: False

    ransomNote = "aa"
    magazine = "ab"
    print(canConstruct(ransomNote, magazine))  # Output: False

    ransomNote = "aa"
    magazine = "aab"
    print(canConstruct(ransomNote, magazine))  # Output: True
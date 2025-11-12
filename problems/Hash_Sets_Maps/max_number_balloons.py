# 1189 
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.





def maxNumberOfBalloons(text: str) -> int:
    text_dict={"b":0,"a":0,"l":0,"o":0,"n":0}
    count=0
    for char in text:
        if char in text_dict.keys():
            text_dict[char]+=1
        if text_dict["b"]>=1 and text_dict["a"]>=1 and text_dict["l"]>=2 and text_dict["o"]>=2 and text_dict["n"]>=1:
            count+=1
            text_dict["b"]-=1
            text_dict["a"]-=1
            text_dict["l"]-=2
            text_dict["o"]-=2
            text_dict["n"]-=1
    return count

if __name__ == "__main__":
    text = "nlaebolko"
    print(maxNumberOfBalloons(text))  # Output: 1

    text = "baoollnnololgbax"
    print(maxNumberOfBalloons(text))  # Output: 2

    text = "balllllllllllloooooooooon"
    print(maxNumberOfBalloons(text))  # Output: 1
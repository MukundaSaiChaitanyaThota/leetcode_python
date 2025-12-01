# LeetCode Problem: Container With Most Water
# Problem: Given n non-negative integers height[0], height[1], ..., height[n-1] ,
# where each represents a point at coordinate (i, height[i]). n vertical lines are drawn such that the two endpoints of the line i is at (i, 0) and (i, height[i]).
# Find two lines, which together with the x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.

from typing import List

def maxArea(height: List[int]) -> int:
    n= len(height)
    l=0
    r=n-1
    max_area=0
    while l<r:
        h=min(height[l],height[r])
        w=r-l
        cur_area=h*w
        max_area=max(max_area,cur_area)
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return max_area

if __name__ == "__main__":
    # Example usage:
    heights = [1,8,6,2,5,4,8,3,7]
    print(maxArea(heights))  # Output: 49

    heights = [1,1]
    print(maxArea(heights))  # Output: 1
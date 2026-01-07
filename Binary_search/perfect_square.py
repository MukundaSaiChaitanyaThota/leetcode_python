class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        r=num//2
        while l<r:
            m=(l+r)//2
            if num < (m*m):
                r=m-1
            elif num > (m*m):
                l=m+1
            else:
                return True
        return False


if __name__ == "__main__":
    s = Solution()

    # Test case 1
    num1 = 16
    print(f"{num1} -> {s.isPerfectSquare(num1)}")

    # Test case 2
    num2 = 25
    print(f"{num2} -> {s.isPerfectSquare(num2)}")

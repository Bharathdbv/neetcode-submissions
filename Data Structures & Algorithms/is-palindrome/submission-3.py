class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = "".join([char for char in s if char.isalnum()])
        print(s)
        print(x)
        i = 0
        j = len(x) -1
        while(i<=j):
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        
        return True
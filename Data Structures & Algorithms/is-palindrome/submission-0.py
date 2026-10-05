class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.lower()
        print(s)
        c = []
        for x in s:
            if x.isalnum():
                c.append(x.lower())
        k = "".join(c)
        print(k)
        i = 0
        j = len(c)-1
        while i<=j:
            if c[i] == c[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True
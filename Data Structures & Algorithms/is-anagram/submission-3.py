class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s = list(s)
            t = list(t)
            list.sort(s)
            list.sort(t)

            for x,y in zip(s,t):
                if x == y:
                    continue
                else:
                    return False
            return True
        
        else:
            return False
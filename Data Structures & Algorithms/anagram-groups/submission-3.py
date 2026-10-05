class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            mapp = {}
            for x in strs:
                if str(sorted(x)) not in mapp:
                    mapp[str(sorted(x))] = [x]
                elif str(sorted(x)) in mapp:
                    mapp[str(sorted(x))].append(x)
            
            res = []
            for y in mapp:
                res.append(mapp[y])
            return res
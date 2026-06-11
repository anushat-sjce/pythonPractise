from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l1 = []
        l2 = []

        if len(s) != len(t):
            return False
        
        mapS = Counter(s)
        print(mapS)
        mapT = Counter(t)
        print(mapT)
        
        for key, value in mapS.items():
             x = mapS[key]
             print(x)
             l1.append(x)
        for key, value in mapT.items():
            y = mapT[key]
            print(y)
            l2.append(y)
            
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        
        return True
            #f mapT[value] == value:
             #   return True
                
            

m = Solution()
s = "bbbaaaba"
t = "aaabbbba"
ret = m.isIsomorphic(s, t)
print(ret)

class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = [] 
        p = False
        print(s)
        for i, val in enumerate(s):
            if val == "(":
                self.stack.append(val)
            if val == "{":
                self.stack.append(val)
            if val == "[":
                self.stack.append(val)
            if val == ")":
                if self.stack:
                    x = self.stack.pop()
                    if x == "(":
                        p = True
                    else :
                        return False
                else: 
                    return False
            if val == "}":
                if self.stack:
                    x = self.stack.pop()
                    if x == "{":
                        p = True
                    else :
                        return False
                else :
                    return False
            if val == "]":
                if self.stack:
                    x = self.stack.pop()
                    if x == "[":
                        p = True
                    else:
                        return False
                else :
                    return False
        if self.stack :
            return False
        return p
    
m = Solution()
s = "([])}"
k = m.isValid(s)
print(k)

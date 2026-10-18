class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        map={"]":"[","}":"{",")":"("} 
        for ch in s:
            if ch in map.values():
                stack.append(ch)
            else:
                if not stack or stack[-1]!=map[ch]:
                    return False
                stack.pop()
        return not stack       
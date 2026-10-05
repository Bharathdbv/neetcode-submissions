class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symb = ['+', '-', '*', '/']
        for x in tokens:
            if x in symb:
                b = stack.pop(len(stack) - 1)
                a = stack.pop(len(stack) - 1)
                if x == '+':
                    res = a+b
                elif x == '-':
                    res = a-b
                elif x == '*':
                    res = a*b
                else :
                    res = int(a/b)
                stack.append(res)
            else:
                stack.append(int(x))
        
        return stack[-1]
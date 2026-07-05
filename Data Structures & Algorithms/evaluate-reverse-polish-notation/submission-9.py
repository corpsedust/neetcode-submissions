class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []     #define the stack 

        operands = {"+":(lambda x,y : x+y),
                    "-":(lambda x,y : y-x),
                    "*":(lambda x,y : x*y),
                    "/":(lambda x,y : int(y/x))}

        for i in tokens:
            if i.lstrip("-").isdigit():
                s.append(int(i))
            elif i in operands:
                s.append(operands[i](s.pop(-1),s.pop(-1)))       #once you pop -1, you would want again -1
            else:
                pass
        return int(s[0])



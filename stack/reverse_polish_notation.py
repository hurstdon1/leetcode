# Evaluate the value of an arithmetic expression in Reverse Polish
#  Notation.

# Valid operators are +, -, *, and /. Each operand may be an
#  integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid.
#  That means the expression would always evaluate to a result, 
#  and there will not be any division by zero operation.


from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for item in tokens:  
            if item == "+":
                num1, num2 = stack.pop(), stack.pop()
                num3 = num2 + num1
                stack.append(num3)
            elif item == "-":
                num1, num2 = stack.pop(), stack.pop()
                num3 = num2 - num1
                stack.append(num3)
            elif item == "/":
                num1, num2 = stack.pop(), stack.pop()
                num3 = int(num2 / num1)
                stack.append(num3)
            elif item == '*':
                num1, num2 = stack.pop(), stack.pop()
                num3 = num2 * num1
                stack.append(num3)
            else:
                stack.append(int(item))

        return stack[0]

# Test Cases
sol = Solution()
tokens = ["2","1","+","3","*"]
print(sol.evalRPN(tokens))
tokens = ["4","13","5","/","+"]
print(sol.evalRPN(tokens))
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(tokens))
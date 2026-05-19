class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                num1 = stack.pop()
                num2 = stack.pop()

                if token == '+':
                    addition = num2 + num1
                    stack.append(addition)
                elif token == "-":
                    subtract = num2 - num1
                    stack.append(subtract)
                elif token == "*":
                    multiply = num2 * num1
                    stack.append(multiply)
                elif token == "/":
                    divide = num2 / num1
                    stack.append(int(divide))
            else:
                stack.append(int(token))
                    
                
        return stack[0]

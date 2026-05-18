class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dictionary = {')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if char not in dictionary:
                stack.append(char)

            else:

                if len(stack) == 0:
                    return False
                
                popped = stack.pop()

                if popped != dictionary[char]:
                    return False
        
        return not stack



            


        
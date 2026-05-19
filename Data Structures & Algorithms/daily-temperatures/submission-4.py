class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):

            while stack != [] and temp > stack[-1][0]:
                past_temp, past_index = stack.pop()
                wait_time = i - past_index
                result[past_index] = wait_time 
            
            stack.append([temp,i])
        return result

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i,h in enumerate(heights):
            start_index = i

            while stack and stack[-1][1] > h:
                pop_index, pop_height = stack.pop()

                current_area = pop_height * (i - pop_index)
                max_area = max(max_area, current_area)
            
                start_index = pop_index
            
            stack.append((start_index, h))

        for i,h in stack:
            current_area = h * (len(heights) - i)
            max_area = max(max_area, current_area)

        return max_area


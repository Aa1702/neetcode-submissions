

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # Our VIP Line (stores indices)
        
        for i, num in enumerate(nums):
            
            # Rule 1: Expiration
            # If the index at the front of the line is outside our current window, kick it out.
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # Rule 2: Absolute Power
            # While the new number is bigger than the numbers at the back of the line,
            # aggressively kick those smaller numbers out.
            while q and nums[q[-1]] < num:
                q.pop()
                
            # Add the new number's index to the back of the line
            q.append(i)
            
            # If our window has fully formed (size k), record the current maximum.
            # The maximum is ALWAYS sitting safely at the very front of our VIP line.
            if i >= k - 1:
                output.append(nums[q[0]])
                
        return output
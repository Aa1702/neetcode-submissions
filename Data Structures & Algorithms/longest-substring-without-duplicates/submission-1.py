class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_string = 0

        memory = set()

        for right in range(len(s)):

            while s[right] in memory:
                memory.remove(s[left])
                left += 1

            memory.add(s[right])

            max_string = max(max_string , (right - left + 1))
        return max_string

            



            




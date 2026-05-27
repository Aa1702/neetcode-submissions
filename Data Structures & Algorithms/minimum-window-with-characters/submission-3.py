class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == '':
            return ''

        t_map = Counter(t)
        window_map = {}

        have = 0
        need = len(t_map)

        best_window = [float('inf'), -1, -1]
        left = 0
        right = 0

        for right in range(len(s)):
            current_letter = s[right]
            window_map[current_letter] = window_map.get(current_letter, 0) + 1

            if current_letter in t_map and window_map[current_letter] == t_map[current_letter]:
                have += 1

            while have == need:
                current_window_size = right - left + 1

                if current_window_size < best_window[0]:
                    best_window = [current_window_size, right, left] 

                left_letter = s[left]
                window_map[left_letter] -= 1

                if left_letter in t_map and window_map[left_letter] < t_map[left_letter]:
                    have -= 1

                left += 1


        if best_window[0] == float('inf'):
            return ''

        return s[best_window[2] : best_window[1] + 1]



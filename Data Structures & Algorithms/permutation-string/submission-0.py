class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        if len(s1) > len(s2):
            return False
            
        # 2. Setup the Variables
        s1_map = Counter(s1) # Automatically counts target letters
        window_map = Counter()
        left = 0
        
        # 3. Slide the Wooden Frame
        for right in range(len(s2)):
            
            # Step A: Add the new letter entering the right side of the frame
            window_map[s2[right]] += 1
            
            # Step B: Enforce the wooden frame's strict size limit
            if (right - left + 1) > len(s1):
                left_char = s2[left]
                window_map[left_char] -= 1
                
                # CRITICAL STEP: If a letter's count hits 0, completely delete it.
                # Otherwise, Python thinks an empty 'a' doesn't match a missing 'a'.
                if window_map[left_char] == 0:
                    del window_map[left_char]
                    
                left += 1
                
            # Step C: The Match Check
            # Only check if they match when the frame is exactly the right size
            if (right - left + 1) == len(s1):
                if window_map == s1_map:
                    return True
                    
        # 4. End of the Line
        return False
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # 1. Initialize variables
        charSet = set()  # Set to track characters in the current window (O(1) lookup/removal)
        leftIndex = 0            # Left pointer of the sliding window
        maxLen = 0      # Stores the maximum length found so far

        # 2. Iterate through the string with the right pointer
        for r in range(len(s)):
            # If the character s[r] is already in the set, it's a duplicate.
            while s[r] in charSet:
                # Shrink the window from the left until the duplicate is removed.
                charSet.remove(s[leftIndex])
                leftIndex += 1
            
        #     # 3. Add the new character to the set and expand the window to the right
            charSet.add(s[r])
            
        #     # 4. Update the maximum length
        #     # Current window size is (right pointer index - left pointer index + 1)
            maxLen = max(maxLen, r - leftIndex + 1)

        return maxLen
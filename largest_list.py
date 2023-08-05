class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the last index of each character in the window
        char_index = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            # If the character is already in the window and its index is greater than or equal to the left pointer,
            # update the left pointer to the next index after the repeating character.
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1
            
            # Update the last index of the character in the window to the current index
            char_index[s[right]] = right

            # Update the maximum length of the window
            max_length = max(max_length, right - left + 1)

        return max_length
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Step 1: Check if the input number is negative
        is_negative = x < 0
        
        # Step 2: Convert the number to its absolute value
        num = abs(x)
        
        # Step 3: Initialize the reversed number
        reversed_num = 0
        
        # Step 4: Loop until the absolute value of the number becomes 0
        while num != 0:
            # Step 5: Get the last digit of the number
            last_digit = num % 10
            
            # Step 6: Build the reversed number by shifting digits to the left and adding the last digit
            reversed_num = reversed_num * 10 + last_digit
            
            # Step 7: Remove the last digit from the number
            num //= 10
        
        # Step 8: Handle the case of negative input by multiplying the reversed number by -1
        if is_negative:
            reversed_num *= -1
        
        # Step 9: Check if the reversed number is within the 32-bit signed integer range
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        
        return reversed_num

# Explanation of How the Solution Works:
# 1. We first check if the input number is negative to keep track of its sign.
# 2. We convert the input number to its absolute value to work with positive integers.
# 3. We initialize 'reversed_num' to store the reversed number.
# 4. In the loop, we extract the last digit of 'num' using the modulo operation.
# 5. We build the 'reversed_num' by shifting digits to the left and adding the last digit.
# 6. We remove the last digit from 'num' by performing integer division.
# 7. If the input was negative, we multiply 'reversed_num' by -1 to restore the sign.
# 8. Finally, we check if 'reversed_num' is within the valid 32-bit signed integer range.
# 9. If it's within the range, we return 'reversed_num'; otherwise, we return 0.
#ssssssssssss
# This solution ensures that the reversed integer is calculated correctly and handles boundary cases.sssss
#how its so fopoooreve
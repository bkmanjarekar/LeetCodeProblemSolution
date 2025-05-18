import collections

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Count the frequency of each digit in the input list
        digit_freq = collections.Counter(digits)        

        valid_3_digit_even_numbers = []

        # Iterate through all 3-digit even numbers from 100 to 998 (step by 2 to ensure even)
        for num in range(100, 1000, 2):
            hundreds = num // 100              # Extract hundreds place
            tens = (num // 10) % 10            # Extract tens place
            units = num % 10                   # Extract units place

            # Count the frequency of digits required to form this number
            required_freq = collections.Counter([hundreds, tens, units])

            # Check if all required digits are available in the input list
            is_possible = True
            for digit, count in required_freq.items():
                if digit_freq[digit] < count:
                    is_possible = False
                    break
            
            # If the number can be formed, add it to the result list
            if is_possible:
                valid_3_digit_even_numbers.append(num)

        return valid_3_digit_even_numbers


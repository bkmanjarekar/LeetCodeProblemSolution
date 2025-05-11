class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        Checks if the list contains three consecutive odd numbers.
        """
        if len(arr) < 3:
            return False  # Not enough elements to have three consecutive odds

        odd_streak = 0  # Counter for consecutive odd numbers

        for num in arr:
            if num % 2 != 0:  # If the number is odd
                odd_streak += 1
            else:
                odd_streak = 0  # Reset if the number is even

            if odd_streak == 3:
                return True  # Found 3 consecutive odd numbers

        return False  # No such streak found

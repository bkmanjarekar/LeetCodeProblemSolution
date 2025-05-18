class Solution(object):
    def minSum(self, nums1, nums2):
        """
        Calculate the minimum possible equal sum by replacing zeros with positive integers.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # Initialize sum of non-zero elements and count of zeros in nums1
        sum_nonzero1, count_zero1 = 0, 0
        for num in nums1:
            if num == 0:
                count_zero1 += 1
            else:
                sum_nonzero1 += num

        # Initialize sum of non-zero elements and count of zeros in nums2
        sum_nonzero2, count_zero2 = 0, 0
        for num in nums2:
            if num == 0:
                count_zero2 += 1
            else:
                sum_nonzero2 += num

        # Minimum possible sum for both arrays by replacing zeros with 1
        min_possible_sum1 = sum_nonzero1 + count_zero1
        min_possible_sum2 = sum_nonzero2 + count_zero2

        # If either array has no zero and its sum is strictly less than the other, return -1
        if (count_zero1 == 0 and sum_nonzero1 < min_possible_sum2) or \
           (count_zero2 == 0 and sum_nonzero2 < min_possible_sum1):
            return -1

        # Return the larger of the two minimum possible sums
        return max(min_possible_sum1, min_possible_sum2)


# time complexity O(M+N) (M elements in nums1) 
# space complexity O(1) (N elements in nums1) 
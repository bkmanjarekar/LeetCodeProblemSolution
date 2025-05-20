class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] > nums[2]:
            if nums[0] + nums[2] > nums[1]:
                if nums[1] + nums[2] > nums[0]:
                    num_count = collections.Counter(nums)
                    if 3 in num_count.values():
                        return "equilateral"
                    elif 2 in num_count.values():
                        return "isosceles"
                    else:
                        return "scalene"

        return "none"
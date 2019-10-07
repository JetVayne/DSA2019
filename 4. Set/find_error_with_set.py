class Solution:
    def findErrorNums(self, nums: [int]) -> [int]:
        n = len(nums)
        input_sum = sum(nums)

        set_sum = sum(set(nums))

        expected_sum = n * (n + 1) // 2

        return [input_sum - set_sum, expected_sum - set_sum]




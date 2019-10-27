class Solution:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums

        bigger_list = []
        smaller_list = []

        for n in nums[1:]:
            if n > nums[0]:
                bigger_list.append(n)
            else:
                smaller_list.append(n)

        return self.sortArray(smaller_list) + [nums[0]] + self.sortArray(bigger_list)

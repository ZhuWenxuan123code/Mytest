class Solution:
    def search(self, nums, target):
        left, right = -1, len(nums)
        while left + 1 != right:
            mid = (right + left) // 2
            num = nums[mid]
            if num <= target:
                left = mid
            else:
                right = mid
        # 根据情况选择要返回left，还是right
        if nums[left] == target:
            return left
        else:  # 不存在返回-1
            return -1


nums = [5, 7, 78, 789, 4567, 12345]
target = 789
Solve = Solution()
res = Solve.search(nums, target)
print(res)

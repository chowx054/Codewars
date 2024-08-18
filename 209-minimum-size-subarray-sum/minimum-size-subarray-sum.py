class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target:
            return 0
        elif target in nums:
            return 1

        else:
            left = 0
            current_sum = 0
            res = float("inf")

            for right in range(len(nums)):
                current_sum += nums[right]

                while current_sum >= target:
                    res = min(res, right-left+1)
                    current_sum -= nums[left]
                    left += 1
            return res
            
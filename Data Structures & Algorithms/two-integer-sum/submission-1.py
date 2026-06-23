class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {} # val:index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_hash:
                return [num_hash[diff],i]
            num_hash[n] = i

            






        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        h = {} #Num:index
        s = set()
        for i in range(len(nums)):  #store num:index in hashmap h
            if nums[i] not in h:
                h[nums[i]] = i

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                desired = - (nums[i] + nums[j])
                if desired in h and h[desired] != i and h[desired] != j:
                    s.add(tuple(sorted([nums[i], nums[j], desired])))
        return [list(triplet) for triplet in s]

        




        
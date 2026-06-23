class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #key:value
        val = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            val[c].append(n)

        res = []
        for i in range(len(val)-1, 0, -1):
            for n in val[i]:
                res.append(n)
                if len(res) ==k:
                    return res


        
        


            
            



        
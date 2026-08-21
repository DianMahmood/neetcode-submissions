class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashNums = defaultdict(int) # num - freq
        for n in nums:
            hashNums[n] += 1

        bList = [[] for _ in range(len(nums) + 1)]
        for num, freq in hashNums.items():
            bList[freq].append(num)
        
        res = []
        for x in range(len(bList) - 1, 0, -1):
            for num in bList[x]:
                res.append(num)
                if len(res) == k:
                    return res
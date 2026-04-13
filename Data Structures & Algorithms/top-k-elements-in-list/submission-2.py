class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashnum = Counter(nums)
        output = sorted(hashnum, key = hashnum.get, reverse=True)
        print(output)
        return output[:k]
 
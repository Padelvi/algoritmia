class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        return 0 if nums = []
        return nums[0] if len(nums) == 1
        def twoB(l: List[int,int]) -> int:
            if l[0] > l[1]:
                a = l[0]
                b = l[1]
            else:
                a = l[1]
                b = l[0]
            return a*(b+1)
        return twoB(nums) if len(nums) == 2

        solved = dict()
        def calc(l: List[int], prev: int) -> int:
            if tuple(l) in solved.values():
                return prev + solved[l]
            results = []
            for i in l:
                item = l[i]
                results.append()
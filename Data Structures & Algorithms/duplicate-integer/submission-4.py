class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains = dict()
        for num in nums:
            if contains.get(num):
                return True
            contains[num] = 1
        return False
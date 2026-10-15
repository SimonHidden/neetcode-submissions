class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = {}

        for i, n in enumerate(nums):
            d = target - n
            
            if d in val_index:
                return [val_index[d], i]

            val_index[n] = i
            
        return []
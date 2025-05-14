class Solution:
    def containsDuplicate(self, nums) -> bool:
        # return False if the length of the set of nums(Nums with dulplicates removed) is the same as the length of the original list
        return len(nums) != len(set(nums))
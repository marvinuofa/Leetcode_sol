class Solution:
    def minSum(self, nums1, nums2) -> int:
        # count the total number of zeros in each list 
        n1_0 = nums1.count(0)
        n2_0 = nums2.count(0)

        # get the sum both lists 
        n1_sum = sum(nums1)
        n2_sum = sum(nums2)

        # add the sum and no of zeros of each list 
        t_sum1 = n1_sum + n1_0
        t_sum2 = n2_sum + n2_0

        # if a list has no zero then its sum cannot be chaged 
        # If the other list total(Zeros + sum) is larger, since negative numbers cannot be added then the arrays will never be equal 
        if (not n1_0 and t_sum1 < t_sum2) or (not n2_0 and t_sum2 < t_sum1):
            return -1 

        # return the larger the list with the larger total 
        else:
            return max(t_sum1, t_sum2)
class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        out = 0 
        for i in arr:
            if i %2 !=0:
                out +=1 
            else:
                out = 0 
            if out == 3:
                return True 
        return False 
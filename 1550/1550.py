class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        # Counter to track consecutive odd numbers
        out = 0 
        
        # Loop through each number in the array
        for i in arr:
            # Check if the number is odd
            if i % 2 != 0:
                out += 1  # Increment counter if odd
            else:
                out = 0  # Reset counter if even

            # If we've seen 3 odds in a row, return True
            if out == 3:
                return True 
        
        # If loop finishes without finding 3 consecutive odds
        return False

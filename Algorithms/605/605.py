class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        # If no flowers need to be placed, return True immediately
        if n == 0:
            return True

        # Add zero padding to both ends to simplify edge case checks
        flowerbed = [0] + flowerbed + [0]

        # Iterate through the flowerbed (excluding padding)
        for i, flower in enumerate(flowerbed[1:-1], start=1):
            # Check if the current, previous, and next plots are all empty (0)
            if not (flower or flowerbed[i - 1] or flowerbed[i + 1]):
                # Place a flower at the current position
                flowerbed[i] = 1
                # Decrease the number of flowers we need to place
                n -= 1
                # If we've placed all required flowers, return True
                if n <= 0:
                    return True

        # If we finish the loop without placing all flowers, return False
        return False
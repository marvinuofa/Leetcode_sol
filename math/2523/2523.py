class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Optimized Sieve of Eratosthenes to find all primes up to 'right'
        def sieve(limit):
            is_prime = [True] * (limit + 1)  # Initialize all numbers as prime
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
            
            # Mark non-primes using Sieve of Eratosthenes
            for i in range(2, int(limit ** 0.5) + 1):
                if is_prime[i]:
                    for multiple in range(i * i, limit + 1, i):
                        is_prime[multiple] = False
            
            # Return only the primes within the [left, right] range
            return [num for num in range(left, limit + 1) if is_prime[num]]

        primes = sieve(right)  # Get all primes between 'left' and 'right'

        # If fewer than 2 primes exist in the range, no closest pair can be formed
        if len(primes) < 2:
            return [-1, -1]

        # Find the pair of primes with the smallest difference
        min_diff = float("inf")  # Initialize minimum difference to infinity
        res = []  # Result will hold the closest pair
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                res = [primes[i - 1], primes[i]]  # Update result with the new closest pair

        return res  # Return the closest pair of primes

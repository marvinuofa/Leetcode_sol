class Solution:
    def findEvenNumbers(self, digits):
        out = []

        # Loop to select the unit (last) digit, which must be even
        for i in range(len(digits)):
            if not digits[i] % 2:  # check if digit is even
                unit = str(digits[i])

                # Loop to select the tens (middle) digit
                for j in range(len(digits)):
                    if j != i:  # ensure digits are not reused
                        tens = str(digits[j])

                        # Loop to select the hundreds (first) digit
                        for k in range(len(digits)):
                            # Ensure all indices are distinct and number doesn't start with 0
                            if k != i and k != j and digits[k] != 0:
                                hundreds = str(digits[k])

                                # Form the 3-digit number and add to output
                                out.append(int(hundreds + tens + unit))

        # Remove duplicates and sort the result
        out = set(out)
        return sorted(list(out))


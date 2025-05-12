class Solution:
    def findEvenNumbers(self, digits):
        out = []
        for i in range(len(digits)):
            if not digits[i]%2:
                unit = str(digits[i])
                for j in range(len(digits)):
                    if j != i:
                        tens = str(digits[j])
                        for k in range(len(digits)):
                            if k != i and k != j and digits[k] != 0:
                                hundreds = str(digits[k])
                                out.append(int(hundreds+tens+unit))
        out = set(out)
        return sorted(list(out))


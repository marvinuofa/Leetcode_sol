class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter  # Import Counter to count character frequencies in strings

        # If the lengths of the strings are different, they can't be anagrams
        if len(s) != len(t):
            return False

        # Count the frequency of each character in both strings
        s_hash = Counter(s)
        t_hash = Counter(t)

        # Compare character counts in both dictionaries
        for key, value in t_hash.items():
            # If the character is not in s_hash or the counts don't match, it's not an anagram
            if not s_hash[key] or s_hash[key] != value:
                return False

        # If all characters match in count, it's an anagram
        return True

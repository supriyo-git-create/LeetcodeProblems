class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Take the first string as a reference
        prefix = strs[0]

        # Compare prefix with every string
        for s in strs[1:]:
            # Reduce prefix until it matches the start of the string s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix

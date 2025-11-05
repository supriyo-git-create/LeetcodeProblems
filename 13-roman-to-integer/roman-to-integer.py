class Solution(object):
    def romanToInt(self, s):
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        for ch in s:
            number += translations[ch]
        return number
#Now, in Roman numerals, when a smaller value comes before a larger one, it means you subtract the smaller from the larger.
#for char in s means it will read the input roman numerical one by one
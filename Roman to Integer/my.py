class Solution:
    def romanToInt(self, s: str) -> int:
        x = []
        rom_to_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        while i < len(s):
            if i + 1 < len(s):
                if rom_to_num[s[i]] >= rom_to_num[s[i + 1]]:
                    x.append(s[i])
                else:
                    x.append(s[i] + s[i + 1])
                    i += 1
            else:
                x.append(s[i])
            i += 1

        sum = 0
        for j in x:
            if len(j) == 1:

                sum += rom_to_num[j]
            else:
                sum += abs(rom_to_num[j[0]] - rom_to_num[j[1]])
        return sum

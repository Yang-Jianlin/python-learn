class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 1:
            return strs[0]
        min_len = len(min(strs, key=len))
        j = 0
        res = ""
        while j < min_len:
            mod = []
            for i in range(0, len(strs)):
                mod.append(strs[i][j])
            if len(set(mod)) == 1:
                res += mod[0]
            else:
                break
            j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    strs = ["dog", "racecar", "car"]
    print(s.longestCommonPrefix(strs))

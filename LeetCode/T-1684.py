class Solution:
    def countConsistentStrings(self, allowed, words):
        count = 0
        for i in words:
            for j in i:
                if j not in allowed:
                    count -= 1
                    break
            count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    print(s.countConsistentStrings(allowed, words))

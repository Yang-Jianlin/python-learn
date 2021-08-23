class Solution(object):
    def __init__(self):
        self.res = []

    def findSubstring(self, s, words):
        words.sort()
        check = [0 for i in range(len(words))]
        self.backtrack([], words, check)
        print(self.res)
        result = []
        for i in self.res:
            try:
                result.extend(self.using_str_index(i, s))
            except Exception as error:
                pass
        return sorted(result)

    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(''.join(sol))
            return

        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol + [nums[i]], nums, check)
            check[i] = 0

    def using_str_index(self, word, sentence):
        r = []
        index = 0
        while index < len(sentence):
            index = sentence.find(word, index)
            if index == -1:
                break
            r.append(index)
            index += 1
        return r


if __name__ == '__main__':
    s = "aaa"
    words = ['a', 'a']

    solu = Solution()
    print(solu.findSubstring(s, words))

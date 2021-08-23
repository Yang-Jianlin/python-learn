class Solution:
    def checkIfPangram(self, sentence):
        a = set(sentence)
        if len(a) == 26:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    sentence = "leetcode"
    print(s.checkIfPangram(sentence=sentence))

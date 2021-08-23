class Solution:
    def replaceSpace(self, s: str):
        replace = '%20'
        l = s.split(' ')
        print(l)
        return replace.join(l)


if __name__ == '__main__':
    solu = Solution()
    s = "We  are  happy."
    print(solu.replaceSpace(s))

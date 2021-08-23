class Solution(object):
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        if needle not in haystack:
            return -1
        return haystack.index(needle)

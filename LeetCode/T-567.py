class Solution:
    def checkInclusion(self, s1: str, s2: str):
        n_s1 = len(s1)
        n_s2 = len(s2)
        start = 0
        end = start + n_s1
        s1_dict = {}
        for x in range(n_s1):
            count = 0
            for y in range(n_s1):
                if s1[x] == s1[y]:
                    count += 1
            s1_dict[s1[x]] = count

        while end <= n_s2:
            em_str = s2[start:end]
            n_em = len(em_str)
            em_dict = {}
            for x in range(n_em):
                count = 0
                for y in range(n_em):
                    if em_str[x] == em_str[y]:
                        count += 1
                em_dict[em_str[x]] = count
            if em_dict == s1_dict:
                return True
            start += 1
            end = start + n_s1
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    s1 = 'ab'
    s2 = "eidbaooo"
    print(s.checkInclusion(s1, s2))

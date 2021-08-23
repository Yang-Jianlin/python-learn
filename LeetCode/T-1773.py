class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0
        if ruleKey == 'type':
            n = 0
        elif ruleKey == 'color':
            n = 1
        elif ruleKey == 'name':
            n = 2
        for i in items:
            if i[n] == ruleValue:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],
             ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    print(s.countMatches(items, ruleKey, ruleValue))

"""
判断括号合法性的条件：
(1) 长度为1或者奇数肯定false
(2) 首字母在“]})”中为false
(3) 当遍历字符在右边，但是栈空时，false
(4) 当遍历字符在右边，且出栈匹配元素和遍历字符位置不一致，false
(5) 遍历结束，栈不空，false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        left = "([{"
        right = ")]}"
        if len(s) == 1 or s[0] in right or len(s) % 2 != 0:
            return False
        stack = [s[0]]
        for i in range(1, len(s)):
            if s[i] in left:
                stack.append(s[i])
            if s[i] in right:
                if not stack:
                    return False
                tmp = stack.pop()
                if right.index(s[i]) != left.index(tmp):
                    return False
        if not stack:
            return True
        else:
            return False


if __name__ == '__main__':
    solu = Solution()
    s = "()[]}{"
    print(solu.isValid(s))

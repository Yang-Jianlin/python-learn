class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        for i in range(len(height) - 1):
            j = len(height) - 1
            while i < j:
                h = min(height[i], height[j])
                s = h * (j - i)
                if s > max_area:
                    max_area = s
                j -= 1
        return max_area

    def maxArea2(self, height):
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            h = min(height[i], height[j])
            s = h * (j - i)
            if s > max_area:
                max_area = s
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:  # 只要两个相等，就可以把左右指针都移动了
                i += 1
                j -= 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    height = [4, 3, 2, 1, 4]
    print(s.maxArea(height))
    print(s.maxArea2(height))

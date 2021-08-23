class Solution:
    def minTimeToVisitAllPoints(self, points):
        count_time = 0
        for i in range(0, len(points)):
            j = i + 1
            if j == len(points):
                break
            else:
                if points[i][0] == points[j][0]:
                    count_time += abs(points[j][1] - points[i][1])
                elif points[i][1] == points[j][1]:
                    count_time += abs(points[j][0] - points[i][0])
                elif abs(points[j][0] - points[i][0]) == abs(points[j][1] - points[i][1]):
                    count_time += abs(points[j][0] - points[i][0])
                else:
                    if abs(points[j][0] - points[i][0]) > abs(points[j][1] - points[i][1]):
                        count_time += abs(points[j][0] - points[i][0])
                    else:
                        count_time += abs(points[j][1] - points[i][1])
        return count_time


if __name__ == '__main__':
    s = Solution()
    points = [[3, 2], [-2, 2]]
    print(s.minTimeToVisitAllPoints(points))

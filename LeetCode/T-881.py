class Solution:
    def numRescueBoats(self, people, limit) -> int:
        i = 0
        j = len(people) - 1
        result = 0
        people.sort()
        while i < j:
            a = people[i]
            b = people[j]
            s = a + b
            if s > limit:
                j -= 1
            else:
                result += 1
                people.remove(a)
                people.remove(b)
                j = len(people) - 1
                i = 0
        result = result + len(people)
        return result

    def numRescueBoats2(self, people, limit) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        result = 0
        while i <= j:
            result += 1
            if people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    people = [3, 2, 2, 1]
    limit = 3
    print(s.numRescueBoats2(people, limit))

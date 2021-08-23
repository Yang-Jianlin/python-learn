class Solution:
    def game(self, guess, answer):
        count = 0
        for i in range(0, len(guess)):
            if guess[i] == answer[i]:
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    guess = [2, 2, 3]
    answer = [3, 2, 1]
    print(s.game(guess, answer))

class Solution:
    def interpret(self, command):
        command = list(command)
        result = []
        for i in range(0, len(command)):
            if command[i] == 'G':
                result.append('G')
            elif command[i] == '(':
                if command[i+1] == ')':
                    result.append('o')
                else:
                    result.append('al')
            elif command[i] == '/':
                result.append('/')
        return ''.join(result)


if __name__ == '__main__':
    command = "G()(al)"
    s = Solution()
    print(s.interpret(command))

def solution(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    return solution(n - 1) + solution(n - 2)


if __name__ == '__main__':
    n = 5
    print(solution(n))

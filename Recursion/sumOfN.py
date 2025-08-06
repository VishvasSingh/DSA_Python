

def get_sum(n: int) -> int:
    if n <= 0:
        return 0

    if n == 1:
        return 1

    return n + get_sum(n-1)


if __name__ == '__main__':
    total = get_sum(-1)
    print(total)

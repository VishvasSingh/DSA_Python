
"""
Recursive function to calculate the nth Fibonacci number.
"""

# def fib(n: int) -> int:
#     if n < 0:
#         raise ValueError("Input cannot be negative")
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#     return fib(n - 1) + fib(n - 2)

"""
Iterative approach
"""


def fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    fib_num, prev_sum, sum_holder = 1, 1, 0
    for i in range(2, n):
        sum_holder = fib_num
        fib_num += prev_sum
        prev_sum = sum_holder

    return fib_num


if __name__ == '__main__':
    try:
        result = fib(10)
        print(f"The 10th Fibonacci number is: {result}")
    except ValueError as e:
        print(e)

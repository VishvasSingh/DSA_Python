from typing import List


def best_time(prices: List[int]) -> int:
    max_profit = 0
    for i in range(1, len(prices)):
        curr_profit = prices[i]-prices[i-1]
        if curr_profit > 0:
            max_profit += curr_profit

    return max_profit


if __name__ == "__main__":
    nums = [1,2,3,4,5]
    prof = best_time(nums)
    print(prof)




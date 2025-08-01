# statistics.py
from math import sqrt

def mean(nums):
    total = 0.0
    for num in nums:
        total += num
    return total / len(nums)

def stdDev(nums, x_bar):
    sum_dev_sq = 0.0
    for num in nums:
        dev = num - x_bar
        sum_dev_sq += dev * dev
    return sqrt(sum_dev_sq / (len(nums) - 1))
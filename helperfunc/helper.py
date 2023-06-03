import pandas as pd
import numpy as np

def helper_function1():
    print("This is Helper Function 1")

def helper_function2():
	print("This is Helper Function 2")

def pick(l: list, index: int = 0) -> int:
    return l[index]


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

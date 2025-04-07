"""
Module for checking task functionality
with manual input
"""
from solution import task_1


if __name__ == "__main__":
    jumps_arr = list(map(int, input().strip().split(' ')))
    print(task_1(jumps_arr))

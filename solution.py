"""Module for solving algorithmic tasks"""
from typing import List


def task_1(jumps: List[int]) -> bool:
    """Solving 1 task"""
    if not jumps or len(jumps) == 1:
        # Probably you can reach last element if there are no elements
        # or only one
        return True
    reachable = 0
    last_ell = len(jumps) - 1
    for i, max_jump in enumerate(jumps):
        if i > reachable:
            return False
        reachable = max(reachable, i + max_jump)
        if reachable > last_ell:
            return True


if __name__ == "__main__":
    jumps_arr = list(map(int, input().strip().split(' ')))
    print(task_1(jumps_arr))

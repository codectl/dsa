from collections import defaultdict


def fn(arr, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in arr:
        # do logic to change curr
        ans += counts[curr - k]
        counts[curr] += 1

    return ans


def count_subarrays_whose_sum_is_k(nums: list[int], k: int) -> int:
    """Given an integer array nums and an integer k,
    find the number of subarrays whose sum is equal to k.
    """
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0

    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1

    return ans

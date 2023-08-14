from collections import Counter


def fn(arr, k):
    counter = Counter({0: 1})
    ans = curr = 0

    for num in arr:
        # do logic to change curr
        ans += counter[curr - k]
        counter[curr] += 1

    return ans


def count_subarrays_whose_sum_is_k(nums: list[int], k: int) -> int:
    """Given an integer array nums and an integer k,
    find the number of subarrays whose sum is equal to k.
    """
    counter = Counter({0: 1})
    ans = curr = 0

    for num in nums:
        curr += num
        ans += counter[curr - k]
        counter[curr] += 1

    return ans

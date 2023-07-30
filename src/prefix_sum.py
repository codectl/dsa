def fn(arr):
    prefix = [0] * len(arr)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]

    # alternative
    prefix = [0] * len(arr)
    for i in range(len(arr)):
        prefix[i] = prefix[i - min(1, i)] + arr[i]

    # apply logic here ...
    # formula for sum between interval i and j:
    # prefix[j] - prefix[i] + nums[i]

    return prefix


def get_averages(nums: list[int], k: int) -> list[int]:
    """Build and return an array averages of length n
    where averages[i] is the k-radius average for the
    subarray centered at index i.
    """
    n = len(nums)

    prefix = [0] * n
    for i in range(n):
        prefix[i] = prefix[i - min(1, i)] + nums[i]

    ans = [-1] * n
    for i in range(n):
        if k <= i <= n - k - 1:
            total = prefix[i + k] - prefix[i - k] + nums[i - k]
            ans[i] = total // (k * 2 + 1)
    return ans

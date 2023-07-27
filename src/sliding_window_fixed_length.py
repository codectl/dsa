def fn(arr, k):
    # some data to track the window
    curr = 0

    # build the first window
    for i in range(k):
        curr += arr[i]

    ans = 0
    for i in range(k, len(arr)):
        right = i
        left = i - k
        # do logic here with arr[left] and arr[right]
        # update ans

    return ans

# EXAMPLES


def get_averages(nums: list[int], k: int) -> list[int]:
    """Build and return an array avgs of length n
    where avgs[i] is the k-radius average for the
    subarray centered at index i.
    """
    n = k * 2 + 1
    ans = [-1] * len(nums)

    if n > len(nums):
        return ans

    curr = sum(nums[:n])
    ans[k] = curr // n

    for i in range(n, len(nums)):
        curr += nums[i] - nums[i - n]
        ans[i - k] = curr // n

    return ans

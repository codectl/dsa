def fn(arr):
    left = ans = curr = 0

    for right in range(len(arr)):
        # do logic here to add arr[right] to curr

        while WINDOW_CONDITION_BROKEN:
            # remove arr[left] from curr
            left += 1

        # update ans

    return ans


# EXAMPLES
def min_sub_array_len(target: int, nums: list[int]) -> int:
    """Return the minimal length of a subarray
    whose sum is greater than or equal to target.
    If there is no such subarray, return 0 instead.
    """
    if sum(nums) < target:
        return 0

    left = curr = 0
    ans = len(nums)
    for right in range(len(nums)):
        curr += nums[right]
        while curr >= target:
            ans = min(ans, right - left + 1)
            curr -= nums[left]
            left += 1
    return ans

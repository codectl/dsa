def fn(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        last = len(arr) - 1
        prefix.append(last + arr[i])

    # apply logic here ...
    # formula for sum between interval i and j:
    # prefix[j] - prefix[i] + nums[i]

    return prefix

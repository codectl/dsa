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

def get_last(arr, target):
    l , r = 0 , len(arr) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if arr[mid] == target:
            l = mid
        elif arr[mid] < target:
            l = mid 
        else:
            r = mid
    #post
    if arr[r] == target: return r
    if arr[l] == target: return l
    return -1
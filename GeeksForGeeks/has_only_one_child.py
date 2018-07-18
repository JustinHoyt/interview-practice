def has_only_one_child(pre):
    upper_bound = float("INF")
    lower_bound = float("-INF")
    for i in range(len(pre) - 1):
        parent = pre[i]
        child = pre[i+1]
        if child > upper_bound or child < lower_bound:
            return False
        if child < parent:
            upper_bound = min(upper_bound, parent)
        else:
            lower_bound = min(lower_bound, parent)
    return True


print(has_only_one_child([20, 10, 11, 13, 12, 24]))
print(has_only_one_child([20, 10, 11, 13, 12]))

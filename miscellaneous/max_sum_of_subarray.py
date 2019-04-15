def maxSubArraySum(a):
  max_so_far = float("-inf")
  max_idxs = (0,0)
  curr_left_bound = 0
  curr_sum = 0

  for i in range(0, len(a)):
    curr_sum = curr_sum + a[i]
    if (max_so_far < curr_sum):
      max_so_far = curr_sum
      max_idxs = curr_left_bound, i

    if curr_sum < 0:
      curr_sum = 0
      curr_left_bound = i + 1

  return max_so_far, a[max_idxs[0]: max_idxs[1] + 1]

array = [-2, 4, -1, -2, 1, 5, -3, -15, 2, 3]
print(maxSubArraySum(array))

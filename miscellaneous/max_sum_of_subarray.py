def maxSubArraySum(a):
  max_so_far = float("-inf")
  max_range = (0,1)
  curr_left_bound = 0
  curr_sum = 0

  for i in range(0, len(a)):
    curr_sum = curr_sum + a[i]
    if (max_so_far < curr_sum):
      max_so_far = curr_sum
      max_range = curr_left_bound, i + 1

    if curr_sum < 0:
      curr_sum = 0
      curr_left_bound = i + 1

  return max_so_far, a[max_range[0]: max_range[1]]

array = [-2, 4, -1, -2, 1, 5, -3, -15, 2, 3]
print(maxSubArraySum(array))

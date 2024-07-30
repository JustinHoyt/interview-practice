function jump(nums: number[]): number {
  const memo: number[] = Array(nums.length);

  function shortestRoute(i: number): number {
    // Out of bounds is okay because it means we found an in-bounds case earlier
    if (i >= nums.length - 1) return 0;
    if (memo[i] != null) return memo[i];

    let shortest = Infinity;
    for (let j = 1; j <= nums[i] && j < nums.length; j++) {
      shortest = Math.min(shortest, shortestRoute(i + j));
    }

    return memo[i] = shortest + 1;
  }

  return shortestRoute(0);
}

export { jump };

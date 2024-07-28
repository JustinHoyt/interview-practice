/**
 *          r
 *          w
 * [1,2,2,4,5]
 *  0 1 2 3 4
 */
export function removeDuplicates(nums: number[]): number {
  if (nums.length < 2) return nums.length;

  /**
   * '[w]alk' and '[r]ight' indexes follow the array from right to left to
   * swap out duplicates with the right most non-duplicate value
   */
  let r = nums.length - 1;
  for (let w = nums.length - 1; w > 0; w--) {
    if (nums[w] !== nums[w - 1]) continue;

    [nums[w], nums[r]] = [nums[r], nums[w]];
    r--;
  }

  nums.splice(r + 1);
  nums.sort((a, b) => a - b);

  return r + 1;
}

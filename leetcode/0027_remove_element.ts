export function removeElement(nums: number[], val: number): number {
  let r = nums.length - 1;
  for (let i = nums.length - 1; i > -1; i--) {
    if (nums[i] !== val) continue;

    [nums[i], nums[r]] = [nums[r], nums[i]];
    r--;
  }

  return r + 1;
}

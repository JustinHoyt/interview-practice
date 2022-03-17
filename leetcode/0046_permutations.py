class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perms: list[list[int]] = []
        if len(nums) == 0:
            return perms

        def generate_perms(idx):
            if idx == len(nums):
                perms.append(nums[:])

            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                generate_perms(idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]

        generate_perms(0)
        return perms



def test_happy_path():
    assert Solution().permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]

def test_one_element():
    assert Solution().permute([1]) == [[1]]

def test_zero_elements():
    assert Solution().permute([]) == []


if __name__ == "__main__":
    test_happy_path()

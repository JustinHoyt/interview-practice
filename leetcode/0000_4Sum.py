import timeit
from timeit import Timer

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j:
                    left = j
                    right = len(nums) - 1
                    while left < right:
                        if i == left or j == left:
                            left += 1
                            continue
                        if i == right or j == right:
                            right -= 1
                            continue

                        total = nums[i] + nums[j] + nums[left] + nums[right]
                        if total == target:
                            temp_combination = [nums[i], nums[j], nums[left], nums[right]]
                            temp_combination.sort()
                            if temp_combination not in results:
                                results.append(temp_combination)
                            left += 1
                            right -= 1
                        elif total < target:
                            left += 1
                        else:
                            right -= 1
        return results


# right            v
# left       v
# j        v
# i     v
# arr = [-3,-1,0,2,4,5]
# arr = [1,0,-1,0,-2,2]
# target = 0
arr = [-498,-492,-473,-455,-441,-412,-390,-378,-365,-359,-358,-326,-311,-305,-277,-265,-264,-256,-254,-240,-237,-234,-222,-211,-203,-201,-187,-172,-164,-134,-131,-91,-84,-55,-54,-52,-50,-27,-23,-4,0,4,20,39,45,53,53,55,60,82,88,89,89,98,101,111,134,136,209,214,220,221,224,254,281,288,289,301,304,308,318,321,342,348,354,360,383,388,410,423,442,455,457,471,488,488]
target = -2808

# arr = [-430,-407,-404,-370,-364,-343,-291,-263,-257,-242,-213,-212,-210,-209,-172,-144,-85,-79,-70,-36,-34,-14,0,18,31,36,45,45,83,117,120,134,153,178,186,197,208,223,234,263,264,313,341,382,388,421,427,439,445,451,458,467,474,480]
# target = 4668

arr = [-487,-462,-445,-401,-389,-388,-379,-374,-365,-334,-326,-314,-302,-280,-277,-241,-234,-216,-207,-179,-154,-130,-118,-102,-98,-37,-30,-19,13,21,22,61,66,83,84,109,117,122,141,162,170,205,209,223,232,240,246,250,264,274,286,289,303,304,322,335,336,338,349,355,360,363,365,397,403,417,420,429,438,439]
target = 1801
sol = Solution()
# print(timeit.timeit(sol.fourSum(arr, target), number=10))
t = Timer(lambda: sol.fourSum(arr, target))
print(t.timeit(number=1))
# print(sol.fourSum(arr, target))

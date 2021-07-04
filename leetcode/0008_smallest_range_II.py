from copy import deepcopy

def smallestRangeRec(A, K, B, idx, memo, is_add):
    # key = ",".join( map(str, B) )
    # key += "," + str(idx)
    key = idx
    if key in memo:
        return memo[key]
    if idx >= 0:
        if idx == len(B):
            return max(B) - min(B)
        if is_add:
            B[idx] = A[idx] + K
        else:
            B[idx] = A[idx] - K
    idx += 1
    add = smallestRangeRec(A, K, B, idx, memo, True)
    sub = smallestRangeRec(A, K, B, idx, memo, False)
    result = min(add, sub)
    memo[key] = result
    return result


class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        B = deepcopy(A)
        memo = {}
        idx = -1
        return smallestRangeRec(A, K, B, idx, memo, False)


A = [8038,9111,5458,8483,5052,9161,8368,2094,8366,9164,53,7222,9284,5059,4375,2667,2243,5329,3111,5678,5958,815,6841,1377,2752,8569,1483,9191,4675,6230,1169,9833,5366,502,1591,5113,2706,8515,3710,7272,1596,5114,3620,2911,8378,8012,4586,9610,8361,1646,2025,1323,5176,1832,7321,1900,1926,5518,8801,679,3368,2086,7486,575,9221,2993,421,1202,1845,9767,4533,1505,820,967,2811,5603,574,6920,5493,9490,9303,4648,281,2947,4117,2848,7395,930,1023,1439,8045,5161,2315,5705,7596,5854,1835,6591,2553,8628]
print(len(A))
K = 4643
sol = Solution()
print(sol.smallestRangeII(A,K))

'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Example
1:
Input: nums = [1, 1, 1], k = 2
Output: 2
Example
2:

Input: nums = [1, 2, 3], k = 3
Output: 2

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        cont=0
        l= len(nums)
        for i in range(l):
            sum = 0
            for j in range(i,l):
                sum += nums[j]
                if sum == k :
                    cont+=1
        return cont


l = [5,0,5,10,3,2,-15,4]
obj = Solution()
print(obj.subarraySum(l,5))

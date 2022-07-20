'''
Given an array nums.We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.
Example
1:
Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
Explanation: Running
sum is obtained as follows: [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4].

Example
2:
Input: nums = [1, 1, 1, 1, 1]
Output: [1, 2, 3, 4, 5]
Explanation: Running
sum is obtained as follows: [1, 1 + 1, 1 + 1 + 1, 1 + 1 + 1 + 1, 1 + 1 + 1 + 1 + 1].

Example
3:
Input: nums = [3, 1, 2, 10, 1]
Output: [3, 4, 6, 16, 17]

Constraints:

1 <= nums.length <= 1000
-10 ^ 6 <= nums[i] <= 10 ^ 6
'''

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        if len(nums) == 0 :
            raise ValueError ("{Need to pass list with value}")

        k= []
        for i in range(len(nums)):
            print(i)
            k.append(sum(nums[:i+1]))
        print(k)

#l = [1,2,3,4,5]
l= [3, 1, 2, 10, 1]
obj = Solution()
obj.runningSum(l)
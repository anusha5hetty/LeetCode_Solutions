# https://leetcode.com/problems/3sum/description/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        three_sum = []
        store = {}
        length = len(nums)-1

        for idx in range(length):
            for jdx in range(idx+1, len(nums)):
                if store.get(nums[jdx]):
                    val = store[nums[jdx]]
                    to_append = sorted([nums[val[0]], nums[val[1]], nums[jdx]])
                    # three_sum.append(to_append)
                    to_append not in three_sum and three_sum.append(to_append)
                    store.pop(nums[jdx])
                else:
                    sum1 = -(nums[idx] + nums[jdx])
                    store[sum1] = [idx, jdx]

        return three_sum
    
    def threeSumTwo(self, nums):
        three_sums = []
        length = len(nums)-2
        kdx = len(nums) - 1
        nums.sort()

        for idx in range(length):
            jdx = idx + 1            
            target = -(nums[idx])

            while jdx<kdx:
                two_sum = nums[jdx] + nums[kdx]
                if (two_sum==target):
                    three_sum = (nums[idx], nums[jdx], nums[kdx])
                    three_sums.append(three_sum)
                    jdx +=1
                    kdx -=1
                
                elif two_sum < target:
                    jdx +=1
                
                else:
                    kdx -=1

        return list(set(tuple(three_sums)))

        
print(Solution().threeSumTwo([-2,0,0,2,2]))

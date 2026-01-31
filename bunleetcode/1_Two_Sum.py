# # 1. Two Sum
class Solution:
    def twoSum(self,nums,target):
        lst=[]
        for i in nums:
            for j in range(len(nums)):
                if nums[j]!=i and i+nums[j]==target and nums.count(nums[j])==1:
                    lst.extend([nums.index(i),nums.index(nums[j])])
                elif i+nums[j]==target and nums.count(nums[j])!=1:
                        x=nums.index(nums[j],nums.index(nums[j])+1)
                        lst.extend([nums.index(i),x])
        return list(set(lst))
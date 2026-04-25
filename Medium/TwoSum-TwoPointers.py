# Link do problema: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Two Sum II - Input Array Is Sorted
#  nums = [2,7,11,15], target = 9 -> Output: [1,2]

def twoSum(nums, target):
   left = 0
   right = len(nums) - 1

   while left < right:
      soma = nums[left] + nums[right]
      
      if soma == target:
         return [left+1, right+1]
      
      if soma < target:
         left+=1
      else:
         right-=1
   return []

print(twoSum([2,7,11,15], 9))
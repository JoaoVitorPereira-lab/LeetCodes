# Two Sum
#  nums = [2,7,11,15], target = 9 -> Output: [0,1]

class Solution(object):
   def twoSum(self, nums, target):
      hasher = {}

      for idx, num in enumerate(nums):
         faltante = target - num

         if faltante in hasher:
            return [hasher[faltante], idx]
         
         hasher[num] = idx

      return []

resp = Solution()
print(resp.twoSum([2,5,11,7], 9))
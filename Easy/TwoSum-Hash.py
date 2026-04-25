# Link do problema: https://leetcode.com/problems/two-sum/description/

# Two Sum
#  nums = [2,7,11,15], target = 9 -> Output: [0,1]

def twoSum(nums, target):
      hasher = {}

      for idx, num in enumerate(nums):
         faltante = target - num

         if faltante in hasher:
            return [hasher[faltante], idx]
         
         hasher[num] = idx

      return []

print(twoSum([2,5,11,7], 9))
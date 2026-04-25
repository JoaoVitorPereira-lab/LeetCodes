# Link do problema: https://leetcode.com/problems/contains-duplicate/description/

# Contains Duplicate
# [1,2,3,1] = True & [1,2,3,4] = False

def contains_Dups(nums):
   hasher = {}

   for num in nums:
      hasher[num] = hasher.get(num, 0) + 1
      
      if hasher[num] == 2:
         return True
   return False     
   
            
print(contains_Dups([1,2,3,1]))
print(contains_Dups([1,2,3,4]))
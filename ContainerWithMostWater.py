# Container With Most Water
# [1,8,6,2,5,4,8,3,7] = 49

def containerWithMostWater(nums):
   left = 0
   right = len(nums) - 1
   areaMaior = 0

   while left < right:
      largura = right - left

      if nums[left] < nums[right]:
         altura = nums[left]
      else:
         altura = nums[right]
      
      area = largura * altura

      if area > areaMaior:
         areaMaior = area

      if nums[left] < nums[right]:
         left+=1
      else:
         right-=1

   return areaMaior

print(containerWithMostWater([1,8,6,2,5,4,8,3,7]))

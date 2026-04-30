# Link do problema: https://leetcode.com/problems/fruit-into-baskets/description/

# Fruit Into Baskets 
# fruits = [1,2,3,2,2] Output = 4
 
def fruitsInBaskets(fruits):
   left = 0
   window = {}
   biggerBasket = 0

   for right in range(len(fruits)):
      i = fruits[right]
      window[i] = window.get(i, 0) + 1

      while len(window) > 2:
         window[fruits[left]] -= 1
         if window[fruits[left]] == 0:
            window.pop(fruits[left])
         left += 1
         
      biggerBasket = max(biggerBasket, right - left + 1)

   return biggerBasket

print(fruitsInBaskets([1,2,3,2,2]))
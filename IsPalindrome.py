# Input: "A man, a plan, a canal: Panama"
# Output: True
# Input: "Ekitike" || Input: "Arara"
# Output: True

def isPalindrome(word):
   left = 0
   right = len(word) - 1

   while left < right:
      if not word[left].isalnum():
         left+=1
         continue
      if not word[right].isalnum():
         right-=1
         continue

      if word[left].lower() != word[right].lower():
         return False
      
      left+=1
      right-=1

   return True

print(isPalindrome("Ekitike"))
# Link do problema: https://leetcode.com/problems/valid-palindrome/description/

# Input: "A man, a plan, a canal: Panama" || "Arara"
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

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("Arara"))
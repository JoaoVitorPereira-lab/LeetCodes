# Link do problema: https://leetcode.com/problems/valid-anagram/description/

# Valid Anagram
# Input: s = "anagram", t = "nagaram" Output: True
# Input: s = "rat", t = "car" Output: False 

def isAnagram(s, t):
   hasher = {}

   for letter in s:
      hasher[letter] = hasher.get(letter, 0) + 1
   for letter in t:
      hasher[letter] = hasher.get(letter, 0) - 1

      if hasher[letter] < 0:
         return False
   return True

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
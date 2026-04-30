# Link do problema: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Longest Substring Without Repeating Characters
# s = "abcabcbb" Output: 3
# s = "pwwkew" Output: 3

def lengthOfLongestSubstring(s):
   left = 0
   window = set()
   maiorArray = 0   

   for letters in s:
      while letters in window: 
         window.discard(s[left])
         left+=1

      window.add(letters)

      if maiorArray < len(window): maiorArray = len(window)
   return maiorArray
         
print(lengthOfLongestSubstring("pwwkew")) 
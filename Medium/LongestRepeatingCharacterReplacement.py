# Link do problema: https://leetcode.com/problems/longest-repeating-character-replacement/

# Longest Repeating Character Replacement
# s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

def characterReplacement(s, k):
   left = 0
   window = {}
   maxFreq = 0
   resp = 0

   for right in range(len(s)):
      char = s[right]
      window[char] = window.get(char, 0) + 1

      maxFreq = max(maxFreq, window[char])

      while(right - left + 1) - maxFreq > k:
         window[s[left]]-=1
         left+=1
      
      resp = max(resp, right - left + 1)
   return resp

print(characterReplacement("AABABBA", 1))
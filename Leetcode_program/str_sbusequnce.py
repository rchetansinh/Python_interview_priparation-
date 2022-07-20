'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
 (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

    Input: s = "abc", t = "ahbgdc"
Output: true
Example
2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t
consist
only
of
lowercase
English
letters.
'''

#Method 1
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        print(len(s))
        if(len(s) == 0):
            return True
        for i in range(len(s)):
            if s[i] in t:
                #print(f"{s[i]} is present in {t[index +1]} at {t.index(s[i])}")
                #index = t.index(s[i])
                t=t[t.index(s[i]) +1 :]
                if i == (len(s) -1):
                    return True
            else:
                return False
'''
#Need to understand this logic
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j,n=0,len(t)
        for i in s:
            while j<n and t[j]!=i:
                j+=1
            if j>=n:
                return False
            j+=1
        return True



s = "abc"
#s = "aaaaaa"
t = "bbaabc"
obj = Solution()
print(obj.isSubsequence(s,t))

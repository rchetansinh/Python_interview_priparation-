'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''


class Solution:
    def isIsomorphic(self, str1: str, str2: str) -> bool:
        if (len(str1) != len(str2) ) :
            return False
        # initializing a dictionary
        # to store letters from str1 and str2
        # as key value pairs
        charCount = dict()
        # initially setting c to "a"
        c = "a"
        # iterating over str1 and str2
        for i in range(len(str1)):
            # if str1[i] is a key in charCount
            if str1[i] in charCount.keys():
                c = charCount[str1[i]]
                print ("c:",c)
                print(f"str2[{i}]",str2[i])
                if c != str2[i]:
                    return False
            # if str2[i] is not a value in charCount
            elif str2[i] not in charCount.values():
                charCount[str1[i]] = str2[i]
            else:
                return False
        return True


'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l= len(s)
        if l != len(t) : 
            return False
        
        d = {}
        for i  in range(l):
            if s[i] in d.keys():
                if d[s[i]] != t[i]:
                    return False
            elif t[i] not in d.values():
                d[s[i]] = t[i] 
            else:
                return False    
        return True
'''

#s = "egg"
#t = "add"

s = "aac"
t = "xxy"
obj = Solution()
print(obj.isIsomorphic(s,t))
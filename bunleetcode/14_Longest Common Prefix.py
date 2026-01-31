# 14. Longest Common Prefix
# class Solution:
#     def longestCommonPrefix(self, strs:list):
#         if not strs:
#             return ""
        
#         prefix = strs[0]
        
#         for word in strs[1:]:
#             while not word.startswith(prefix):
#                 prefix = prefix[:-1]
#                 print(prefix)
#                 if prefix == "":
#                     return ""
        
#         return prefix

# print(Solution().longestCommonPrefix(["flower","flow","flight"]))
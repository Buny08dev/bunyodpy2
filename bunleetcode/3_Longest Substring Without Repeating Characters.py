# # 3. Longest Substring Without Repeating Characters
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         lst=[]
#         a=lst.copy()
#         c=lst.copy()
#         for i in s:
#             if i not in lst:
#                 lst.append(i)
#             elif i in lst:
#                 a=lst.copy()
#                 c.append(a) 
#                 lst.clear()
#                 lst.append(i)
#         # d=[0]
#         # for i in c:
#         #     if len(i)>d[0]:
#         #         d.clear()
#         #         d.append(len(i))
#         # return d[0]
#         if c:
#             return 0
#         else:
#             return len(max(c,key=lambda x: len(x)))
# print(Solution().lengthOfLongestSubstring(""))
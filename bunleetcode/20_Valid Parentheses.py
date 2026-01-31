# 20. Valid Parentheses
################################## first try
# class Solution:
#     def isValid(self, s: str) -> bool:
#         qavs="([{}])"
#         while s:
#             if s[0] in qavs[:3]:
#                 start,end=s[0],qavs[-qavs.index(s[0])-1]
#                 print(start,end)
#                 try:
#                     if s.rindex(end)%2==1:
#                         s=s.replace(start,"",1)
#                         s=s[::-1].replace(end,"",1)
#                         s=s[::-1]
#                         print(s,"             ",s[::-1])
#                     else:
#                         return False,"1"
#                 except ValueError:
#                     return False,"2"
#             else:
#                 return False,"3"
#         return True
# print(Solution().isValid("[({(())}[()])]"))
######################################## Seocnd try +
# def isValid(s:str):
#     s=" ".join(s).split()
#     qavs="([{"
#     qavs_2=")]}"
#     strs=""
    
#     i=0
#     while s:
#         try:
#             if s[i] in qavs:
#                 strs=s[:i+1]
#                 i+=1
#                 # print(strs)
#                 # print(s)
#             elif s[i] in qavs_2:
#                 # print(s[i])
#                 # print(strs)
#                 # print(strs[-1]==qavs[qavs_2.index(s[i])])
#                 if strs[-1]==qavs[qavs_2.index(s[i])]:
#                     del s[i-1:i+1]
#                     del strs[-1]
#                     # print(s,s[i],i)
#                     # print(s)
#                     i-=1
#                 else:
#                     return False
#             else:
#                 return False      
#         except IndexError:
#             return False
#     else:
#         return True

# print(isValid("(){}}{"))
#################################### True answer
# def isValid(s: str) -> bool:
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}

#     for char in s:
#         if char in mapping.values():  # agar ochuvchi qavs bo'lsa
#             stack.append(char)
#         else:  # agar yopuvchi qavs bo'lsa
#             if not stack or stack[-1] != mapping[char]:
#                 return False
#             stack.pop()

#     return not stack
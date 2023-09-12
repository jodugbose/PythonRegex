# import re
# count = 0
# pattern=re.compile("ab")
# matcher=pattern.finditer("abaababa")
# for match in matcher:
#     count+=1
#     print(match.start(), "...", match.end(),"....",match.group())
#     print("The number of occurences:", count)

# import re
# count = 0
# matcher=re.finditer("ab","abaababa")
# for match in matcher:
#     count+=1
#     print(match.start(), "...", match.end(),"....",match.group())
#     print("The number of occurences:", count)

# import re
# matcher=re.finditer("[abc]","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())


# import re
# matcher=re.finditer("[a-zA-Z0-9]","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("[a-z]","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("[^abc]","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("[0-9]","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("[^a-zA-Z0-9]","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("\s","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("\S","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("\d","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("\D","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("\w","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("\W","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer(".","a7b@k9z")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("a","abaabaaab")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("a+","abaabaaab")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("a*","abaabaaab")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("a?","abaabaaab")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("a{3}","abaabaaab")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# matcher=re.finditer("a{2,4}","abaabaaab")
# for match in matcher:
#     print(match.start(), "...", match.end(),"....",match.group())

# import re
# s=input("Enter pattern to check: ")
# m=re.match(s,"abcabdefg")
# if m != None:
#     print("Match is available at the beginning of the string")
#     print("Start Index:", m.start(), "and End Index:", m.end())
# else:
#     print("Match is not available at the beginning of the string")

# import re
# s=input("Enter pattern to check:")
# m=re.fullmatch(s,"ababab")
# if m != None:
#     print("Full String Matched")
# else:
#     print("Full String not Matched")

# import re
# s=input("Enter pattern to check: ")
# m=re.search(s,"abaaaba")
# if m != None:
#     print("Match is available")
#     print("First Occurrence of match with start index",m.start(), "and end index",m.end())
# else:
#     print("Match is not available at the beginning of the string")

# import re
# l=re.findall("[0-9]","a7b9c5kz")
# print(l)

# import re
# s=re.sub("[a-z]","#","a7b9c5k8z")
# print(s)

# import re
# t = re.subn("[a-z]","#","a7b9c5k8z")
# print(t)
# print("The Result String:",t[0])
# print("The number of replacements:", t[1])

# import re
# l=re.split("\d", "KGF,BB1,BB2")
# print(l)
# for t in l:
#     print(t)

# import re

# with open("input.txt","r") as d:
#     for line in d:
#         items = re.findall("[7-9]\d{9}",line)
#         with open("output.txt", "w") as g:
#             for n in items:
#                 g.write(n+"\n")
#     print("extracted all mobile numbers into output.txt")

# import re
# s = input("Enter Mail Id:")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# if m!=None:
#     print("Valid Mail id")
# else:
#     print("Invalid Mail id")

# import re
# s = input("Enter Mail Id:")
# m=re.fullmatch("\w.*@gmail[.]com",s)
# if m!=None:
#     print("Valid Mail id")
# else:
#     print("Invalid Mail id")
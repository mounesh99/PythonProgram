import re
str=input()
str_list=re.findall("[a-zA-Z]",str)
str_list.reverse()
for i in range(len(str)):
    if str[i]=='#' or str[i]=='@':
        str_list.insert(i,str[i])
res=''.join(str_list)
print(res)

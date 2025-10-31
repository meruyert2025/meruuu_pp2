import re
str="sugiii 77588055925 77845687674 77845698003"
a=r'\b\d{11}\b'
print (bool(re.findall(a,str)))


# import re 
# str="ngrjg_fnejk_ ngrjg_fnejk"
# print(re.sub("_","15",str))


# import re
# str="abdigaliyeva.meruyert@bk.ru"
# a=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
# b=re.match(a,str)
# if b:
#     print("right")
# else:
#     print("no")



# import re
# str="ajsjdj_dkdkdk_mdekd"
# print(re.split("_",str))


# import re
# str="MeruyertOutWorld"
# s=r'([a-z0-9])([A-Z])'
# s1=r"\1 \2"
# print((re.sub(s,s1,str)))


import re
str="x"
r=re.match('xy*',str)
if r:
    print("true")
else:
    print("false")

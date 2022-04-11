num=[1,3,2,4,5,3,5,6,7]
lis=[]
val=[]
for i in num:
    if i not in lis:
        lis.append(i)
    else:
        val.append(i)
print(lis)
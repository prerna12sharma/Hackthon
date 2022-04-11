list1=[1,2,3]
list2=[4,5,6]
l=[]
sum=0
# i=0
# while i<len(list1):
#     sum=list1[i]+list2[i]
#     l.append(sum)
#     i+=1
# print(l)

for i in range(len(list1)):
    sum=list1[i]+list2[i]
    l.append(sum)
print(l)

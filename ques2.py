list1=[1,3]
list2=[2]
l=[]
sum=list1+list2
sum.sort()
i=0
while i<len(sum):
    s=i//2
    i+=1
print(sum[s])



num=[1,2,3,4]
sum=0
l=[]
i=0
while i<len(num):
    if i==2:
        break
    l.append(i)
    sum=sum+num[i]
    l.append(i)
    
    i+=1
print(i)
def mul(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if target-num[i]==num[j]:
                return [i,j]
test=[2,4,3,5]
target=7
print(mul(test,target))
def fun():
    sum=[]
    list=[[1,2,3],[1,2],[3,4,5]]
    for i in range(len(list)):
        sum=sum+list[i]
        sum.sort()
    print(sum)
fun()
num=int(input("enter your num"))
rev=0
x=num
while num>0:
    rev=(rev*10)+num%10
    num//=10
if x==rev:
    print("palindrom",rev)
else:
    print("no")
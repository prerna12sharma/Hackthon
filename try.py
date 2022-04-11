# a="sam"
# b="7.2"
# c="12"
# d=float(b)
# e=int(d)
# # print(e)
# print(a+c+str(e))

# a=int(input("enter"))
# b=int(input("enter"))
# c=input("enter")
# if c=="+":
#     d=a+b
#     print(d)

# num=int(input("enter"))
# if num%5==0 and num%11==0:
#     print(num,"divisible")
# else:
#     print("not")

# num=int(input("enter"))
# num2=int(input("enter"))
# num3=int(input("enter"))
# if num>num2 and num>num3:
#     print("num is greatrer")
# elif num2>num and num2>num3:
#     print("num2 is graeter")
# elif num3>num and num3>num2:
#     print("num3 is graeter")
# else:
#     print("all are equal")

# a="prerna"
# s=""
# c=0
# for i in a:
#     if a[i]=="":
#         c+=1
#     print(c)

# list=[10,20,[30,34],30,30]
# i=0
# c=0
# lis=[]
# while i <len(list):
#     j=0
#     while j<len(i):
#         if list[i] not in lis:
#             lis.append(list[i])
#     # else:
#     #     lis.append(list[i])
#         j+=1
#     i+=1
# print(lis)

# a=[10,20,35]
# i=0
# max=0
# smax=0
# thmax=0
# while i<len(a):
#     if a[i]>max:
#         thmax=smax
#         smax=max
#         max=a[i]
#     if a[i]<smax and a[i]>smax:
#         smax=a[i]
#     i=i+1
# print(thmax)
# print(smax)
# print(max)

# def sum(a,b):
#     c=a+b
#     return c
# def mul(c,d):
#     f=c*d
#     return f
# print(mul(3,4))
    
# x=lambda a,b:   a*b
# print(x(4,3))

# def add(n):
#     print(n)
#     if n ==10:
#         return 1
#     return add(n+1)
# n=int(input("enter"))
# add(n)

# def add():
#     def sub():
#         print("nav")
#     print("gurukul")
#     sub()
# add()

# file=open("stu.txt","x")
# file.write("prerna")
# file.write("sharma")
# file.close()

a={"a":2,"b":3,"c":5}
import json
# max=0
# smax=0
# thmax=0
# m=0
# s=0
# th=0
# for i in a:
#     if a[i]>max:
#         thmax=smax
#         smax=max
#         max=a[i]
#     elif a[i]>smax:
#         thmax=smax
#         smax=a[i]
#     elif a[i]>thmax:
#         thamx=a[i]
# print(max,smax,thmax)

with open("file.json","w") as file:
    json.dump(a,file,indent=2)  
        



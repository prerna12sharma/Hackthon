x=123
i=0
while x>0:
    i=(i*10)+x%10
    x//=10
print(i) 
list1=input().split(",")
l=[]
for i in list1:
    if(int(i)>0):
        l.append(i)
print(*l)    

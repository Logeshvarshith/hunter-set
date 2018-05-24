n=int(input("enter the number:"))
a=[]
for i in range(0,n):
  b=int(input())
  a.append(b)
for i in a:
  if(a.count(i)!=1):
    print(i)
    break
    

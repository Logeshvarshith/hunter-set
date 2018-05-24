n=int(input("enter the number:"))
a=[]
for i in range(0,n):
  b=int(input())
  a.append(b)
a.sort()
b=a[::-1]
print("".join(str(x)for x in b))

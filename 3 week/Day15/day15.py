

######### On how many buildings sun rays will fall from left to right and right to left
# arr=[3,5,9,6,11,2]
# l=[0]*len(arr)
# r=[0]*len(arr)
# m=0
# for i in range(len(arr)):
#     if(arr[i]>m):
#         m=arr[i]                                      
#     l[i]=m
# print(l)
# m1=0
# for i in range(len(arr)-1,-1,-1):
#     if(arr[i]>m1):
#         m1=arr[i]
#     r[i]=m1
# print(r)
# l=set(l)
# k=len(l)
# r=set(r)
# v=len(r)
# print(k+v)




#############single coins possible for the list so that sum will make n value##########
'''l=[2,3,5,6]
op:11'''
l=list(map(int,input().split()))
t=int(input())
m=[]
for i in range(len(l)+1):
    m.append([0]*(t+1))
    m[0][0]=1
for i in range(1,len(l)+1):
    for j in range(t+1):
        if j==0:


            m[i][j]=1
        elif l[i-1]>j:
            m[i][j]=m[i-1][j]
        else:
            if m[i-1][j]==0:
                x=j-l[i-1]
                m[i][j]=m[i-1][x]
            else:
                m[i][j]=m[i-1][j]
print(m)
if m[len(l)][t]==1:
    print("yes")
else:
    print("no")








########################even maximum possible number###################
# a="tu5g3k1h8"
# b="g5g8gd6h3"
# l=[]
# v=[]
# y=[]
# for i in a:
#     if not(i.isupper() or i.islower()):
#         l.append(int(i))
# for i in b:
#     if not(i.isupper() or i.islower()):
#         v.append(int(i))
# r=""

# s=set(l+v)
# s=list(s)
# print(s)
# q=sorted(s)
# w=q[::-1]

# print(w)
# for i in w:
#     r=r+str(i)

# if int(r[-1])%2==0:
#     print(r)
# else:
#     for i in range(len(w)-2,-1,-1):
#         if(int(w[i])%2==0):
#             w.append(w.pop(i))
#             f=[str(num) for num in w]
#             print(''.join(f))
#             break
#     else:
#         print(-1)





########################even maximum possible number###################
# a=input()
# b=input()
# c=set()
# for i in a:
#     if(i.isdigit()):
#         c.add(i)
# for i in b:
#     if(i.isdigit()):
#         c.add(i)
# d=list(sorted(c,reverse=True))
# if(int(d[-1])%2==0):
#     print(''.join(d))
# else:
#     for i in range(len(c)-2,-1,-1):
#         if(int(d[i])%2==0):
#             d.append(d.pop(i))
#             print(''.join(d))
#             break
#     else:
#         print(-1)







# def pal(n):
#     temp=str(n)
#     if(temp==temp[::-1]):
#         return n
        
   
#     else:
#         while(1):
#             n=n+1
#             return pal(n)

# n=76583
# print(pal(n))





############printing nearest palindrome for the number with less TC############
m=int(input())
n=m
z=""
z1=""
def palin(n):
    rev=0
    while n>0:
       r=n%10
       rev=rev*10+r
       n=n//10
    if rev==m:
        return 1
    else:
       return 0
if palin(n):
    print(m)
else:
    x=str(m)
    if len(x)%2==0:
        y=x[:len(x)//2]
        y=y+"".join(reversed(y))
        if int(y)>m:
            print(y)
        else:
            y=x[:len(x)//2]
            y=int(y)+1
            y=str(y)
            y=y+"".join(reversed(y))
            print(y)
    else:
        y=x[:len(x)//2]
        z=z+"".join(reversed(y))
        y=y+(x[(len(x)//2)])
        y=y+z
        if int(y)>m:
            print(y)
        else:
            y=x[:len(x)//2]
            z1=z1+"".join(reversed(y))
            y=y+str(int((x[(len(x)//2)]))+1)
            y=y+z1
            print(y)
    








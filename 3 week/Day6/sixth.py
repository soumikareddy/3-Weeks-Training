# l=[6,6,6,6,7]
# p=len(l)//2
# v=[]
# for i in l:
#     if l.count(i)>p and i not in v:
#         v.append(i)
# for i in v:
#     print(i)



# l=[6,6,6,7,7,7,7,7,7]
# p=len(l)//2
# cc={}
# for i in l:
#     if i in cc:
#         cc[i]+=1
#     else:
#         cc[i]=1
# for i in l:
#     if cc[i]>p:
#         print(i)
#         break




# a=[1,1,2,1,1,3]
# c=1
# p=a[0]
# for i in range(1,len(a)):
#     if(a[i]==p):
#         c=c+1

#     else:
#         if(c!=0):
#             c=c-1
#         if(c==0):
#             c=1
#             p=a[i]
# print(p)





# n=10
# l=[0,1,2,5,4,3,6,7,8,9]
# for i in range(n+1):
#     if i not in l:
#         print(i)
#         break










# a=l=[0,1,2,5,4,3,6,7,8,10]
# n=10
# b=sum(a)
# n=n*(n+1)//2
# print(n-b)



# n=12
# l=[]
# k=4
# max1=0
# for i in range(1,n+1):
#     if n%i==0:
#         l.append(i)
# print(l)
# v=l[-k:-k+1]
# for i in v:
#     print(i)





# n=int(input())
# k=int(input())
# c1=0
# c=0
# if k==1:
#     print(n)
# else:
#     for i in range(n,0,-1):
#         if n%i==0:
#             c1=c1+1
#             if c1==k:
#                 print(i)
#                 break







# n=21
# k=25
# l=[]
# v=[]
# s=[]
# for i in range(1,n+1):
#     if n%i==0:
#         l.append(i)
# for j in range(1,k+1):
#     if k%j==0:
#         v.append(j)
# print(l)
# print(v)
# for i in l:
#     for j in v:
#         if(i==j):
#             s.append(i)
#         else:
#             continue
# if len(s)==1:
#     print("co prime")
# else:
#     print("not a co prime")







# import math
# a=21
# b=27
# print(math.gcd(a,b))
# if(math.gcd(a,b)==1):
#     print("co prime")
# else:
#     print("not a co prime")




# a=5
# b=10
# for i in range(2,(min(a,b)//2)+1):
#     if(a%i==0 and b%i==0):
#         print("not a co prime")
#         break
# else:
#     print("co prime")









# a = "(([{]))"
# s = []
# f = 0
# c = 0

# for i in a:
#     if i in '{[(':
#         s.append(i)
#     elif not s:
#         print(c)
#         f = 1
#         break
#     else:
#         if (i == '}' and s[-1] == '{') or (i == ']' and s[-1] == '[') or (i == ')' and s[-1] == '('):
#             s.pop()
#         else:
#             print(c)
#             f = 1
#             break
#     c += 1

# if f == 0:
#     if s:
#         print(c)
#     else:
#         print("-1")

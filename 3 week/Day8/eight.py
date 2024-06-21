








################## n*4 is time complexity ###############

# l=[2,3,4,1,3,2,4,2,1,3]
# p=[]
# c=0

# while(c!=len(l)):
#     r=[]
#     for i in range(len(l)):
#        if(not str(l[i]).isalpha()):
#            if(l[i] not in r):
#                c=c+1
#                r.append(l[i])
#                l[i]='a'
#     p.append(r)
# print(p)
               





# l=[2,3,4,1,3,2,4,2,1,3]
# s=[]
# d={}
# c=0
# for i in l:
#     if(i not in d):
#        d[i]=1
#     else:
#         d[i]=d[i]+1
# while(c!=(len(l))):
#     a=[]
#     for i in d: 
#         if d[i]!=0:
#             d[i]=d[i]-1
#             a.append(i)
#             c+=1
#     s.append(a)
# print(s)






# s="qwweer yuiop asdfvgh jkl mnbvlkjcxz"
# s=set(s)
# print(s)
# if len(s)==27:
#     print("yes")
# else:
#     print("no")



# s="the 4quick br$%^own foENDx j45umps o.ver the lazy dg"
# s=set(s)
# print(s)
# c=0
# for i in s:
#     if i.islower():
#         c=c+1
# if(c==26):
#     print("yes")
# else:
#     print("no")




# a=input()
# b="abcdefghijklmnopqrstuvwxyz"
# for i in b:
#     if i not in a:
#         print("no")
#         break
# else:
#     print("yes")



# a=input()
# b=97
# for i in range(b,123):
#     if(chr(i) not in a):
#         print("no")
#         break
# else:
#     print("yes")



# a=input()
# d=[0]*26
# for i in a:
#     if i.islower():
#         d[ord(i)-97]+=1
# print(d)




# a=input()
# d=[0]*26
# for i in a:
#     if i.islower():
#         d[ord(i)-97]+=1
# print(all(d))









# a = "abfgresagtyuiofdb"
# d = {}
# s = ""
# i = 0
# m = 0

# while i < len(a):
#     while i < len(a):
#         if a[i] not in s:
#             s += a[i]
#             d[a[i]] = i  
#         else:
#             if len(s) > m:
#                 m = len(s)
#             s = ""
#             break
#         i += 1
#     if i < len(a):  
#         i = d[a[i]] + 1

# if len(s) > m:
#     m = len(s)

# print(m)













# 6
# 0 1 1 1 0 1
# 0 1 0 1 0 0
# 1 0 1 1 0 0
# 0 0 0 1 1 1
# 1 1 0 0 0 1
# 1 1 1 0 1 0
# 4 6
# o/p: 8





# l=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
# n=int(input())
# l=[]

# for i in range(n):
#     l1=[]
#     for j in range(n):
#         l1.append(int(input()))
#     l.append(l1)
# print(l)





"""
ip: 6
    0 1 1 1 0 1
    0 1 0 1 0 0
    1 0 1 1 0 0 
    0 0 0 1 1 1
    1 1 0 0 0 1 
    1 1 1 0 1 0 
    4 6

op: 8
"""

# def fun(l,i,j,n): 
#     if(i<0 or j<0 or i>=n or j>=n or l[i][j]!=1):
#         return
#     if l[i][j]==1:
#         l[i][j]=2
#     fun(l,i-1,j,n)
#     fun(l,i,j-1,n)
#     fun(l,i+1,j,n)
#     fun(l,i,j+1,n)
#     return 

# n=int(input())
# l=[]
# co=0
# for i in range(n):
#     l1=[]
#     for j in range(n):
#         l1.append(int(input()))
#     l.append(l1)
# r=int(input())
# c=int(input())  
# fun(l,r-1,c-1,n) 
# for i in range(n):
#     for j in range(n):
#         if l[i][j]==1:
#             co=co+1
# print(l)
# print("Trees:",co)

# 6
# 0
# 1
# 1
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 0
# 0
# 1
# 0
# 1
# 1
# 0
# 0
# 0
# 0
# 0
# 1
# 1
# 1
# 1
# 1
# 0
# 0
# 0
# 1
# 1
# 1
# 1
# 0
# 1
# 0
# 4 
# 6
# [[0, 2, 2, 2, 0, 1], [0, 2, 0, 2, 0, 0], [1, 0, 2, 2, 0, 0], [0, 0, 0, 2, 2, 2], [1, 1, 0, 0, 0, 2], [1, 1, 1, 0, 1, 0]]
# Trees: 8












# def fun(i,j,k,t):
#     if(k==len(s)):
#         return 1
#     if(i<0 or j<0 or i>=n or j>=n or a[i][j]!=s[k]):
#         return
#     if(a[i][j]==s[k]):
#         a[i][j]=0
#     t=fun(i+1,j,k+1)
#     t=fun(i-1,j,k+1)
#     t=fun(i,j-1,k+1)
#     t=fun(i,j+1,k+1)
#     return t



# fun(i,j,1,0)




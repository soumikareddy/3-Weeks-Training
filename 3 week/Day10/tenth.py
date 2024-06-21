# def prime(x):
#     for i in range(2,(x//2)+1):
#         if(x%i==0):
#             return 0
#     return 1

# def fun(i,j):  
#     for k in range(j-1,i,-1):
#         if prime(k):
#             return k
#     return 0
# l=list(map(int,input().split()))
# s=0
# for i in range(len(l)-1): 
#     s=s+fun(l[i],l[i+1])
# print(s)




# a=input().split()
# print(a)
# a=list(map(int,a))
# print(a)






# [4,9,8,2,14,3,5,6]
# 4 8 9 2 14 3 5 6
#   2 8 9
#     8 9 14
#       3 9 14


# 4 2 8 3 5 6 9 14


# a=list(map(int,input().split()))
# for i in range(len(a)-2):
#     if(a[i]>a[i+1]):
#         a[i],a[i+1]=a[i+1],a[i]
#     if(a[i+1]>a[i+2]):
#         a[i+1],a[i+2]=a[i+2],a[i+1]
#     if(a[i]>a[i+1]):
#         a[i],a[i+1]=a[i+1],a[i]
# print(a)
    

# a[0]=min(9,8,1)
# a[2]=max(9,8,1)
# a[1]=s-a[2]-a[0]


  









# cc={
    # "hello":5438,
    #  "car":214,
    #  "book":8799,
    #  "apple":2187

# }
# y=""
# for i,c in cc.items():
#     k=len(i)
    
#     if str(k) in str(c):
#         print(i[k-1:k-1+1])
#         y=y+i[k-1:k-1+1]
#     elif str(k-1) in str(c):
#         print(i[k-2:k-2+1])
#         y=y+i[k-2:k-2+1]
#     elif str(k-2) in str(c):
#         print(i[k-3:k-3+1])
#         y=y+i[k-3:k-3+1]
#     elif str(k-3) in str(c):
#         print(i[k-4:k-4+1])
#         y=y+i[k-4:k-4+1]
    
#     else:
#         print("x")
#         y=y+"x"
# print(y)






# a=input().split(',')
# print(a)
# s=''
# for i in a:
#     print(i)
#     b=i.split(":")
#     print(b)
#     l=len(b[0])
#     if(str(l) in b[1]):
#         s=s+b[0][-1]
#     else:
#         for i in range(l-1,0,-1):
#             if(str(i) in b[1]):
#                 s=s+b[0][i-1]
#                 break
#         else:
#             s=s+'x'
# print(s)




































































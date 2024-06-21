
#####################Trapping Water###########################



#      |   |
#     ||   |
#  |  ||  ||
#  |  ||  ||
#  | |||  ||
# ||||||  ||
# ||||||| ||


# arr=[0,1,0,2,1,0,1,3,2,1,2,1]
# l=[0]*len(arr)
# r=[0]*len(arr)
# m=0
# for i in range(len(arr)):
#     if(arr[i]>m):
#         m=arr[i]                                      
#     l[i]=m
# m1=0
# for i in range(len(arr)-1,-1,-1):
#     if(arr[i]>m1):
#         m1=arr[i]
#     r[i]=m1
# s=0
# for i in range(len(arr)):
#     s=s+abs(min(l[i],r[i])-arr[i])
# print(s)











##################### wrong code Dont try this code below one is correct code ##########################
# l=list(map(int,input().split()))
# n=int(input())
# dp=[]
# for i in range(len(l)):
#     a=[0]*(n+1)
#     dp.append(a)
# for i in range(len(l)):
#     for j in range(len(a)):
#         if l[i]>j:
#             if i==0:
#                 dp[i][j]=0
#             else:
#                 dp[i][j]=dp[i-1][j] 
#         elif l[i]==j:
#             dp[i][j]=1 
#         else:
#             m=j-l[i]
#             v=dp[i][m]+1 
#             if i==0:
#                 dp[i][j]=v
#             else: 
#                 dp[i][j]=min(dp[i-1][j],v)
            
# print(dp)
# print(dp[len(l)-1][n])











###################### minimum coins possible to get the n value ##############
# def fun():
#     l1=[-1]*(n+1)
#     l1[0]=0
#     for i in l:
#         for j in range(1,n+1):
#             if(j>=i):
#                 if(l1[j-i]!=-1):
#                     if(l1[j]!=-1):
#                         l1[j]=min(l1[j],l1[j-i]+1)
#                     else:
#                         l1[j]=l1[j-i]+1
#     print(l1)
#     print(l1[-1])
# l=[1,3,4,5]
# n=17
# fun()









##############down right paths#####
# def paths(m,n):
#     if m==1 and n==2:## This is obstacle
#         return 0
#     elif m==1 or n==1:
#         return 1
#     elif m==0 or n==0:
#         return 0
    
#     else:
#         return paths(m-1,n)+paths(m,n-1)
# print(paths(4,3))



###########All possible paths#################3333
# def fun(i,j,c):
#     if(i<0 or i>=n or j>=m or j<0): #or(i == k and j == l):
#         return c
#     if (i==n-1 and j==m-1):
#         c = c+1
#         return c
#     vi.append((i,j))
#     if((i-1,j) not in vi):
#         c = fun(i-1,j,c)
#     if((i+1,j) not in vi):
#         c = fun(i+1,j,c)
#     if((i,j-1) not in vi):
#         c = fun(i,j-1,c)
#     if((i,j+1) not in vi):
#         c = fun(i,j+1,c)
#     vi.pop()
#     return c
# n = int(input())
# m = int(input())

# vi=[]
# print(fun(0,0,0))







# #############Nqueen problem#################
# def Nqueen(board,r):
#     if r==len(board):
#         return True
#     for c in range(len(board)):
#         if issafe(board,r,c):
#             board[r][c]="1"
#             if Nqueen(board,r+1):
#                 return True
#             board[r][c]='0'
    
# def issafe(board,r,c):
#     for i in range(r):
#         if board[i][c]=="1":
#             return False
#     i,j=r,c
#     while i>=0 and j<len(board):
#         if board[i][j]=="1":
#             return False
#         i=i-1
#         j=j+1
#     i,j=r,c
#     while i>=0 and j>=0:
#         if board[i][j]=="1":
#             return False
#         i=i-1
#         j=j-1
#     return True
# n=int(input("enter number of queens:"))
# board=[["0" for i in range(n)] for j in range(n)]
# print(board)
# if Nqueen(board,0):
#     for i in board:
#         print("".join(i))
# else:
#     print(False)





##################Nquuen with rook################
# def queen(r):
#     if(r==n):
#         return 
#     for c in range(n):
#         if(check(r,c)):
#             m[r][c]=1
#             break
#     return queen(r+1)
# def check(i,j):
#     if(i==u):
#         return 0
#     elif(j==v):
#         return 0
#     r,c=i,j
#     for i in range(r+1):
#         if(m[i][j]==1):
#             return 0
#     i=r
#     while(i>=0 and j>=0):
#         if(m[i][j]==1):
#             return 0
#         i=i-1
#         j=j-1
#     while(r>=0 and c<n):
#         if(m[r][c]==1):
#             return 0
#         r=r-1
#         c=c+1
#     return 1
   
# n=5
# u=1
# v=3
# m=[]
# for i in range(n):
#     m.append([0]*n)

# queen(0)
# print(m)




##############################Nqueen with rook########
# def Nqueen(board,r,r1,c1,co):
#     if r==len(board):
#         return co
#     if r!=r1:
#         for c in range(len(board)):
#             if issafe(board,r,c,c1):
#                 board[r][c]="1"
#                 co=co+1
#                 break
        
#             board[r][c]='0'
#         return Nqueen(board,r+1,r1,c1,co)

#     else:
#         return Nqueen(board,r+1,r1,c1,co)
# def issafe(board,r,c,c1):
#     for i in range(r):
#         if c==c1:
#             return False
#         if board[i][c]=="1":
#             return False
        
#     i,j=r,c
#     while i>=0 and j<len(board):
#         if board[i][j]=="1":
#             return False
#         i=i-1
#         j=j+1
#     i,j=r,c
#     while i>=0 and j>=0:
#         if board[i][j]=="1":
#             return False
#         i=i-1
#         j=j-1
#     return True
# n=int(input("enter number of queens:"))
# r1=int(input())
# c1=int(input())
# board=[["0" for i in range(n)] for j in range(n)]
# print(Nqueen(board,0,r1,c1,0))
# for i in board:
#         print("".join(i))







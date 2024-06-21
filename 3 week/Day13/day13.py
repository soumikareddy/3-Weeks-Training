

################job scheduling#######################333

# l=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
# a=[5,6,5,4,11,2]
# b=a.copy()
# print(b)
# for i in range(1,len(a)):
#     for j in range(0,i):
#           if l[j][1]<=l[i][0]:
#                if b[j]+a[i]>b[i]:
#                    b[i]=b[j]+a[i]
          
# print(max(b))

# print(b)





######################Longest common sub sequence########################
# """
# ip: abcd
#     axbd
    
# op: 3
# # """
# s=""
# a=input()
# b=input()
# dp=[]
# u=len(a)
# v=len(b)
# for i in range(len(a)+1):
#     l=[0]*(len(b)+1)
#     dp.append(l)
# for i in range(1,len(a)+1):
#     for j in range(1,len(b)+1):
#         if a[i-1]==b[j-1]:
#             dp[i][j]=dp[i-1][j-1]+1
#         else:
#             dp[i][j]=max(dp[i][j-1],dp[i-1][j])
# while u>0 and v>0:
#     if(a[u-1]==b[v-1]):
#         s=s+a[u-1]
#         u=u-1
#         v=v-1
#     else:
#         if dp[u][v]==dp[u][v-1]: 
#             v=v-1
#         else:
#             u=u-1
# print(s[::-1])
# print(dp[len(a)][len(b)])











# ################no of of ilands in the list land=1 and water=0###########
# #lands should not be diagonal and also print higehst area
# """
# ip:  5
#      some numbers
# 5
# 0
# 1
# 0
# 0
# 1
# 1
# 0
# 0
# 1
# 1
# 0
# 0
# 0
# 0
# 0
# 1
# 0
# 0
# 0
# 0
# 1
# 0
# 0
# 0
# 1

# op:  5 and 3
# """


# def fun(l,i,j,co): 
    # if(i<0 or j<0 or i>=n or j>=n or l[i][j]!=1):
    #     return co
    # if l[i][j]==1:
    #     l[i][j]=2
    #     co=co+1
    # co=fun(l,i-1,j,co)
    # co=fun(l,i,j-1,co)
    # co=fun(l,i+1,j,co)
    # co=fun(l,i,j+1,co)
    # return co

# n=int(input())
# l=[]
# for i in range(n):
#     a=[]
#     for j in range(n):
#         a.append(int(input()))
#     l.append(a) 
# count=0
# m=0
# for i in range(n):
#     for j in range(n):
#         if l[i][j]==1:
            
#             k=fun(l,i,j,0)
#             if(k>m):
#                 m=k
#             count+=1

# print("Number of Islands and highest area:",count,"and",m)







# # n=500
# n=7262
# h=n//3600
# a=(n%3600)
# mi=a//60
# sec=a%60
# print(h,"h:",mi,"m:",sec,"s")






# n = 65476
# year_length = 360
# month_length = 30
# week_length = 6

# years = n // year_length
# remainder = n % year_length


# months = remainder // month_length
# remainder = remainder % month_length


# weeks = remainder // week_length


# days = remainder % week_length


# print(f"{years} years, {months} months, {weeks} weeks, {days} days")



















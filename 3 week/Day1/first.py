# l=list(map(int,input().split()))
# m=list(map(int,input().split()))
# k=l+m
# k.sort()
# print(k)





# l=[1,5,8,9]
# m=[2,7,9,10,14]
# c=[]
# i=0
# j=0
# while i<len(l) and j<len(m):
#     if l[i]<m[j]:
#         c.append(l[i])
#         i=i+1
        
#     else:
#         c.append(m[j])
#         j=j+1
# # while(j<len(m)):
# #     c.append(m[j])
# #     j=j+1
# # while(i<len(l)):
# #     c.append(l[i])
# #     i=i+1
# if(j<len(m)):
#     c.extend(m[j:])
# if(i<len(l)):
#     c.extend(l[i:])
# print(c)








# s="aaabbaaaaddd"
# cc={}
# count=0
# for i in s:
#     if i in cc:
#         cc[i]+=1
#     else:
#         cc[i]=1
# for i,count in cc.items():
#     print(i,count)














# s="aaabbaaaadddbb"
# c=1
# b=' '
# for i in range(len(s)-1):
#     if s[i]==s[i+1]:
#         c=c+1
#     else:
#         b=b+s[i]+str(c)
#         c=1
# b=b+s[i+1]+str(c)
# print(b)   










# l=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
# cc={}

# for i in l:
#     if i in cc:
#         cc[i]+=1
#     else:
#         cc[i]=1
# for i,count in cc.items():
#     print(i,"-",count)










# a=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
# b=[]
# for i in a:
#     if(i not in b):
#         b.append(i)
# for i in b:
#     print(i,"-",a.count(i))











# a="f46feLK9y56u#@&56hIjbn6KJhA"
# uv,uc,lv,lc,d,s=0,0,0,0,0,0
# for i in a:
#     if(i.isupper()):
#         if(i in 'AEIOU'):
#             uv=uv+1

#         else:
#             uc=uc+1
#     elif (i.islower()):
#         if(i in 'aeiou'):
#             lv=lv+1
#         else:
#             lc=lc+1
#     elif(i.isdigit()):
#         d=d+1
#     elif(not i.isalnum()):
#         s=s+1
# print("uv","-",uv)
# print("uc","-",uc)
# print("lv","-",lv)
# print("lc","-",lc)
# print("d","-",d)
# print("s","-",s)








# s="PlacemEnts"
# s3=""
# s1="aeiou"
# s2="AEIOU"
# for i in s:
#     if i.islower():
#         if i not in s1 :
#             s3+=i
#         else:
#             x=i.upper()
#             s3+=x
#     if i.isupper():
#         if i not in s2 :
#             x=i.lower()
#             s3+=x
#         else :
#             s3+=i
# print(s3)



























# l=[5,3.8,7,5.6,4,2,3]
# sum1=0
# sum2=0
# sum3=0
# for i in l:
#     if i%2==1:
#         sum1=sum1+i
#     elif i%2==0:
#         sum2=sum2+i
#     else:
#         sum3=sum3+i
    
# print(sum1,sum2,sum3)






# l=300
# m=400
# count=0
# for i in range(l,m+1,7):

#     # if i%7==0:
#     count=count+1
#         # print(i)
# print(count)



# l=300
# m=400
# print(abs((300/7)-(400/7)))













# n=int(input())
# while(1):
#     c=0
#     for i in range(2,(n//2)+1):
#         if(n%i==0):
#             c=c+1
#             break
#     if c==0:
#         print(n)
#         break
#     else:
#         n=n+1







# n=int(input())
# c=0
# while(n):
#     if(n%10 in[2,3,5,7]):
#         c=c+1
#     n=n//10
# print(c)




# n=input()
# c1,c2,c3,c4=0,0,0,0

# for i in n:
#     if i.isupper():
#         c1=1
#     elif i.islower():
#         c2=1
#     elif i.isdigit():
#         c3=1
#     else:
#         c4=1
# c=4-(c1+c2+c3+c4)
# if(len(n)+c)<8:
#     print(8-len(n))
# else:
#     print(c)











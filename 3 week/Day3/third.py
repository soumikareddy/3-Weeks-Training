# s="bcdmnwc"
# k=3
# l=[]
# p=[]
# v=[]
# str=" "
# for i in s:
#     l.append(ord(i)-96)
# for i in l:
#     p.append(i-3)


# print(p)

# for i in p:
#     v.append(chr(i+96))
# print("".join(v))  


       










# a="bvec"
# b=30
# c=b%26
# d=''
# for i in a:
#     if((ord(i)-c)>=97):
#         d=d+chr(ord(i)-c)
#     else:
#         d=d+chr(ord(i)-c+26)
# print(d)






# s="abcde"
# c=1
# s=list(s)
# max1=0
# for i in range(len(s)-1):
#     if ord(s[i+1])-ord(s[i])==1:
#         c=c+1
#         max1=max(max1,c)
#     else:
#         c=1
    
# print(max1)





# n=int(input())


# l=[]
# for i in range(n):
#     l.append(input())
# print(l)
# s=input()
# f=0
# for i in range(len(s)):
#     if(s[i] in l[i%n]):
#         continue
#     else:
#         f=1
#         break
# if(f==1):
#     print("no")
        
# else:
#     print("yes")










# n=int(input())


# l=[]
# for i in range(n):
#     l.append(list(input()))
# print(l)
# s=input()
# f=0
# for i in range(len(s)):
#     if(s[i] not in l[i%n]):
#         print("no")
#         f=1
#         break
#     else:
#         l[i].remove(s[i])
# if(f==0):
#     print("yes")




# a={5,5.0,'5',(5,2),'5,2'}
# print(a)


# a={5,5.2,'5',(5,2),{5,2},(2,5)}
# print(a)                     no list set and dict inside a set if it is there it is an error



# a=[5]
# a.extend("3.5")
# print(len(a))




# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     if s[0]==s[-1]:
#         return is_palindrome(s[1:-1])
#     return False
# print(is_palindrome("12321"))  
   



# def fun(x,re):
#     if(x==0):
#         return re
#     re=re*10+(x%10)
#     return fun(x//10,re)
# n=int(input())
# if(n==fun(n,0)):
#     print("pal")
# else:
#     print("np")

















# l=list(map(int,input().split()))
# max1=0
# for i in range(len(l)-1):
#     for j in range(i+1,len(l)):
#         if l[j]-l[i]>max1:
#             max1=l[j]-l[i]
# print(max1)






# 7,1,5,3,6,4

# l=list(map(int,input().split()))
# b=l[0]
# profit=0
# for i in l[1:]:
#     if b>i:
#         b=i
#     profit=max(profit,i-b)
# print(profit)
    






# n=int(input())
# c=1
# for i in range(n):
#     for j in range(n):
#         if(i==0 or j==0 or i==n-1 or j==n-1):
#             print("*",end=" ")
#         elif(i!=n-1):
#             print(c,end=" ")
#             c=c+1
#     print()



# 5
# * * * * *
# * 1 2 3 *
# * 4 5 6 *
# * 7 8 9 *
# * * * * *














# def print_pattern(n):
#     # n is the number of levels
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

#     for i in range(n):
#         # Create the left part of the pattern
#         left_part = alphabet[:i+1]
#         # Create the right part of the pattern (reversed left part excluding the last character)
#         right_part = left_part[:-1][::-1]
#         # Combine both parts
#         full_part = left_part + right_part
#         # Calculate the number of leading hyphens
#         hyphens = '-' * (n - i - 1)
#         # Print the line with leading and trailing hyphens
#         print(hyphens + full_part + hyphens)

# # Set the number of levels
# n = 4
# print_pattern(n)

















# def print_pattern(n):
#     for i in range(n):
#         row = []
#         for j in range(n):
#             # Calculate the value based on the distance to the nearest edge
#             value = min(i, j, n - i - 1, n - j - 1) + 1
#             row.append(value)
#         print(" ".join(map(str, row)))

# # Set the size of the pattern
# n = 7
# print_pattern(n)

























# n=int(input())
# c=2
# for i in range(n+c):
#     for j in range(n+c):
#         print(1,end=" ")
      
#     print()

























# l=["aa","aaaa","abc","aabc","abca","aaa"]
# p=[]
# for i in l[:]:
#         if len(i)==i.count(i[0]):
#                 p.append(i)
#                 l.remove(i)
#         else:
#                 l
# print(l)
# print(p)
   





# l = ["aa", "aa", "ba", "abc", "abc", "ac", "da"]
# p = []

# for i in l[:]:  
#     if len(i) == i.count(i[0]) or any(i[j] == i[j+1] for j in range(len(i) - 1)):
#         p.append(i)
#         l.remove(i)

# print(l)  
# print(p)  








# from collections import Counter

# # Initial list
# l = ["aa", "aa", "ba", "abc", "abc", "ac", "da"]

# # Count the occurrences of each element
# count = Counter(l)

# # Create an empty list to store the filtered elements
# filtered_list = []

# # Iterate over the original list
# for item in l:
#     # If the count of the current item is 1, add it to the filtered list
#     if count[item] == 1:
#         filtered_list.append(item)

# # Print the resulting list
# print(filtered_list)

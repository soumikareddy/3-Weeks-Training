##########3prime or next prime
# def pr(n):
#     p=str(n)
#     s=0
#     for i in p:
#         s=s+int(i)
   
#     if s in[0,1,2,3,4,5,6,7,8,9]:
#         print(s)
#     else:
#         return pr(s)

# n=537867891234
# pr(n)





# def add(n):
#     s=0
#     while(n):
#         s=s+(n%10)
#         n=n//10
#     return s
# def pnp(x):
#     if (n in [2,3,5,7]):
#         return m
#     else:
#         return m+1
# n=int(input())
# m=n
# if(n<10):
#     print(pnp(n))
# else:
#     while(1):
#         n=add(n)
#         if(n<10):
#             break
#     print(pnp(n))













# def fun(x):
#     print(x)
#     fun(x+1)
# fun(1)


# def fun(x):
#     if(x==3):
#         return 500
#     print(x)
#     print(fun(x+1))
#     print(x)
#     return 100
# print(fun(1))





# def fun(x):
#     if(x==3):
#         return 500
#     print(x)
#     t=fun(x+1)
#     print(x)
#     return t
# print(fun(1))


# def fun(x,s):
#     if(x==len(a)):
#         return s
#     s=s+a[x]
#     return fun(x+1,s)
# a=[6,7,2]
# print(fun(0,0))







# def fun(i,s1,s2):
#     if(i==len(a)):
        
#         return s1,s2
    
#     if a[i]%2==0:
#         s1=s1+a[i]
        
    
#     if b[i]%2!=0:
#         s2=s2+b[i]
        
   
#     return fun(i+1,s1,s2)




# a=[3,8,5,4,3]
# b=[5,0,9,3,2]
# print(fun(0,0,0))







# def fun(i):

#     if(i==0):
#         return 0
   
#     return i+fun(i-2)
# n=13
# if(n%2==0):
#     print(fun(n))
# else:
#     print(fun(n-1))










# def fun(a):
#     if len(a)%2==0:
#         print("yes")
#     else:
#         print("no")

# a=[5,8,9,5,2,4.7,8]
# fun(a)



# p="MMFF"
# l=0
# t=0
# for i in p:
#     if i=='M':
#         l=l+1
#     elif i=='F':
#         t=t+1
# if l>t:
#     print("m")
        
# elif l<t:
#     print("f")
# else:
#     print("0")
        


# p="mmmmmfff"
# c=0
# for i in p:
#     if i=='m':
#         c=c+1
#     else:
#         c=c-1
# if c==0:
#     print("0")
# elif c>1:
#     print("m")
# else:
#     print("f")



# a="leet**co*de"
# b=[]
# for i in a:
#     if(i!='*'):
#         b.append(i)
#     else:
#         b.pop()
# print("".join(b))





# s="is2 sentence4 This1 a3"
# s=s.split()
# re=[0]*len(s)
# for i in s:
#     re[int(i[-1])-1]=i[:-1]
# print(" ".join(re))



# import ast

# # Function to take double list as input
# def take_double_list_input():
#     # Prompt the user for input
#     input_string = input("Enter a list of lists (e.g., [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]): ")
    
#     # Safely evaluate the input string to a Python list of lists
#     double_list = ast.literal_eval(input_string)
    
#     return double_list

# # Example usage
# double_list = take_double_list_input()
# print(double_list)






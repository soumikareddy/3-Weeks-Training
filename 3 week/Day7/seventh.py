# l=[3,2,5,4,1,6,8]
# n=len(l)
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             print(l[i],l[j],l[k])










 


# def comb(l,k):
#     def fun(curr,start):
#         if len(curr)==k:
#             print(curr)
#             return
#         for i in range(start,len(l)):
#             fun(curr+[l[i]],i+1)
#         return
#     fun([],0)
# a=[3,5,1,6]
# k=3
# comb(a,k)







# s = input()
# q=s
# k = int(input())
# l = []
# r=[]

# for i in range(k):
#     l.append(input())

# for i in l:
#     if i[0] == 'L':
#         v= s[int(i[1]):] + s[:int(i[1])]
#         print(v)
#         r.append(v[0])
#     elif i[0] == 'R':
#         v = s[-int(i[1]):] + s[:-int(i[1])]
#         print(v)
#         r.append(v[0])

#     s = q
# d="".join(r)
# print(d)
# print(s)
# t=[]
# for i in range(len(s)-2):

#     v=s[int(i):k]
#     s=q
#     k=k+1
#     t.append(v)
# print(t)
# for i in t:
#     print(sorted(i))





# a=input()
# n=int(input())
# str=''
# for i in range(n):
#     b=input()
#     if(b[0]=='L'):
#         str=str+a[int(b[2])]
#     else:
#         str=str+a[-int(b[2])]
# print(str)
# str=list(str)
# str.sort()
# b=[]
# for i in range(len(a)-n+1):
#     t=list(a[i:n+i])
#     t.sort()
#     b.append(t)
# print(b)
# print(str)
# for i in b:
#     if(i==str):
#         print("yes")
#         break
# else:
#     print("no")





########13 =11+2 so for 13 it is 1 as 11 and 2 are prime
# def isprime(x):
#     if(x==1):
#         return 1
#     if(x==2):
#         return 1
#     for i in range(2,(x//2)+1):
#         if(x%i==0):
#             return 0
#     return 1

# a=int(input())
# for i in range(1,(a//2)+1):
#     if(isprime(i) and isprime(a-i)):
#         print("yes")
#         break
# else:
#     print("no")



# a = "polikujmnhytgbvfredcxswqaz"
# b = "abbcddabb"
# c= {}
# for i in range(len(a)):
#     c[a[i]] = i
# s= ''.join(sorted(b,key =c.get))
# print(s)





"""
ip:
   2
   polikujmnhytgbvfredcxswqaz
   abcd
   qwryupcsfoghjkldezxvbintma
   ativedoc

op:  
   bdca
   codevita
"""







# n=2
# q1="polikujmnhytgbvfredcxswqaz"
# s1="abbcdd"
# q2="qwryupcsfoghjkldezxvbintma"
# s2="ativedoc"
# a=""


# n=int(input())
# while(n):
#     a=input()
#     c=input()
#     s=""
#     for i in a:
#         if(i in c):
#             s=s+(i*c.count(i))
#     print(s)
#     n=n-1

 

# def fun(l):
#     if(len(l)==0):
#         return 0
#     if(len(l)==1):
#         return l[0]
#     if(len(l)==2):
#         return max(l)
#     le=l[0]+fun(l[2:])
#     ri=l[1]+fun(l[3:]) 
#     return max(le,ri)
# l=[13,9,4,10,5,7]      
# print(fun(l))







# def fun(root):
#     if(root==None):
#         root=node(x)
#      elif(x<root.data):
#         fun(root.left)
#       else:
#         fun(root.right)
# fun(x)









# def prime(n):
#      if n<=1:
#         return 0
#      if n==2:
#         return 1
#      def pnt(i,n):
#       if i>n//2:
#          return 1

#       if(n%i==0):
#            return 0
      
#       return pnt(i+1,n)
 
#      if(pnt(2,n)):
#       return 1
#      else:
#       return 0
# n=int(input())
# print(prime(n))








# def palin(temp,n):
    
#     if(n==0):
#        if(temp==org):
#           return 1
#        else:
#           return 0    
#     return palin(temp*10+n%10,n//10)


#    #  org=n
#    #  temp=0
    
#    #  while(n>0):
#    #      dig=n%10
#    #      temp=temp*10+dig
#    #      n=n//10
#    #  if(temp==org):
#    #      return 1
#    #  else:
#    #      return 0
    

# n=int(input())
          
# org=n
# print(palin(0,n))







# def sum_of_squares(n):
#     return sum(int(digit) ** 2 for digit in str(n))

# def is_happy(n):
#     seen = set()
#     while n != 1 and n not in seen:
#         seen.add(n)
#         n = sum_of_squares(n)
#     return n == 1

# n = int(input("Enter a number: "))  # input is 19

# if is_happy(n):
#     print(f"{n} is a happy number.")
# else:
#     print(f"{n} is not a happy number.")







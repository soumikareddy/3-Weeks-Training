# #######Longest sub string which is palindrome###########



# n=int(input())
# l=[]
# m=[]
# p=[]
# for i in range(n):
#     x,y=list(map(str,input().split(" ")))
    
#     if int(x)==1:
#         l.append(y)
#     elif int(x)==2:
#         m.append(y)
#     elif int(x)==3:
#         p.append(y)
# print(l)
# print(m)
# print(p)

# for i in l:
#     for j in m:
#         if(i==j):
#             print("True")
#             break
# else:
#     print("False")
            


        
    
# for i in l:
#     for j in p:
#         k=len(j)
#         if(i[0:k]==j):
#             print("True")
#             break
#     else:
#         print("False")
        



# def parse_input(n):
#     l, m, p = [], [], []
#     for _ in range(n):
#         x, y = input().split()
#         if x == '1':
#             l.append(y)
#         elif x == '2':
#             m.append(y)
#         elif x == '3':
#             p.append(y)
#     return l, m, p

# def search(l, word):
#     return word in l

# def prefix_search(l, prefix):
#     for word in l:
#         if word.startswith(prefix):
#             return True
#     return False

# def main():
#     n = int(input("Enter the number of inputs: "))
#     l, m, p = parse_input(n)
    
#     print("List l:", l)
#     print("List m:", m)
#     print("List p:", p)

#     # Check for exact matches
#     for word in m:
#         if search(l, word):
#             print("True")
#         else:
#             print("False")
    
#     # Check for prefix matches
#     for prefix in p:
#         if prefix_search(l, prefix):
#             print("True")
#         else:
#             print("False")

# # Call the main function
# main()



    

class node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            
            t=t.d[i]
        t.flag=1
        
    def search(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:
            return False
    def prefix(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    
    def append(self,str):
        def fun(t,s):
            if(t.flag==1):
                print(s)
                return 
            for i in t.d:
                fun(t.d[i],s+i)


        t=self.root
        s=""
        for i in str:
            if i in t.d:
                s=s+i
                t=t.d[i]
            else:
                return 
        fun(t,s)
    



t=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if(a=='1'):
        t.insert(s)
    if(a=='2'):
        print(t.search(s))
    if(a=='3'):
        print(t.prefix(s))
    if a=='4':
        t.append(s)

# t.insert("world")
# t.insert("words")
# t.insert("apple")
# t.insert("woo")
# t.insert("wo")
# t.insert("w")
# print(t.search("apple"))
# print(t.prefix("wo"))

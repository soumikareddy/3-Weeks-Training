# def fun(j,l):
#     print(j,end=" ")
#     l.append(j)
#     for i in d[j]:
#         if i not in l:
#             fun(i,l)
  

# d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
# fun(5,[])

##########output##########
# 5 7 4 8 3 2 





##################All Paths#############

# def fun(d,x,e,c):
    
#     l.append(x)
#     if(x==e):
#         c=c+1
#         print(l)
#         l.pop()
#         return c

#     for i in d[x]:
#         if i not in l:
#             c=fun(d,i,e,c)
#     l.pop()
#     return c
# d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
# l=[]
# print(fun(d,5,2,0))









##################cost for all paths###############3333
# def fun(d,x,e,c):
    
#     l.append(x)
#     if(x==e):
        
#         print(l,c)
#         l.pop()
#         return c

#     for i in d[x]:
#         if i[0] not in l:
#             fun(d,i[0],e,c+i[1])
#     l.pop()
    
# d={5:[(7,1),(3,7)],7:[(5,1),(4,4),(3,5)],4:[(7,4),(8,2),(2,8)],8:[(3,6),(4,2),(2,9)],3:[(5,7),(7,5),(8,6)],2:[(4,8),(8,9)]}
# l=[]
# fun(d,5,2,0)












##################least cost for the path###########
# def fun(d,x,e,c,m,l1):
    
#     l.append(x)
#     if(x==e):
#         if(c<m):
#             m=c   
#             l1=l.copy()
#         l.pop()
#         return m,l1

#     for i in d[x]:
#         if i[0] not in l:
#             m,l1=fun(d,i[0],e,c+i[1],m,l1)
#     l.pop()
#     return m,l1
# d={5:[(7,1),(3,7)],7:[(5,1),(4,4),(3,5)],4:[(7,4),(8,2),(2,8)],8:[(3,6),(4,2),(2,9)],3:[(5,7),(7,5),(8,6)],2:[(4,8),(8,9)]}
# l=[]
# print(fun(d,5,2,0,999999,[]))















def dfs(j,l):
    l.append(j)
    for i in d[j]:
        if i not in l:
            dfs(i,l)
    return l
    
def path(s,e,l,c):
    l.append(s)
    if s==e:
        print(l) 
        c=c+1
        l.pop()
        return c
    for i in d[s]:
        if i not in l:
            c=path(i,e,l,c)
    l.pop()
    return c
    
def path_cost(s,e,l,co):
    l.append(s)
    if s==e:
        print(l,co)
        l.pop() 
        return
    for i in d1[s]:
        if i[0] not in l:  
            path_cost(i[0],e,l,co+i[1])
    l.pop()
    
def mincost(s,e,l,co,m,l1):
    l.append(s)
    if s==e: 
        if co<m:
            m=co
            l1=l.copy()
        l.pop() 
        return m,l1
    for i in d1[s]:
        if i[0] not in l:  
            m,l1=mincost(i[0],e,l,co+i[1],m,l1)
    l.pop()
    return m,l1

def allpaths(s,e,l):
    l.append(s)
    if s==e:
        print(l) 
        l.pop() 
        return
    for i in d[s]:
        if i not in l:
            allpaths(i,e,l)
    l.pop()

def allpathsleastcost(s,e,l,co,m,l1):
    l.append(s)
    if s==e: 
        if co<m:
            m=co
            l1=l.copy()
        l.pop() 
        return m,l1
    for i in d1[s]:
        if i[0] not in l:  
            m,l1=allpathsleastcost(i[0],e,l,co+i[1],m,l1)
    l.pop()
    return m,l1

d1={5:[(7,11),(3,10)],7:[(5,11),(4,12),(3,14)],4:[(7,12),(8,10),(2,13)],8:[(3,15),(4,10),(2,16)],3:[(5,10),(7,14),(8,15)],2:[(4,13),(8,16)]}
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
print("Dfs:", dfs(5,[]))
print("Paths:")
print("Total paths:",path(5,2,[],0))
path_cost(5,2,[],0)
print("Min. cost path:",mincost(5,2,[],0,999999,[]))
print("All possible paths:")
for i in d: 
    allpaths(5,i,[])
print("Minimum cost of all paths:")
for i in d.keys():
    print(allpathsleastcost(5,i,[],0,999999,[]))
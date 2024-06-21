
# # def bfs(d,n,q,l):
# #     q=[n]
# #     while(q):
# #         for i in d[q[0]]:
# #             if (i not in q) and (i not in l):
# #                 q.append(i)
# #         l.append(q[0])
# #         q.pop(0)
# #     return l
# # def new(d1,n,q,l):
# #     q=[n]
# #     while(q):
# #         for i in d1[q[0]]:
# #             if (i not in q) and (i not in l):
# #                 q.append(i)
# #         l.append(q[0])
# #         q.pop(0)
# #     return l

# # d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
# # print("BFS",bfs(d,5,[],[]))
# # d1=d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,9],3:[5,7,8],9:[8,10],10:[9],2:[4,6],6:[2]}
# # print("BFS1",new(d1,5,[],[]))










def dijkstra(s):
    d1={1:9999,2:9999,3:9999,4:9999,5:9999}
    d1[s]=0
    v=[]
    q=[s]
    while(q):
        m=9999
        for i in q:
            if d1[i]<m:
                m=d1[i]
                s=i
        for i in d[s]:
            if i[0] not in v:
                if d1[i[0]]>(d1[s]+i[1]):
                    d1[i[0]]=d1[s]+i[1]
                print(d1)
                if i[0] not in q:
                    q.append(i[0]) 
        v.append(s)
        print(v)  
        q.remove(s)
    return (d1)

d={1:[(2,2),(3,2),(4,1)],2:[(1,2),(4,2),(5,3)],3:[(1,2),(4,3)],4:[(1,1),(2,2),(3,3),(5,2)],5:[(2,3),(4,2)]}
print("Dijkstra:",dijkstra(1))









# def fun(i):
#     if i==len(l):
#         return 
#     if l[i]%2==0:
#         def fun2(a,r,j,s,b):
#             if j==len(a):
#                 r.append(s)
#                 return 
#             if a[j]%2!=0:
#                 b.append(l[i]+a[j])
#                 s=s+l[i]+a[j] 
#             fun2(a,r,j+1,s,b) 
#         fun2(a,r,0,s,b) 
#         fun(i+1)
#     else: 
#         fun(i+1)

# l=[6,3,2,9,4,7]
# a=[8,7,5,3,6,9]
# r=[]
# b=[]
# s=0
# fun(0) 
# print(b)
# print(r)
# # [13, 11, 9, 15, 9, 7, 5, 11, 11, 9, 7, 13]
# # [48, 32, 40]
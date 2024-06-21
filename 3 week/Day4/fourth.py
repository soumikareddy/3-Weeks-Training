# class node:
#     def __init__(self,u):
#         self.data=u
#         self.nxt=None
# class sll:
#     def __init__(self):
#         self.head=None

#     def display(self):
       
#         t=self.head
#         while(t!=None):
            
#             print(t.data,end="->")
#             t=t.nxt
       
#     def addback(self,x):
#         t=self.head
#         while(t.nxt!=None):
#             t=t.nxt
#         t.nxt=node(x)
#     def addfront(self,x):
#         t=node(x)
#         t.nxt=self.head
#         self.head=t
#     def search(self,x):
#         t=self.head
#         while(t!=None):
            
#             if(t.data==x):
#                 print("found",x)
#                 break
#             t=t.nxt
#         else:
#             print("not found")


#     def sub(self):
#         t=self.head  
       
#         max1=0
#         while(t.nxt!=None):
#             if(t.data==t.nxt.data-1):
#                 p=p+1
#                 max1=max(max1,p)
                
#             else:
#                 p=1
#             t=t.nxt
#         print("max sub string is",max1)
 
#     def pairs(self):
#         t=self.head
#         t1=t.nxt
#         print("pairs:")
#         while(t.nxt!=None):
#             while(t1!=None):

#                 print(t.data,t1.data)
#                 t1=t1.nxt
#             t=t.nxt
#             t1=t.nxt

#     def bubble(self):
        
#         T=self.head
#         p=None
#         while(T.nxt!=None):
#             f=0
#             t=self.head
#             while(t.nxt!=p):
#                 if(t.data>t.nxt.data):
#                     f=1
#                     t.data,t.nxt.data=t.nxt.data,t.data
#                 t=t.nxt
#             if(f==0):
#                 break
#             p=t
#             T=T.nxt
#         l1.display() 
            
#     def middle(self):
       
#         slow=self.head
#         fast=self.head
#         while(fast!=None and fast.nxt!=None):
#             slow=slow.nxt
#             fast=fast.nxt.nxt
            
#         print("middle element",slow.data)
#     def reverse(self):
#         a=0
#         b=self.head
#         c=self.head
#         while c!=None:
#             c=c.nxt
#             b.nxt=a
#             a=b
#             b=c
#         self.head=a
#         temp=self.head
#         while temp!=0:
#             print(temp.data,end=" ")
#             temp=temp.nxt

#     def evenorodd(self):
#         slow=self.head
#         fast=self.head
       
#         while(fast!=None and fast.nxt!=None):
#             slow=slow.nxt
#             fast=fast.nxt.nxt
            
#         if(fast==None):
#             print("even")
#         else:
#             print("odd")
    
    

    
    
#     def addeven(self):
#         t=self.head
#         s1=0
#         while(t!=None):
#             if(t.data%2==0):
#                 s1=s1+t.data
#                 t=t.nxt
#             else:
#                 t=t.nxt
#         print("sum of even",s1)
# l1=sll()

# l1.head=node(2)
# l1.addback(1)
# l1.addback(6)
# l1.addback(8)
# l1.addfront(6)
# l1.search(6)
# l1.display()
# print()
# l1.addeven()
# l1.middle()
# l1.sub()
# l1.pairs()
# l1.bubble()
# print()

# l1.evenorodd()
# l1.reverse()
# # l2=sll()
# # l2.head=node(100)
# # l2.addback(201)
# # l2.addfront(24)
# # l2.addfront(25)
# # l2.search(201)

# # l2.display()
# # print()
# # l2.addeven()
# # l2.middle()
# # l2.evenorodd()
# # l2.sub()
# # l2.pairs()










# #####################reverse of a linked list###############################





# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         p = list()
#         while head:
#             p.append(head.val)
#             head = head.next
#         i, j = 0, len(p) - 1
#         while i < j:
#             if p[i] != p[j]:
#                 return False
#             i, j = i + 1, j - 1
#         return True
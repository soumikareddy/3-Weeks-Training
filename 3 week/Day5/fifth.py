# a="aabBCaB"
# print(a.rindex('a'))






class node:
    def __init__(self,x):
        self.next=None
        self.data=x
        self.prev=None

class  dll:
    def __init__(self):
        self.head=None
        self.tail=None

    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print()
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=t

    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    # def search(self,x):
    #     if(self.head==None):
    #         self.head=node(x)
    #         self.tail=self.head
    #     else:
    #         t=self.head
    #         while(t!=None):
    #             if(t.data==x):
    #                 print("found",x)
    #                 break
    #             t=t.next
    #         else:
    #             print("not found")
    def search(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=self.head
            t1=self.tail
            while(t!=t1 and t!=t1.next):
                if(t.data==x or t1.data==x):
                    print("found",x)
                    break
                t=t.next
                t1=t1.prev
            else:
                if(t.data==x):
                    print("found",x)
                      
                
                else:
                    print("not found")

    def evorodlen(self):
            t=self.head
            t1=self.tail
         
            while(t!=t1 and t!=t1.next):
               
                t=t.next
                t1=t1.prev
            if(t==t1):
                print("odd")
            else:
                print("even")


    def swappair(self):
        t=self.head 
        while(t!=None):
            t1=t.next
            if(t==self.head):
                t.next,t1.next=t1.next,t
                t.prev,t1.prev=t1,None 
                t.next.prev=t
                self.head=t1
            else:
                t.next,t1.next=t1.next,t
                t1.prev,t.prev=t.prev,t1
                if(t.next!=None):
                    t.next.prev=t
                t1.prev.next=t1    
            t=t.next



    def evodsum(self,t,s,s1):
           
            if(t==None):
                return abs(s-s1)
            if(t.data%2==0):
                s=s+t.data
            else:
                s1=s1+t.data
    
   
            return self.evodsum(t.next,s,s1)
    
   
    def prime(self,t,c):
        if(t==None):
            return c
        def pnt(s,n):
            if(s>=(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            
            return pnt(s+1,n)
        if(pnt(2,t.data)):
            c=c+1
        return self.prime(t.next,c)




    def palin(self):
        t=self.head
        t1=self.tail
        c=0
        while(t!=t1 and t!=t1.next):
            if(t.data!=t1.data):
                print("not a palindrome")
                break
            t=t.next
            t1=t1.prev
        else:
            print("palindrome")



    
    def move(self):
        fast=self.head
        slow=self.head
        while(fast!=None):
            fast=fast.next.next
            slow=slow.next

        fast=self.head
        while(slow!=None):
            slow.data,fast.data=fast.data,slow.data
            slow=slow.next
            fast=fast.next
      
        


        


l1=dll()

l1.addback(7)
l1.addback(8)
l1.addback(9)
l1.addback(11)
l1.addback(12)
l1.addback(15)
l1.addfront(5)
l1.addfront(3)
l1.evorodlen()

l1.search(10)
print(l1.evodsum(l1.head,0,0))
print(l1.prime(l1.head,0))
l1.display()

l1.rev_display()

l1.palin()
l1.move()
l1.display()
l1.swappair()
l1.display()
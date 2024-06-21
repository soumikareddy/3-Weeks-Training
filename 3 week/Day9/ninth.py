class node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None

class tree:
    def __init__(self):
        self.root=None

    def inorder(self,root): 
        if(root):
            self.inorder(root.left) 
            print(root.data,end=" ")
            self.inorder(root.right) 

    def postorder(self,root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")

    def preorder(self,root):
        if(root):
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def add(self, root):
        if root is None:
            return 0
        return root.data+self.add(root.left)+self.add(root.right)
    
    def even(self,root):
        if root is None:
            return 0
        if root.data%2==0:
            return root.data+self.even(root.left)+self.even(root.right)
        else:
            return self.even(root.left)+self.even(root.right)
    
    def odd(self,root):
        if root is None:
            return 0
        if root.data%2!=0:
            return root.data+self.odd(root.left)+self.odd(root.right)
        else:
            return self.odd(root.left)+self.odd(root.right)
    
    def diff(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.diff(root.left)+self.diff(root.right)
        return self.diff(root.left)+self.diff(root.right)-root.data
    def heigh(self,root):
        if root==None:
            return -1
        else:
            return max(self.heigh(root.left),self.heigh(root.right))+1
        
    def bal(self,root):
        
        return abs(self.heigh(root.left)-self.heigh(root.right))<=1
    def leaf(self,root,c):
        if root==None:
            return 0
        elif root.right==None and root.left==None:
            c=c+1
        return c+self.leaf(root.left,c)+self.leaf(root.right,c)
    def addleaf(self,root,s):
        if root==None:
            return 0
        elif root.right==None and root.left==None:
            
            s=s+root.data
        return s+self.addleaf(root.left,s)+self.addleaf(root.right,s)

    def search(self,root,s):
        if root==None:
            return 0
        if s==root.data:
            return root.data
        return self.search(root.left,s)+self.search(root.right,s)
    def dep(self,root,c,s):
         if root==None:
            return -1
         
         if(self.search(root,s)!=0):
             if root.data==s:
                 return c
             elif root.data>s:
                 c=c+1
                 return self.dep(root.left,c,s)
             elif root.data<s:
                 c=c+1
                 return self.dep(root.right,c,s)
         else:
             return "element not found"


    def lef(self,root,c,l):
        if root==None:
            return
        if c not in l:
            print(root.data,c)
            l.append(c)
        self.lef(root.left,c+1,l)
        self.lef(root.right,c+1,l)
    
    def rig(self,root,c,l):
        if root==None:
            return
        if c not in l:
            print(root.data,c)
            l.append(c)
        self.rig(root.right,c+1,l)
        self.rig(root.left,c+1,l)
    



    def top(self,root,d,q):
        if root==None:
            return
        
        d={}
        q=[(root,0)]
        while(q):
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            if(q[0][1] not in d):
                d[q[0][1]]=root.data
            q.pop(0)
        print(d)
        for i in sorted(d):
            print(d[i],end=" ")

    
    def bottom(self,root,d,q):
        if root==None:
            return
        
        d={}
        q=[(root,0)]
        while(q):
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            
            d[q[0][1]]=root.data
            q.pop(0)
        print(d)
        for i in sorted(d):
            print(d[i],end=" ")



    
    def create(self,root,x): 
        if(root is None):
            return node(x)
        elif(x<root.data):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
    

t1=tree()
t1.root=t1.create(t1.root,10)
t1.create(t1.root,5)
t1.create(t1.root,15)
t1.create(t1.root,2)
t1.create(t1.root,7)
t1.create(t1.root,11)
# t1.create(t1.root,20)
# t1.create(t1.root,4)
# t1.create(t1.root,3)
# t1.create(t1.root,12)
t1.create(t1.root,8)
t1.create(t1.root,9)
t1.inorder(t1.root)
print()
t1.postorder(t1.root)
print()
t1.preorder(t1.root)
print()
print(t1.add(t1.root.left)-t1.add(t1.root.right))
print()
print(t1.even(t1.root))
print()
print(t1.odd(t1.root))
print(abs(t1.diff(t1.root)))
print(t1.heigh(t1.root))
if(t1.bal(t1.root)):
    print("balanced")
else:
    print("not balanced")
print(t1.leaf(t1.root,0))
print(t1.addleaf(t1.root,0))
b=t1.search(t1.root,2)
if(b==0):
    print("not found")
else:
    print("found",t1.search(t1.root,2))
print(t1.dep(t1.root,0,15))
print("left view")
t1.lef(t1.root,0,[])

print("right view")
t1.rig(t1.root,0,[])

print("top view")
t1.top(t1.root,{},[])
print()
print("bottom view")
t1.bottom(t1.root,{},[])
print()

































































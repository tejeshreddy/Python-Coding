class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()
    
    def append(self,data):
        new_node=node(data)
        cur=self.head
        while(cur.next!=None):
            cur=cur.next
        cur.next=new_node

    def display(self):
        ele=[]
        cur=self.head
        while(cur.next!=None):
            cur=cur.next
            ele.append(cur.data)
        print(ele)

    def get(self,data):
        cur=self.head
        pos=1
        while(cur.next!=None):
            cur=cur.next
            if(cur.data==data):
                return(pos)
            pos+=1
        

my_list=linked_list()

while True:
    x=int(input("1.add\n2.display\n3.get\n4.exit"))
    if(x==1):
        data=int(input())
        my_list.append(data)
    elif(x==2):
        my_list.display()
    elif(x==3):
        position=my_list.get(int(input()))
        print(position)
    elif(x==4):
        break
    
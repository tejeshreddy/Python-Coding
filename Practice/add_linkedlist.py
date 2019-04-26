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
            elem=[]
            cur_node=self.head
            while(cur_node.next!=None):
                cur_node=cur_node.next
                elem.append(cur_node.data)
            print(elem)

my_list=linked_list()

my_list.append(1)
my_list.append(2)

my_list.display()
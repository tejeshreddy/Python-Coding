class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
    
class linked_list:
    def __init__(self):
        self.head=node()

    def insert(self,data):
        new_node=node(data)
        cur=self.head
        while(cur.next!=None):
            cur=cur.next
        cur.next=new_node
    
    def length(self):
        cur=self.head
        len=0
        while(cur!=None):
            cur=cur.next
            len+=1
        return len
    
    # def delete(self,data):
    #     if(self.length()<1):
    #         print("Not possible")
    #         return
    #     else:
    #         cur=self.head
    #         sec=cur.next
    #         if(cur.data==data):
    #             self.head=sec
    #             return
    #         else:
    #             while(sec!=None):
    #                 if(sec.data==data):
    #                     cur.next=sec.next
    #                     cur=cur.next
    #                     sec=cur.next

    def display(self):
        ele=[]
        cur=self.head
        while(cur.next!=None):
            cur=cur.next
            ele.append(cur.next)
        print(ele)

my_list=linked_list()
my_list.insert(1)
my_list.insert(2)
# my_list.delete(0)
my_list.display()

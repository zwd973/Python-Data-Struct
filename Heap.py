#This is minimum heap with Python.
class Heap(object):
    def __init__(self):
        self.list=[0]
        self.n=0
    # def __init__(self,nums):
    #     n=len(nums)
    #     self.list=[0]
    #     self.list.extend(nums)
    def adjust_heap(self,index):
        """
        Adjusting heap to maintain heap property.
        :param index:
        :return:
        """
        l=self.n
        u,m=index,index
        while(2*u<l):
            m=u
            if self.list[m]>self.list[2*u]:
                m=2*u
            if 2*u+1<l and self.list[m]>self.list[2*u+1]:
                m=2*u+1
            if m==u:
                break;i
            temp=self.list[u]
            self.list[u]=self.list[m]
            self.list[m]=temp
            u=m
        return
    def buid_heap(self):
        """
        Initialize for heap.
        :return:
        """
        for i in range(self.n//2,1):
            self.adjust(i)
    def __adjust_heap__(self):
        """
        Adjusting heap while inserting a new value.
        :return:
        """
        cur = self.n
        while cur>1:
            p=cur//2
            if self.list[cur]<self.list[p]:
                self.list[cur],self.list[p] = self.list[p],self.list[cur]
                cur=p
            else:
                break
        return
    def insert(self,value):
        """
        Step1:
            Inserting value at last of the list.
        Step2:
            Adjusing heap。
        :param value:
        :return:
        """
        if self.n+1<len(self.list):
            self.list[self.n+1]=value
        else:
            self.list.append(value)
        self.n = self.n+1
        self.__adjust_heap__()
        return
    def extract_minmum(self):
        value = self.list[0]
        self.list[0],self.list[self.n] = self.list[self.n],self.list[0]
        self.n = self.n-1
        self.adjust_heap(0)
        return value
    def delete(self,index):
        value = self.list[index]
        self.list[index],self.list[self.n] = self.list[self.n],self.list[index]
        self.n = self.n-1
        self.adjust_heap(index)
        return value
    def empty(self):
        return self.n==0

#test
def main():
    nums=[1,2,5,4,7,8,9,6,6]
    heap=Heap()
    for v in nums:
        heap.insert(v)
    heap.delete(4)
    while not heap.empty():
        print(str(heap.extract_minmum()) + ' ',end='')
if __name__=='__main__':
    main()
import timeit


# class for binary search
class BinaryStringList:

    # constructor, which creates a list
    def __init__(self):

        self.list2=[]
      
    # method to add the element to a list
    def add(self,element):
        self.list2.append(element)

    # method to find the element in a list
    def find(self,element):

        self.list2.sort()

        first_pos=0
        last_pos=len(self.list2)-1
        flag=False

        while first_pos <= last_pos and not flag:
            mid_point=(first_pos+last_pos )//2

            if self.list2[mid_point] == element:              
                return self.list2[mid_point]
            else:
                if element < self.list2[mid_point]:
                    last_pos=mid_point - 1
                else:
                    first_pos=mid_point + 1

        return None

if __name__=='__main__':

    code2='''
from __main__ import BinaryStringList
ob=BinaryStringList()
ob.add('java')
ob.add('python')
ob.add('perl')
ob.add('c')
ob.add('c++')
ob.add('ada')
ob.add('go')
ob.add('rust')
ob.add('swift')
ob.add('html')
ob.add('php')
ob.add('bash')
ob.add('c#')
ob.add('cython')
ob.add('jython')
ob.add('cobol')
ob.add('fortran')
ob.add('basic')
ob.add('smalltalk')
ob.add('pascal')
'''
    # finding the execution for searching the list
t3=timeit.timeit("ob.find('cython')",code2,number=1)
print('Binary search,string found: ',t3)
t4=timeit.timeit("ob.find('simula')",code2,number=1)
print('Binary Search, string not found:',t4)      

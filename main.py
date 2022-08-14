# -*- coding: utf-8 -*- 
# !usr/bin/env python


# stack ,int
class Stack():
	# initial 3 lists
    def __init__(self):
        self.stack = []
        self.max2 = [] # way2nd
        self.max3 = [] # way3rd

	# input
    def append(self, item):
        self.stack.append(item)
        print(f"The list is:{self.stack}")
        # way2nd
        if len(self.max2) == 0:
            self.max2.append(item)
        else:
            if self.max2[-1]>item:
                # self.max2.append(self.max2[-1])
                pass
            else:
                self.max2.append(item)
        # way3rd
        if len(self.max3) == 0:
            self.max3.append(0) # onlu postion, not value
        else:
            if self.stack[ self.max3[-1] ] < item:
                self.max3.append( len(self.stack)-1 )
            else:
                pass
        print(self.max3)

    # output
    def pop(self):
        # way2nd
        self.max2.pop()
        # way3rd
        if len(self.stack)-1 == self.max3[-1]:
            self.max3.pop()
        else:
            pass
        return self.stack.pop()

    # Judge whether the list is empty or not
    def isempty(self):
        return len(self.stack) == 0

    # return the length of the list
    def length(self):
        return len(self.stack)

    # Get the top of stack or tail of the list
    def getup(self):
        if self.isempty():
            raise IndexError
        else:
            return self.stack[-1]

    # Way1st constant time complexity O（n）
    def getMax1(self):
        return max(self.stack)
    
    # Way2nd，constant space complexity O（n）
    def getMax2(self):
        if len(self.max2) == 0:
            raise IndexError
        else:
            return self.max2[-1]

    # Way3rd, constant space complexity< O（n）
    def getMax3(self):
        if len(self.max3) == 0:
            raise IndexError
        else:
            return self.stack[ self.max3[-1] ]

# Test
if __name__ == '__main__':
    s = Stack()
    s.append(1)
    s.append(2)
    assert s.length() == 2
    assert s.isempty() == False
    assert s.pop() == 2
    assert s.getup() == 1
    s.pop()
    assert s.isempty()
    try:
        s.getup()
        print("error")
    except IndexError:
        pass
    s.append(4)
    s.append(6)
    s.append(1)
    s.append(2)
    s.append(4)
    s.append(-1)
    s.append(10)
    # Way 1st, only use simply max()
    assert s.getMax1() == 10
    assert s.getMax2() == 10
    assert s.getMax3() == 10
    s.pop()
    assert s.getMax1() == 6
    assert s.getMax2() == 6
    assert s.getMax3() == 6



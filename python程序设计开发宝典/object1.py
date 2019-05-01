class Test:
    '''This is a test'''

class Root:
    __total=0

    def __init__(self,v):
        self.__value = v
        Root.__total+=1
    def show(self):
        print("self.__value:",self.__value)
        print("Root.__total:",Root.__total)

    @classmethod
    def classShowTotal(cls):
        print(cls.__total)
    @staticmethod
    def staticShowTotal():
        print(Root.__total)


class myDeque:
    def __init__(self,iterable=None,maxlen=10):
        if iterable == None:
            self._content = []
            self._current = 0
        else:
            self._content = list(iterable)
            self._current = len(iterable)
        self._size = maxlen
        if self._size < self._current:
            self._size = self._current
        
    def __del__(self):
        del self._content
    
    def setSize(self,size):
        if size<self._current:
            for i in range(size,self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    def appendRight(self,v):
        if self._current<self._size:
            self._content.append(v)
            self._current += 1
        else:
            print("the queue is full")
    
    def appendLeft(self,v):
        if self._current<self._size:
            self._content.insert(0,v)
            self._current += 1
        else:
            print("the queue is full")
    
    def popLeft(self):
        if self._content:
            self._current -= 1
            return self._content.pop(0)
        else:
            print("the queue is empty")
        
    def popRight(self):
        if self._content:
            self._current -= 1 
            return self._content.pop()
        else:
            print("the queue is empty")
        
    def rotate(self,k):
        if abs(k)>self._current:
            print('k must <= '+str(self._current))
            return
        self._content = self._content[-k:] + self._content[:-k]

    def reverse(self):
        self._content = self._content[::-1]

    def __len__(self):
        return self._current

    def __str__(self):
        return 'myDeque'+str(self._content)+',maxlen='+str(self._size)+')'

    __repr__ = __str__

    def clear(self):
        self._content = []
        self._current = 0

    def isEmpty(self):
        return not self._content

    def isFull(self):
        return self._current == self._size

class Stack:
    def __init__(self,maxlen=0):
        self._content = []
        self._size = maxlen
        self._current = 0
    
    def __del__(self):
        del self._content

    def clear(self):
        self._content = []
        self._current = 0
    
    def isEmpty(self):
        return not self._content

    def isFull(self):
        return self._current == self._size

    def setSize(self,size):
        if size < self._current:
            print('new size must >= '+str(self._current))
            return
        self._size = size
    
    def push(self,v):
        if self._current< self._size:
            self._content.append(v)
            self._current+=1
        else:
            print('stack is full')
    def pop(self):
        if self._content:
            self._current -= 1
            return self._content.pop()
        else:
            print('stack is empty')
    
    def __str__(self):
        return 'stack('+str(self._content)+',maxlen='+str(self._size)+')'
    __repr__ = __str__
    


class Set(object):
    def __init__(self,data=None):
        if data == None:
            self.__data = []
        else:
            if not hasattr(data,'__iter__'):
                raise Exception("必须提供可迭代的数据类型")
            temp = []
            for item in data:
                hash(item)
                if not item in temp:
                    temp.append(item)
            self.__data = temp
        
    def __del__(self):
        del self.__data

    def add(self,value):
        hash(value)
        if value not in self.__data:
            self.__data.append(value)
        else:
            print('元素已存在')
    
    def remove(self,value):
        if value in self.__data:
            self.__data.remove(value)
            print('删除成功')
        else:
            print('元素不存在，删除操作被忽略')
    
    def pop(self):
        if not self.__data:
            print('集合为空，弹出操作被忽略')
            return 
        import random 
        item = random.choice(self.__data)
        self.__data.remove(item)
        return item
    def __sub__(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception("类型错误")
        result = Set()
        for item in self.__data:
            if item not in anotherSet.__data:
                result.__data.append(item)
        return result

    def difference(self,anotherSet):
        return self-anotherSet

    def __or__(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception("类型错误")
        result = Set(self.__data)
        for item in anotherSet.__data:
            if item not in result.__data:
                result.__data.append(item)
        return result

    def union(self,anotherSet):
        return self | anotherSet

    def __and__(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception("类型错误")
        result = Set()
        for item in self.__data:
            if item in anotherSet.__data:
                result.__data.append(item)
        return result
    def __xor__(self,anotherSet):
        return (self-anotherSet) | (anotherSet-self)
    
    def __eq__(self,anotherSet):
        if not isinstance(anotherSet,Set):
            raise Exception("类型错误")
        if sorted(self.__data) == sorted(anotherSet.__data):
            return True
        return False

    def __iter__(self):
        return iter(self.__data)


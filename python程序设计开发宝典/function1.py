#PYthon程序设计开发宝典，
# 第五章 代码复用技术（一）函数，
# 5.11精彩案例赏析 ，
# p141
def demo5_1(*para):
    avg = sum(para)/len(para)
    g = [i for i in para if i>avg]
    return (avg,)+tuple(g)

def demo5_2(s):
    result = [0,0]
    for ch in s:
        if ch.islower():
            result[1]+=1
        elif ch.isupper():
            result[0]+=1
    return tuple(result)

def demo5_3(lst,k):
    x = lst[k-1::-1]
    y = lst[:k-1:-1]
    return list(reversed(x+y))

def demo5_4(t):
    print([1])
    line = [1,1]
    print(line)
    for i in range(2,t):
        r = []
        for j in range(0,i-1):
            r.append(line[j]+line[j+1])
        line = [1]+r+[1]
        print(line)

from collections import defaultdict

def demo5_5(t):
    triangle = defaultdict(int)
    for row in range(t):
        triangle[row,0] = 1
        print(triangle[row,0],end="\t")
        for col in range(1,row+1):
            triangle[row,col]=triangle[row-1,col-1]+triangle[row-1,col]
            print(triangle[row,col],end='\t')
        print()

def demo5_6(n):
    def isPrime(p):
        if p == 2:
            return True
        if p%2==0:
            return False
        for i in range(3,int(p**0.5)+1,2):
            if p%i==0:
                return False
        return True
    
    if isinstance(n,int) and n>0 and n%2==0:
        for i in range(2,n//2+1):
            if isPrime(i) and isPrime(n-i):
                print(i,'+',n-i,'=',n)

def demo5_7(m,n):
    p = m*n
    while m%n != 0:
        m,n = n,m%n
    return (n,int(p/n))
def demo5_7_1(m,n):
    import math
    r = math.gcd(m,n)
    return (r,int((m*n)/r))

def demo5_8(x,n):
    t1 = [i for i in x if i<n]
    t2 = [i for i in x if i>n]
    return t1+[n]+t2

def demo5_9(origin,userInput):
    if not (isinstance(origin,str) and isinstance(userInput,str)):
        print('The tow parameters must be strings.')
        return
    right = sum((1 for o,u in zip(origin,userInput) if o==u))
    return round(right/len(origin),2)

def demo5_10(n):
    if not isinstance(n,int):
        print("must be a integer")
        return
    import math
    result = []
    primes = [p for p in range(2,10000) if 0 not in [p%d for d in range(2,int(math.sqrt(p))+1)]]
    for p in primes:
        while n!=1:
            if n%p==0:
                n = n/p
                result.append(p)
            else:
                break
        else:
            result="*".join(map(str,result))
            return result
    if not result:
        return n

def demo5_11(maxValue=100,maxTimes=5):
    from random import randint
    value = randint(1,maxValue)
    for i in range(maxTimes):
        prompt = "start to guess:" if i==0 else"guess again:"
        try:
            x = int(input(prompt))
        except:
            print("must input an integer between 1 and ",maxValue)
        else:
            if x==value:
                print("congratulations")
                break
            elif x>value:
                print('too big')
            else:
                print('too small')
    else:
        print('game over ,FAIL')
        print('the value is ',value)

def demo5_12(v,n):
    assert type(n)==int and 0<v<10,'v must be integer between 1 and 9'
    result,t=0,0
    for _ in range(n):
        t=t*10+t
        result+=t
    return result


def demo5_13(lst,k):
    from itertools import cycle
    t_lst = lst[:]
    while len(t_lst)>1:
        c = cycle(t_lst)
        for _ in range(k):
            t = next(c)
        index = t_lst.index(t)
        t_lst = t_lst[index+1:]+t_lst[:index]
    return t_lst[0]

times = 0
def demo5_14(num,src,dst,temp=None):
    global times 
    assert type(num)==int,'num must be an integer'
    assert num>0,'num must > 0'
    if num == 1:
        print('the {0} times move:{1}=>{2}'.format(times,src,dst))
        times+=1
    else:
        demo5_14(num-1,src,temp,dst)
        demo5_14(1,src,dst)
        demo5_14(num-1,temp,dst,src)

def demo5_15(n):
    L=[0]*n
    for i in range(1,2**n):
        b_i = bin(i)
        j = len(b_i)-b_i.rfind('1')-1
        print('第'+str(i)+'步:移动盘子'+str(j+1),chr(65+L[j]),'->',end=' ')
        L[j]=((L[j]+1)%3 if j%2==0 else (L[j]+2)%3)
        print(chr(65+L[j]))

def demo5_16(n):
    start = 10**(n-1)
    end = 10**n
    for i in range(start,end):
        big = ''.join(sorted(str(i),reverse=True))
        little = ''.join(reversed(big))
        big,little = map(int,(big,little))
        if big-little == i:
            print(i)


def demo5_17(v):
    from random import randint
    from itertools import permutations
    result = set()
    exps = ('((%s%s%s)%s%s)%s%s',
            '(%s%s%s)%s(%s%s%s)',
            '(%s%s(%s%s%s))%s%s',
            '%s%s((%s%s%s)%s%s)',
            '%s%s(%s%s(%s%s%s))')
    ops = r'+-*'
    def check(exp):
        try:
            return int(eval(exp))==24
        except:
            return False
    
    for a in permutations(v):
        t = [exp%(a[0],op1,a[1],op2,a[2],op3,a[3]) for op1 in ops for op2 in ops for op3 in ops for exp in exps if check(exp%(a[0],op1,a[1],op2,a[2],op3,a[3]))]
        if t:
            for item in t:
                result.add(item)
    return result

def isValid(s,col):
    row = len(s)
    for r,c in enumerate(s):
        if c==col or abs(row-r)==abs(col-c):
            return False
    return True

# 不懂 ，八皇后问题
def demo5_18(n,s=()):
    if len(s)==n:
        return[s]
    res = []
    for col in range(n):
        if not isValid(s,col): 
            continue
        for r in demo5_18(n,s+(col,)):
            res.append(r)
    return res

# 找零问题，不会
def demo5_19(total,changes=(1,2,5,10,20,50,100),result=None):
    if result is None:
        result=[]
    if total==0:
        yield result
    for change in changes:
        if change>total or (len(result)>0 and result[-1]<change):
            continue
        for r in demo5_19(total-change,changes,result+[change]):
            yield r


def demo5_20(iterable):
    tMax = tMin = iterable[0]
    for item in iterable[1:]:
        if item > tMax:
            tMax = item
        elif item < tMin:
            tMin = item
    return (tMax,tMin)

def demo5_21(iterable):
    for item in iterable:
        if not item:
            return False
    return True

def demo5_22(lst,reverse=False):
    length = len(lst)
    for i in range(length):
        flag = False
        for j in range(length-i-1):
            exp = 'lst[j]>lst[j+1]'
            if reverse:
                exp = 'lst[j]<lst[j+1]'
            if eval(exp):
                lst[j],lst[j+1] = lst[j+1],lst[j]
                flag = True
        if not flag:
            break

def demo5_23(lst,end=None,reverse=False):
    if end == None:
        length = len(lst)
    else:
        length = end
    if length<=1:
        return
    flag = False
    for j in range(length-1):
        exp = 'lst[j]>lst[j+1]'
        if reverse:
            exp = 'lst[j]<lst[j+1]'
        if eval(exp):
            lst[j],lst[j+1] = lst[j+1],lst[j]
            flag = True
    if not flag:
        return
    else:
        demo5_23(lst,length-1,reverse)


def demo5_24(lst,reverse=False):
    length = len(lst)
    for i in range(length):
        m = i
        for j in range(i+1,length):
            exp = 'lst[j]<lst[m]'
            if reverse:
                exp = 'lst[j]>lst[m]'
            if eval(exp):
                m = j
        if m!=i:
            lst[i],lst[m] = lst[m],lst[i]

def demo5_25(lst,value):
    start = 0
    end = len(lst)
    while start < end:  
        middle = (start+end)//2
        if value == lst[middle]:
            return middle
        elif value > lst[middle]:
            start = middle+1
        elif value < lst[middle]:
            end = middle-1
    return False

def demo5_26(lst,start,end,value):
    if start>end:
        return False
    mid = (start+end)//2
    midValue = lst[mid]
    if midValue == value:
        return mid
    elif midValue>value:
        return demo5_26(lst,start,mid-1,value)
    else:
        return demo5_26(lst,mid+1,end,value)

def demo5_27(lst,reverse = False):
    if len(lst) <=1:
        return lst
    pivot = lst.pop()
    first ,second = [],[]
    exp = 'x<=pivot'
    if reverse:
        exp = 'x>=pivot'
    for x in lst:
        first.append(x) if eval(exp) else second.append(x)
    return demo5_27(first,reverse)+[pivot]+demo5_27(second,reverse)


def demo5_28(lst):
    i=0
    length = len(lst)
    while i<length:
        if i==0 or lst[i-1]<=lst[i]:
            i+=1
        else:
            lst[i-1] ,lst[i] = lst[i],lst[i-1]
            i-=1

def demo5_29(seq,reverse=False):
    mid = len(seq)//2
    left,right = seq[:mid],seq[mid:]
    if len(left)>1:
        left = demo5_29(left,reverse)
    if len(right)>1:
        right = demo5_29(right,reverse)
    temp = []
    while left and right:
        if left[-1]>=right[-1]:
            temp.append(left.pop())
        else:
            temp.append(right.pop())
    temp.reverse()
    result = (left or right) + temp
    if reverse:
        i,j = 0,len(result)-1
        while i<j:
            result[i],result[j] = result[j],result[i]
            i+=1
            j-=1
    return result

def demo5_30(data,k,s=()):
    if len(s) == k and s[0]!=0:
        print(eval(''.join(map(str,s))))
    else:
        for item in data:
            if item not in s:
                demo5_30(data,k,s+(item,))

def demo5_31(lst):
    from itertools import combinations
    for length in range(len(lst),0,-1):
        for sub in combinations(lst,length):
            if list(sub) == sorted(sub):
                return sub 

def demo5_32(seq):
    seq = sorted(seq)
    dif = float('inf')
    for i,v in enumerate(seq[:-1]):
        d = abs(v-seq[i+1])
        if d<dif:
            first,second,dif = v,seq[i+1],d
    return (first,second)

def demo5_33(lst):
    from math import log
    num = len(lst)
    his = dict()
    for data in lst:
        his[data] = his.get(data,0)+1
    print(his)
    return abs(sum(map(lambda x:x/num*log(x/num,2),his.values())))
# 哈夫曼编码不会
def demo5_34(seq):
    from collections import Counter
    global temp
    temp = Counter(seq)
    for item in sorted(temp.items(),key=lambda x:x[1],reverse=True):
        print(item)
    print('='*20)
    seq = list(temp.keys())
    frq = [temp[t] for t in seq]
    tree = huffman(seq,frq)
    return codes(tree)

def huffman(seq,frq):
    from itertools import count
    from heapq import heapify,heappush,heappop
    num = count()
    trees = list(zip(frq,num,seq))
    heapify(trees)
    while len(trees)>1:
        fa,_,a = heappop(trees)
        fb,_,b = heappop(trees)
        heappush(trees,(fa+fb,next(num),[a,b]))
    return trees[0][-1]

def codes(tree,prefix=''):
    if len(tree) == 1:
        yield(tree,prefix)
        return
    for bit,child in zip('01',tree):
        for pair in codes(child,prefix+bit):
            yield pair

def demo5_35(maxNumber):
    lst = list(range(3,maxNumber,2))
    m = int(maxNumber**0.5)
    for index in range(m):
        current = lst[index]
        if current>m:
            break
        lst[index+1:] = list(filter(lambda x:x%current!=0,lst[index+1:]))
    return [2]+lst

def demo5_36(a,b):
    aa = list(map(int,reversed(str(a))))
    bb = list(map(int,reversed(str(b))))

    result = [0]*(len(aa)+len(bb))
    
    for ia,va in enumerate(aa):
        c=0
        for ib,vb in enumerate(bb):
            c,result[ia+ib]=divmod(va*vb+c+result[ia+ib],10)
        result[ia+ib+1] = c
    result = int(''.join(map(str,reversed(result))))
    return result

def demo5_37_1(lst,howFar):
    assert howFar>1,"howFar must > 1"
    start = 0
    ll = len(lst)
    while start<=ll:
        m = lst[start]
        loc = lst[start+1:start+howFar]
        mm = max(loc)
        if m>mm:
            return m
        else :
            mmPos = loc.index(mm)
            start+=mmPos+1
def demo5_37_2(lst,howFar):
    from random import random
    assert howFar>1,"howFar must > 1"
    start = 0
    ll = len(lst)
    times = 1
    while start<=ll:
        m = lst[start]
        loc = lst[start+1:start+howFar]
        if not loc:
            return m
        mm = max(loc)
        mmPos = loc.index(mm)
        if m<=mm:
            start+=mmPos+1
        else:
            delta = (m-mm)/(m+mm)
            if delta<=random()/times:
                start+=mmPos+1
                times+=1
            else:
                return m

def demo5_38(xs,func):
    vs = list(zip(xs,map(func,xs)))
    return sum(((v[0]-vs[i+1][0])**2+(v[1]-vs[i+1][1])**2)**0.5 for i,v in enumerate(vs[:-1]))

def 轮盘赌(奖项分布):
    from random import random
    本次转盘读数=random()
    for k,v in 奖项分布.items():
        if v[0]<=本次转盘读数<v[1]:
            return k
    
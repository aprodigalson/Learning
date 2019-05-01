def demo7_1(source,key):
    from itertools import cycle
    result = ''
    temp =  cycle(key)
    for ch in source:
        result = result + chr(ord(ch)^ord(next(temp)))
    return result


from random import choice,randint
import string
import codecs

StringBase = '\u7684\u4e00\u4e86\u662f\u6211\u4e0d\u5728\u4eba\u4eec\u6709\u6765\u4ed6\u8fd9\u4e0a\u7740\u4e2a\u5730\u5230\u5927\u91cc\u8bf4\u5c31\u53bb\u5b50\u5f97 \
\u4e5f\u548c\u90a3\u8981\u4e0b\u770b\u5929\u65f6\u8fc7\u51fa\u5c0f\u4e48\u8d77\u4f60\u90fd\u628a\u597d\u8fd8\u591a\u6ca1\u4e3a\u53c8\u53ef\u5bb6\u5b66 \
\u53ea\u4ee5\u4e3b\u4f1a\u6837\u5e74\u60f3\u751f\u540c\u8001\u4e2d\u5341\u4ece\u81ea\u9762\u524d\u5934\u9053\u5b83\u540e\u7136\u8d70\u5f88\u50cf\u89c1 \
\u4e24\u7528\u5979\u56fd\u52a8\u8fdb\u6210\u56de\u4ec0\u8fb9\u4f5c\u5bf9\u5f00\u800c\u5df1\u4e9b\u73b0\u5c71\u6c11\u5019\u7ecf\u53d1\u5de5\u5411\u4e8b \
\u547d\u7ed9\u957f\u6c34\u51e0\u4e49\u4e09\u58f0\u4e8e\u9ad8\u624b\u77e5\u7406\u773c\u5fd7\u70b9\u5fc3\u6218\u4e8c\u95ee\u4f46\u8eab\u65b9\u5b9e \
\u5403\u505a\u53eb\u5f53\u4f4f\u542c\u9769\u6253\u5462\u771f\u5168\u624d\u56db\u5df2\u6240\u654c\u4e4b\u6700\u5149\u4ea7\u60c5\u8def\u5206\u603b\u6761 \
\u767d\u8bdd\u4e1c\u5e2d\u6b21\u4eb2\u5982\u88ab\u82b1\u53e3\u653e\u513f\u5e38\u6c14\u4e94\u7b2c\u4f7f\u5199\u519b\u5427\u6587\u8fd0\u518d\u679c \
\u600e\u5b9a\u8bb8\u5feb\u660e\u884c\u56e0\u522b\u98de\u5916\u6811\u7269\u6d3b\u90e8\u95e8\u65e0\u5f80\u8239\u671b\u65b0\u5e26\u961f\u5148\u529b \
\u5b8c\u5374\u7ad9\u4ee3\u5458\u673a\u66f4\u4e5d\u60a8\u6bcf\u98ce\u7ea7\u8ddf\u7b11\u554a\u5b69\u4e07\u5c11\u76f4\u610f\u591c\u6bd4\u9636 \
\u8fde\u8f66\u91cd\u4fbf\u6597\u9a6c\u54ea\u5316\u592a\u6307\u53d8\u793e\u4f3c\u58eb\u8005\u5e72\u77f3\u6ee1\u65e5\u51b3\u767e\u539f\u62ff\u7fa4 \
\u7a76\u5404\u516d\u672c\u601d\u89e3\u7acb\u6cb3\u6751\u516b\u96be\u65e9\u8bba\u5417\u6839\u5171\u8ba9\u76f8\u7814\u4eca\u5176\u4e66\u5750 \
\u63a5\u5e94\u5173\u4fe1\u89c9\u6b65\u53cd\u5904\u8bb0\u5c06\u5343\u627e\u4e89\u9886\u6216\u5e08\u7ed3\u5757\u8dd1\u8c01\u8349\u8d8a\u5b57\u52a0\u811a\u7d27\u7231\u7b49\u4e60\u9635\u6015\u6708\u9752\u534a\u706b\u6cd5\u9898\u5efa\u8d76\u4f4d\u5531\u6d77\u4e03\u5973\u4efb\u4ef6\u611f \
\u51c6\u5f20\u56e2\u5c4b\u79bb\u8272\u8138\u7247\u79d1\u5012\u775b\u5229\u4e16\u521a\u4e14\u7531\u9001\u5207\u661f\u5bfc\u665a\u8868\u591f\u6574\u8ba4\u54cd\u96ea\u6d41\u672a\u573a\u8be5\u5e76\u5e95\u6df1\u523b\u5e73\u4f1f\u5fd9\u63d0\u786e\u8fd1\u4eae\u8f7b\u8bb2\u519c\u53e4\u9ed1 \
\u544a\u754c\u62c9\u540d\u5440\u571f\u6e05\u9633\u7167\u529e\u53f2\u6539\u5386\u8f6c\u753b\u9020\u5634\u6b64\u6cbb\u5317\u5fc5\u670d \
\u96e8\u7a7f\u5185\u8bc6\u9a8c\u4f20\u4e1a\u83dc\u722c\u7761\u5174\u5f62\u91cf\u54b1\u89c2\u82e6\u4f53\u4f17\u901a\u51b2\u5408\u7834 \
\u53cb\u5ea6\u672f\u996d\u516c\u65c1\u623f\u6781\u5357\u67aa\u8bfb\u6c99\u5c81\u7ebf\u91ce\u575a\u7a7a\u6536\u7b97\u81f3\u653f\u57ce \
\u52b3\u843d\u94b1\u7279\u56f4\u5f1f\u80dc\u6559\u70ed\u5c55\u5305\u6b4c\u7c7b\u6e10\u5f3a\u6570\u4e61\u547c\u6027\u97f3\u7b54\u54e5 \
\u9645\u65e7\u795e\u5ea7\u7ae0\u5e2e\u5566\u53d7\u7cfb\u4ee4\u8df3\u975e\u4f55\u725b\u53d6\u5165\u5cb8\u6562\u6389\u5ffd\u79cd\u88c5 \
\u9876\u6025\u6797\u505c\u606f\u53e5\u533a\u8863\u822c\u62a5\u53f6\u538b\u6162\u53d4\u80cc\u7ec6' 


def getEmail():
    suffix = ['.com','.org','.net','.cn']
    characters = string.ascii_letters+string.digits+'_'
    username = ''.join((choice(characters) for i in range(randint(6,12))))
    domain = ''.join(choice(characters) for i in range(randint(3,6)))
    return username+'@'+domain+choice(suffix)

def getTelNo():
    return ''.join((str(randint(0,9)) for i in range(11)))

def getNameOrAddress(flag):
    if flag==0:
        rangestart,rangeend = 2,5
    elif flag==1:
        rangestart,rangeend = 10,30
    result = ''.join((choice(StringBase) for i in range(randint(rangestart,rangeend))))
    return result

def getSex():
    return choice(('男','女'))

def getAge():
    return str(randint(18,100))

def main(filename):
    with codecs.open(filename,'w','utf-8') as fp:
        fp.write('Name,Sex,Age,TelNo,Address,Email\n')
        for _ in range(200):
            name = getNameOrAddress(0)
            sex = getSex()
            age = getAge()
            telNo = getTelNo()
            address = getNameOrAddress(1)
            email = getEmail()
            line = ','.join([name,sex,age,telNo,address,email])+'\n'
            fp.write(line)
def output(filename):
    with codecs.open(filename,'r','utf-8') as fp:
        for line in fp:
            line = line.split(',')
            for i in line:
                print(i,end=',')
            print()


def demo7_3(pwd):
    if not isinstance(pwd,str) or len(pwd)<6:
        return "not suitable for password"
    
    d = {1:'weak',2:'below middle',3:'above middle',4:'strong'}

    r = [False]*4
    
    for ch in pwd:
        if not r[0] and ch in string.digits:
            r[0] = True
        elif not r[1] and ch in string.ascii_lowercase:
            r[1] = True
        elif not r[2] and ch in string.ascii_uppercase:
            r[2] = True
        elif not r[3] and ch in ',.!;?<>':
            r[3] = True

    return d.get(r.count(True),'error')

import re
def demo8_1():
    telNumber = '''suppose my phone is 0253-1234654,
                yours is 021-12345633,
                his is 021-4564465.'''
    pattern = re.compile(r'(\d{3,4})-(\d{7,8})')
    index = 0
    while True:
        matchResult = pattern.search(telNumber,index)
        if not matchResult:
            break
        print('-'*30)
        print('success:')
        for i in range(3):
            print('searched content:',matchResult.group(i),\
                ' start from:',matchResult.start(i),'end at:',matchResult.end(i),\
                    'its span is:',matchResult.span(i))
        index = matchResult.end(2)

import os 
import sys

classes = {}
functions = [] 
variables = {'normal':{},'parameter':{},'infor':{}}

def _identifyClassName(index,line):
    pattern = re.compile(r'(?<=class\s)\w+(?=.*?:)')
    matchResult = pattern.search(line)
    if not matchResult:
        return
    className = matchResult.group(0)
    classes[className] = classes.get(className,[])
    classes[className].append(index)

def _identifyFunctionNames(index,line):
    pattern = re.compile(r'(?<=def\s)(\w+)\((.*?)\)(?=:)')
    matchResult = pattern.search(line)
    if not matchResult:
        return 
    functionName= matchResult.group(1)
    functions.append((functionName,index))
    parameter = matchResult.group(2).split(r',')
    if parameter[0]=='':
        return
    for v in parameter:
        variables['parameter'][v] = variables['parameter'].get(v,[])
        variables['parameter'][v].append(index)


def _identifyVariableNames(index, line):
    pattern = re.compile(r'\b(.*?)(?=\s=)')
    matchResult = pattern.search(line)
    if matchResult :
        vs = matchResult.group(1).split(r',')
        for v in vs:
            if 'if' in v:
                v=v.split()[1]
            if '[' in v:
                v = v[0:v.index('[')]
            variables['normal'][v] = variables['normal'][v].get(v,[])
            variables['normal'][v].append(index)

    pattern = re.compile(r'(?<=for\s)(.*?)(?=\sin)')
    matchResult = pattern.search(line)
    if matchResult:
        vs = matchResult.group(1).split(r',')
        for v in vs:
            variables['infor'][v] = variables['infor'][v].get(v,[])
            variables['infor'][v].appecnd(index)


def output1():
    print('='*20)
    print('class name and line number:')
    for key,value in classes.items():
        print(key,':',value)
    print('='*20)
    print('function name and line number:')
    for i in functions:
        print(i[0],':',i[1])
    print('='*20)
    print('the normal variable name and line number:')
    for key,value in variables['normal'].items():
        print(key,':',value)
    print('-'*20)
    print('the parameter variable name and line number:')
    for key,value in variables['parameter'].items():
        print(key,':',value)
    print('-'*20)
    print('the in for variable name and line number:')
    for key,value in variables['infor'].items():
        print(key,':',value)


def comments(index,allLines):
    for i in range(50):
        line = allLines[index+i].strip()
        if line.endswith('"""') or line.endswith("'''"):
            return i+1

def demo8_2(filename):
    if not os.path.isfile(filename):
        print('filename is not a file')
        sys.exit(0)
    allLines = []
    with open(filename,'r') as fp:
        allLines = fp.readlines()
    index = 0
    totalLen = len(allLines)
    while index < totalLen:
        line = allLines[index]
        line = line.strip()
        if line.startswith('#'):
            index+=1
            continue
        if line.startswith('"""') or line.startswith("'''"):
            line+=comments(index,allLines)
            continue
        _identifyClassName(index+1,line)
        _identifyFunctionNames(index+1,line)
        _identifyVariableNames(index+1,line)
        index+=1
    output1()



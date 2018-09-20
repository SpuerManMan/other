#coding=utf-8

import os,sys,random
import  subprocess
cmd='netfly.exe'
def netfly():
    panpath = 'D:\\netfly'
    ts=os.listdir(panpath)
    for tst in ts:
        #print(tst)
        t = os.path.join(panpath, tst)
        if os.path.isdir(t):
            print(t)
            os.chdir(t)
            subprocess.call(cmd, shell=True)


L = ['haha','xixi','hehe','heihei','gaga']

print(L[-1::-1])

def strim(str):
    if str[:1]==" ":
        str=str[1:]
    elif str[-1:]==" ":
        str=str[:-2]
    return str

print(strim("    eeeeeee "))


def strim1(str):
    while(str[:1]=="."):
        str=str[1:]
    while(str[-1:]=="."):
        str=str[:-2]
    return str

print(strim1("...eeeeeee..."))

qq = ''.join(
    str(random.choice(range(10))) for l in range(9)
)

q=[]
for i in range(10):

    l=str(random.choice(range(10)))
    q.append(l)
s=''.join(q)
print(s)

article_title='Django 教程'
tag_name = article_title.split(' ',1)[0]

print(tag_name)



def createCounter():
    def counter(j):
        def sum():
            return j+j
        return sum
    fs=[]
    for i in range(1,4):
        fs.append(counter(i))
    return fs

fs,fs1,fs2=createCounter()
print(fs())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs



def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1(),f2(),f3())
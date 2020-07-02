#!/usr/bin/env python
# coding: utf-8

# ### 0528 파이썬 첫날

# In[5]:


1<3


# In[12]:


a='Enjoy'
b='python!'
c=a+b
print(c)
print(a*3 + b*3)
print(3*(a+b))


# In[18]:


str1="Hello"
str2="World"
str1+str2


# In[33]:


list=[0,1,2,3,4,5,6,7,8,9]
print(list)
print(list[0:4])
print(list[:4])
print(list[1:])
print(list[::2])
print(list[2::3])
list=list+[10,11,12,13]
print(list)
list[3::3]
list[1::]
print(list[10::-1])
print(list[:])
print(list[:-1])


# In[55]:


print("%d"%100)
print("%d"%(100*10))
print("%d %d"%(100,200))
print("%05d %x %o %5.2f %c %s"%(100,100,100,3.5,"a","abcd"))
print("%0")
#x 16진수, o 8진수 f float
#%5.2f ; 5자리 중에 소수점 2자리
#%05d ; 5자리 중에 부족한 부분은 0으로 표현


# In[57]:


print("{} {}".format(1,"one")) 
#변수가 들어갈 자리에 각 각 format으로 차례대로 넣는다


# In[142]:


print("{0:d} {1:5d} {2:05d} ".format(123,123456,123))

#{변수의 위치정보,_자리 decimal로 표현}


# In[70]:


a = 123
type(a)


# In[75]:


a=100**100
print(a)
type(a)


# In[77]:


a=0xff #hexa
b=0o77 #octa
c=0b111 #binary 
print(a,b,c)


# In[90]:


a = 3.14
b=3.14e5
c=3.14e-5

print(a,b,c)


# In[103]:


print(str1)
print(str1[::2])
print(str1[1::2])
#글자 뒤에서 앞으로 (거꾸로) 쓰려면...?


# In[145]:


myFriends=['James','Robert','Lisa','Mary']

myFriends.append('Thomas')
myFriends.insert(1,'Paul')
myFriends.extend(['Laura','Bety'])
myFriends.remove('Laura')
popFriend=myFriends.pop()
indexFriend=myFriends.index('Lisa')
countFriend =myFriends.count('Mary')
myFriends.sort()
myFriends.reverse()
print(myFriends,popFriend)


# In[149]:


aa=[1,20,3,40,5]
aa.sort() #sort: 원본 객체를 update 함
print(aa)


# In[152]:


aa=[1,20,3,40,5]
print(sorted(aa))
x=sorted(aa) #sorted: 원본 (객체)를 바꾸지 않음
print(x)
print(aa)


# In[159]:


# list_queue=[]
# list_stack=[]


# list_queue_insert=list_queue.insert(0)
# list_queue_pop=list_queue.pop()

# list_stack_insert=list_stack.append()
# list_stack_pop=list_stack.pop()


list_queue=[]
list_queue.insert(0,1)
print(list_queue)
list_queue.insert(0,2)
print(list_queue)
list_queue.pop()
print(list_queue)


list_stack=[]

list_stack.append(1)
print(list_stack)
list_stack.append(2)
print(list_stack)
list_stack.append(3)
print(list_stack)
list_stack.pop()
print(list_stack)


# In[168]:


a=[1,2,3,4,5]
b=['a']
#1 in a
1 not in a
print(1 in a,1 not in a, 'a' in b,min(a),max(a),len(a),len('anc'))


# In[170]:


a=[1,2,3]
b=[1,2,3]
a==b


# In[187]:


a = [1,2,3,4,5,6,7,8,9]
b = a
print(a,b)
print(a==b)
b[4]=10
print(a,b)

c=list(a)
print(a,c)
c[4]=100
print(a,c)


# In[210]:


tup1=(1,2,3)
tup2=(9)
tup3=(9,)
print(tup1[::2])
print(tup2, tup3, type(tup2), type(tup3))


# In[211]:


dict_data={'a':1,'b':2,'c':3,'d':4}
dict_items=list(dict_data.items())
dict_items[0]


# In[209]:


country_capital={"영국":"런던","프랑스":"파리","스위스":"베른","호주":"멜버른","덴마크":"코펜하겐"}
print(country_capital["영국"])
country_capital["호주"]="캔버라"
print(country_capital)
del country_capital["덴마크"]
print(country_capital)
print(country_capital.keys())
print(country_capital.values())
print(country_capital.items())
dict={"대한민국":"서울"}
print(country_capital.update({"미국":"워싱턴DC"}))
print(country_capital)


# In[212]:


country_capital.values()[0]
#return 이 안된다! list로 casting해서 바꿔줘야 한다~
list(country_capital.values())[0] #<-?   


# In[265]:


a=['a','b','c','d']
b=['a','b','d']
for num in a:
    if ((num in b)==False): 
        print( num, "is not in list")
        
#sol 2
for val in b:
    a.remove(val)
print(a)

#sol 3
for i in range(len(a)):
    if a[i] not in b:
        print(a[i])


# In[4]:



#rand_num=random.randint(0,10)
print(rand_num)


# In[ ]:


# lst = []
# #0~9까지 4개 (중복x)
import random

set1={}
lst=[]

# while(len(set)<4):
#     rand_num=random.randint(0,10)
#     set1.add(rand_num)
#     print(set)

rand_num=random.randint(0,10)
#lst.insert(rand_num)

while(len(lst)<4):
    rand=random.randint(0,10)
    if(rand in lst ==False):
        lst.append(rand)
print(lst)


# In[12]:


lst1=[1,2,3,4,5,6,7]
lst2=[i**2 for i in lst1]
lst3=lst1 + lst2 * 3
print(lst2)
print(lst3)
lst4=[i**2 for i in lst1 if i%2==0]
print(lst4)


# In[15]:


help(sep)


# In[23]:


yourName=input("당신의 이름은?")
print("당신은 {}이군요. 반가워요".format(yourName),type(yourName))


# In[26]:


a=input("소가 계단을 오르면?")
if(a=="소오름"):
    print("정답이다!")
else: print("오답이다!")


# In[35]:


#피타고라스 정리를 만족하는 삼각형을 모두 찾아주세요옷~!
#삼각형 한 변의 길이는 1부터 30이하다.

ans=[]
for i in range(1,30):
    for j in range(1,30):
        for k in range(1, 30):
            if(k**2==(i**2+j**2)):
                ans.append((i,j,k))
print(ans)


# In[55]:


ans=[]
for i in range(1,30):
    for j in range(1,30):
        for k in range(1, 30):
            if(i<j<k):
                if(k**2==(i**2+j**2)):
                    ans.append((i,j,k))
print(ans)
len(ans)


# In[59]:


#sol
nlst=[]
for x in range(1,30):
    for y in range(x,30):
        for z in range(y,30):
            if(x**2+y**2==z**2):
                nlst.append((x,y,z))
print(nlst)


# In[61]:


#sol - comprehension
nlst=[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2+y**2==z**2]
print(nlst)


# In[122]:


st = "this is a string"
for c in st:
    print(c)

lst=list(st)
print(lst)


# In[89]:


#
#lst = ['this', 'is', 'a', 'string']
ans=[]
count=0
tmp=""
while(count<len(st)):
    if(st[count]!=' '):
        tmp=tmp+(st[count])
        if(count+1==len(st)):
            ans.append(tmp)
    else:
        ans.append(tmp)
        tmp=""
    count=count+1
print(ans)


# In[83]:


#sol
st="This is a string"
tmp=''
lst=[]
for i in range(len(st)):
    if st[i] != ' ':
        tmp += st[i]
        if i ==(len(st)-1): #마지막 글자를 append 함
            lst.append(tmp)
    else:
            lst.append(tmp)
            tmp = ''
print(lst)


# In[90]:


a="a"
b="b"
c=a+b
print(c)


# In[93]:


splt=st.split()
print(splt)
type(splt)


# In[95]:


st="this.is.a.string"
st.split('.')


# In[97]:


print(st)
st.find("is") #2번째 index에서 처음으로 나옴


# In[99]:


print(st)
st.replace('is','IS_REAL')


# In[105]:


print(st.upper(), st.lower(),"    ", st.swapcase(), st.title())
#swapcase: L->U, U->L
#Title: 첫 단어->Upper case


# In[121]:


st.count('is')
st.count('a')
st.index('a')
st.index('')
st.find('home')
#문자안에 찾는게 없으면
#find: -1 return
#index: error
#index는 확실할 때 쓴다


# In[119]:


st.startswith('th'), st.endswith('ng')


# In[2]:


st="This.is.a.string"
lst=[]

for c in set(st):
    lst.append((c,st.count(c)))
print(lst)


# In[126]:


tmp=(1,2,3,4)
tmp[1]


# In[ ]:


#야구게임
#목표는 4B! 유저에게 물어봅시다!@@
#숫자 중복 X


# In[1]:


import random
com=[]
while(len(com)<4):
    rand=random.randint(0,9)
    if(rand not in com):
        com.append(rand)
print(com)


# In[9]:


print("안녕 인간. 나는 컴퓨터. 게임을 시작하지. \n")
hh=input()
hum=[]
for i in input:
    hum.append(int(i))
print(hum)
# while(hum)


# In[4]:


a="1234"
b="1324"
a==b


# In[12]:


print("안녕 인간. 나는 컴퓨터. 게임을 시작하지. \n")
hh=input("____")
hum=[]
for i in input:
    hum.append(int(i))
print(hum)
# while(hum)


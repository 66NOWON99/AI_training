#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#야구게임
#목표는 4B! 유저에게 물어봅시다!@@
#숫자 중복 X


# In[2]:


# import random
# comp=[]
# while(len(comp)<4):
#     rand=random.randint(0,9)
#     if(rand not in comp):
#         comp.append(rand)

comp="1234"

print(comp)


# In[9]:


print("안녕 인간. 나는 컴퓨터. 게임을 시작하지. \n")
hh=input()
# hum=[]
# for i in hh:
#     hum.append(int(i))
# print(hum)
# while(hum)
print(hh)


# In[11]:


s=0
b=0
if(hh==comp):
    print("정답이다.")
else:
    while(hh!=comp):
        for i in range(4):
            if hh[i] in comp:
                if hh[i]==comp[i]:
                    s=s+1
                else: 
                    b=b+1
        print("S:",s," B:",b )

        s=0
        b=0
        hh=input("다시해라 인간\n")

    print("정답이다!")


# In[13]:


#str.replace logic
str="this is a string"
str1=str.replace("is","IS")
print(str1)

#logic
#let set str.replace(a,b)
for i in str:
    if(i==a):
        str[i]==b
    
    


# In[ ]:


#str.find(a)

if a not in str:
    return -1
else: # a is in str
    for i in len(str):
        if(str[i]==a):
            return i
        


# In[ ]:


#str.startswith(a)
if len(str)>0:
    if str[0]==a:
        return True
    else:
        return False


# In[14]:


#str.endswith(a)
if len(str)>0:
    if str[len(str)-1]==a:
        return True
    else:
        return False


# In[15]:


#str.title
if len(str)>0:
    tmp=str.split()
    for i in lenth(tmp):
        tmp[i][0]
        
    
    
    


# In[26]:


t="this is a string"
tp=t.split()
print(tp)
k=tp[0][0]
k.upper()


# In[29]:


a=t[0]
a.upper()
t=a+


# In[35]:


t="this is a string"
print(t[3])


# In[44]:


str="this is a string "
lst=[]
for c in str:
    lst.append(c)
# print(lst)

if len(lst)>0:
    t=lst[0].upper()
    lst[0]=t
    
    for i in range(1,len(str)):
        if(lst[i-1]==" "):
            m=lst[i].upper()
            lst[i]=m

print(lst)


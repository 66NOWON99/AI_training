#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#야구게임
#목표는 4B! 유저에게 물어봅시다!@@
#숫자 중복 X


# In[ ]:


import random
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


# In[ ]:


s=0
b=0
while(s!=4):
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
    


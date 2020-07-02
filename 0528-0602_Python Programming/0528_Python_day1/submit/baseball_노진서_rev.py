#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Baseball Game!
#Goal= 4B! Let's play!@@
#숫자 중복 X


# In[8]:


import random
comp=[]
while(len(comp)<4):
    rand=random.randint(0,9)
    if(rand not in comp):
        comp.append(rand)

# comp="1234"

print(comp)


# In[9]:


s=0
b=0
result=0

print("Hi human! Let's play game! \n")
print("no redundant number please!\n")
while(result!=1):
    s=0
    b=0
    ini=input("Guess 4 digits!\n")
    hum=[]
    for i in ini:
        hum.append(int(i))

    if(hum==comp):
        print("You Win!")
        result=1
    
    else:
        print("YoU LoSe!")
        for i in range(4): #len(comp): #
            if hum[i] in comp:
                if hum[i]==comp[i]:
                    s=s+1
                else: 
                    b=b+1
        print("S:",s," B:",b )


# In[ ]:





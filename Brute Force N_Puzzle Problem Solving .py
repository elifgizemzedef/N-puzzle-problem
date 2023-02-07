#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random

# In[2]:


n=4#int(input())
m =n

# In[3]:


array=["*"]

# In[4]:


for i in range(1,pow(n,2)):
    array.append(i)
    

# In[5]:


array

# puzzle=[]
# for i in range(0,pow(n,2)):
#     x=random.choice(array)
#     puzzle.append(x)
#     array.remove(x)

# n_puzzle=np.array(puzzle).reshape(n,n)

# In[6]:


n_puzzle=np.array(array).reshape(n,n)

# In[7]:


array

# In[8]:


n_puzzle.shape

# In[9]:


n_puzzle[0,0]=="6"


# In[10]:


kontrol_puzzle=n_puzzle.copy()

# In[11]:


previous_direction="null"

# In[12]:



def choosewheretomove():
    global previous_direction
    for i in range(n):
        for x in range(m):
            directionlist=[]
            if n_puzzle[i,x]=="*":
                #print(i , x)
                if i!=n-1:
                    directionlist.append("down") 

                if i!=0:
                    directionlist.append("up")

                if x!=m-1:
                    directionlist.append("right")

                if x!=0:
                    directionlist.append("left")
                    #cycle önlemek için direction kontrolü
                while(True):
                    direction= random.choice(directionlist)
                    
                    if previous_direction=="right" and direction=="left":
                        continue
                    if previous_direction=="left" and direction=="right":
                        continue
                    if previous_direction=="up" and direction=="down":
                        continue
                    if previous_direction=="down" and direction=="up":
                        continue
                    else:
                        break
                previous_direction=direction
                #print(direction +" "+previous_direction)
                swap(i,x,direction)
                i=n
                x=m
                
            if x==m:
                break
                
        if i==n:
            break
                    
                    
                    

# In[13]:


def swap(i,j,direction):
    
    if direction == "up":
        temp=n_puzzle[i-1,j]
        n_puzzle[i-1,j]=n_puzzle[i,j]
        n_puzzle[i,j]=temp
    elif direction == "down":
        temp=n_puzzle[i+1,j]
        n_puzzle[i+1,j]=n_puzzle[i,j]
        n_puzzle[i,j]=temp
    elif direction == "right":
        temp=n_puzzle[i,j+1]
        n_puzzle[i,j+1]=n_puzzle[i,j]
        n_puzzle[i,j]=temp
    elif direction == "left":
        temp=n_puzzle[i,j-1]
        n_puzzle[i,j-1]=n_puzzle[i,j]
        n_puzzle[i,j]=temp
    else:
        print ("aha zortladık.")
    

# In[14]:


for i in range(0,15):
    choosewheretomove();
    

# In[15]:


n_puzzle[1,0]



# In[ ]:


sayac=0
boolcontrol=True
while(boolcontrol):
    if sayac==7000000:
        break
    
    choosewheretomove()
    #print("kontrol zamanı")
    a=0
    for i in n_puzzle:
        b=0
        for x in i:
            if x == kontrol_puzzle[a,b] :
                boolcontrol=False
            else:
                boolcontrol=True
                break
            b=b+1
        if boolcontrol:
            break
        a=a+1
    print(n_puzzle, "\n")
    sayac=sayac+1
    
print(sayac)
        

# a=0
# for i in n_puzzle:
#     b=0
#     for x in i:
#         print(x)
#         if x == kontrol_puzzle[a,b] :
#             print("allah allah")
#         b=b+1
#     a=a+1
#         
#             
#         
# 

# In[ ]:


choosewheretomove()

# In[ ]:


n_puzzle

# In[ ]:


kontrol_puzzle

# In[ ]:




#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyttsx3


# In[1]:


import pyttsx3


# In[2]:


friend=pyttsx3.init()


# In[31]:


friend.say("Hii Man How are you?")


# In[32]:


friend.runAndWait()
voices = friend.getProperty('voices')
friend.setProperty('voice', voices[1].id)


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


# V 1.0
def exchange(nok_amount):
    nok_gbp = 12.56
    nok_usd = 9.55
    
    gbp_result = nok_amount / nok_gbp
    usd_result = nok_amount / nok_usd
    
    print("GBP: ", gbp_result)
    print("USD: ", usd_result)
    
exchange(100)


# In[ ]:





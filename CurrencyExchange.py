#!/usr/bin/env python
# coding: utf-8

# In[4]:


# V 1.4
def exchange(nok_amount):
    nok_gbp = 12.56
    nok_usd = 9.55
    nok_sek = 1.01
    
    gbp_result = nok_amount / nok_gbp
    usd_result = nok_amount / nok_usd
    sek_result = nok_amount / nok_sek
    
    print("GBP: ", gbp_result)
    print("USD: ", usd_result)
    print("SEK: ", sek_result)
    
exchange(100)


# In[ ]:





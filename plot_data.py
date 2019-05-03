#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import random

#get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


def show_random_image(X_data, y_data, num_rows = 2, num_columns = 4):
    fig=plt.figure(figsize=(20, 20))
    columns = num_columns
    rows = num_rows
    for i in range(1, columns*rows +1):
        random_int = random.randint(0,X_data.shape[0])
        img = X_data[random_int]
        fig.add_subplot(rows, columns, i)
        plt.imshow(img)
        plt.title(y_data[random_int])
    plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tarfile
from tqdm import tqdm_notebook as tqdm

# In[3]:



def unzip_tarfile(file_name):
    if (file_name.endswith("tar.gz")):
        tar = tarfile.open(file_name)
        for member in tqdm(iterable=tar.getmembers(), total=len(tar.getmembers())):
            tar.extract(member=member)
        tar.close()
    elif (file_name.endswith("tar")):
        tar = tarfile.open(file_name)
        for member in tqdm(iterable=tar.getmembers(), total=len(tar.getmembers())):
            tar.extract(member=member)
        tar.close()





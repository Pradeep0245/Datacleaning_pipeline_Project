#Hello All, this project was created in Jupyter Notebook and then converted to python executable script. Commands are arranged by their order of execution automatically.



import numpy as np
import pandas as pd


# In[4]:


df=pd.read_csv("/Users/pradeepprkakash/Downloads/dirty_cafe_sales.csv")


# In[10]:


df["Location"].unique()


# In[14]:


df["Location"]=df["Location"].replace("UNKNOWN",pd.NA)


# In[16]:


df["Location"].unique()


# In[17]:


df["Location"]=df["Location"].replace("ERROR",pd.NA)


# In[21]:


df["Total Spent"].unique()


# In[22]:


df["Total Spent"]=df["Total Spent"].replace("ERROR",pd.NA)


# In[28]:


df["Total Spent"]=df["Total Spent"].replace("UNKNOWN",pd.NA)
df


# In[30]:


df["Total Spent"].unique()


# In[33]:


df["Total Spent"]=pd.to_numeric(df["Total Spent"],errors="coerce")


# In[36]:


df
avg=df["Total Spent"].mean()


# In[40]:


df["Total Spent"] = df["Total Spent"].fillna(avg)


# In[42]:


df["Item"].unique()


# In[43]:


df = df.dropna(subset=["Item"])


# In[47]:


df["Item"]=df["Item"].replace("UNKNOWN",pd.NA)
df["Item"]=df["Item"].replace("ERROR",pd.NA)


# In[49]:


df=df.dropna(subset=["Item"])


# In[51]:


df["Quantity"].unique()


# In[52]:


df["Quantity"]=pd.to_numeric(df["Quantity"], errors="coerce")


# In[54]:


avg1=df["Quantity"].mean()
df["Quantity"]=df["Quantity"].fillna(avg1)


# In[56]:


df["Payment Method"].unique()


# In[57]:


df["Payment Method"]=df["Payment Method"].replace("ERROR",pd.NA)
df["Payment Method"]=df["Payment Method"].replace("UNKNOWN",pd.NA)


# In[59]:


df["Payment Method"]=df["Payment Method"].fillna("Cash")


# In[64]:


df["Location"]=df["Location"].fillna("In-store")
df.head(80)


# In[66]:


df["Transaction Date"]=df["Transaction Date"].replace("ERROR",pd.NA)


# In[68]:


df["Transaction Date"].unique()


# In[69]:


df["Transaction Date"]=df["Transaction Date"].dropna()


# In[78]:


df = df.dropna(subset=["Transaction Date"])


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# <hr style="border:5px solid #108999"> </hr>

# In[18]:


s= "hi i am pramod"
s.split( " ",3)


# In[2]:


s.split(" ")


# In[8]:


s.lstrip("hi ")


# In[20]:


s.rstrip("pramod")


# In[10]:


s.strip("id")


# In[31]:


s.upper()
s.lower()
s.capitalize()
s.title()
s.replace("pramod","sanketh")
s.startswith("hi")
s.endswith("pramod")


# In[76]:


s.isnumeric()
s.isdigit()
s.islower()


# In[62]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


s="price per unit"


# In[2]:


s.replace("price","cost")


# In[3]:


s.endswith("nit")


# In[4]:


s.startswith("pri")


# In[5]:


len(s.split())
print(s.split(" ",0))
print(s.split(" ",1))
print(s.split(" ",2))
s.split(" ")[2]


# In[6]:


len(s.split(" ",1))


# In[7]:


s.upper()


# In[27]:


s.lower()


# In[28]:


s.capitalize()


# In[29]:


s.title()


# In[42]:


s.strip(" ")


# In[31]:


s.strip("per")


# In[37]:


s.strip("pt")


# In[45]:


s.lstrip("price")
s.rstrip("unit")


# working with a string data in pandas
# and in series object

# In[53]:


import pandas as pd
sd= pd.Series(["employee satisfaction rating", "employee charm rate"])
sd[0].lstrip("employee")


# In[156]:


import pandas as pd
sd3= pd.DataFrame(data=[["employee satisfaction rating", "employee charm rate"],
                       ["employee satisfaction rating", "employee charm rate"]],
                columns=["column 1","column 2"],
                index=range(2))


# In[157]:



print(sd3.columns.str.lstrip("column"))
print(sd3.columns.str.lower())
sd3


# In[158]:


sd3.columns=sd3.columns.str.lstrip("columns").str.lower().str.replace(" ", "-")
sd3


# In[198]:


s2 = pd.Series(["a_b_c", "c_d_e", np.nan, "f_g_h"], dtype="string")
print(s2.str.split("_").str[2])
print(s2.str.split("_"))
print(s2.str.split("_",expand=True,n=1))
print(s2.str.rsplit("_",expand=True,n=1))


# In[226]:


s3 = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", "", np.nan, "CABA", "dog", "cat"],
    dtype="string",)

print(s3.str.replace("^.a|dog", "X", case=False, regex=True))
print(s3.str.replace("^.a|dog", "X", case=False, regex=True))


# In[246]:


dollars = pd.Series(["12", "-$10", "$10,000"], dtype="string")
print(dollars.str.replace(r"-\$", "-", regex=True))
print(dollars.str.replace(r"-\$", "-", regex=True))


# In[249]:


pat = r"[a-z]+"
def repl(m):
    return m.group(0)[::-1]
pd.Series(["foo 123", "bar baz", np.nan], dtype="string").str.replace(
    pat, repl, regex=True)


# In[274]:


pat = r"[a-z]+"
def repl(m):
    return m.group(0)[::-1]
pd.Series(["foo 123", "bar baz", np.nan], dtype="string").str.replace(
    pat, repl, regex=True)
#re.match attempts a match with the beginning of a string. For example, 
#here we try to locate any uppercase letters (+ denotes one or more) at the beginning of a string.
#r’[A-Z]+’  can be broken down as follow:

#[A-Z]: Capture all the uppercase characters

#+: Occurring once or more

#As a result, the output is the string MY.


# In[393]:


pat = r"(?P<one>\w+) (?P<two>\w+) (?P<three>\w+)"
def repl(m):
    return m.group(0).swapcase()#group(0/1/2) or group("one"/"two"/"three")
pd.Series(["Foo Bar Baz", np.nan], dtype="string").str.replace(pat, repl, regex=True)


# concatinate some list into series

# In[323]:


s = pd.Series(["a", "b", "c", "d"], dtype="string")
t = pd.Series(["a", "b", np.nan, "d"], dtype="string")
s.str.cat(["a", "b", "c", "d"])
s.str.cat(["a", "b", np.nan, "d"])
s.str.cat(t,na_rep=" a1,d")
t


# In[394]:


d=pd.concat([t,s],axis=1)#axis 0 for index and 1 for column
s.str.cat(d,na_rep="000")
d


# In[356]:


f = d.loc[[3, 2, 1, 0], :]
f2 = d.loc[[1, 3, 0, 2], :]
print(f)
print(f2)


# In[377]:


u = pd.Series(["b", "d", "a", "c"], index=[1, 2, 3, 0], dtype="string")
s.str.cat([u,u.to_numpy()], join="left")#series
g=pd.concat([s,u],axis=1)#data frame
j=u.to_numpy()#numpy object


# In[392]:


pd.Series(
    ["a1", "b2", "c3"],
    dtype="string",
).str.extract(r"([ab])(\d)",expand=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[54]:


sd[1].lstrip(" employee")


# In[58]:


pd.Series([sd[0].lstrip("employees"), sd[1].lstrip("employee")])


# In[57]:


sd.str.lstrip("employee")


# In[77]:


sd.str.match("employee charm rate")


# In[78]:


sd.str.match("employees")


# In[122]:


import numpy as np
print(np.random.randn(3,2))
print(np.random.randint(2,3))
print(np.random.random(10))
print(np.random.RandomState())
print(np.random.rand(10))


# In[ ]:





# ## Using the .format() Method <hr style="border:4.5px solid #108999"> </hr>

# Consider the following string.

# In[397]:


print("{} expect their next year's sales of Q{} to {}".format("comapany a",3,"increase"))


# Use the **.format()** method to substitute the pairs of braces in the string with the following three values, thus obtaining information about the sales of Company A for the third quarter of next year: 
# <br/> 'Company A'
# <br/> 3
# <br/> 'increase'

# In[ ]:





# Execute the next cell to create three variables that store information about companies, quarters and sales performance predictions, respectively.

# In[398]:


companies = ['Company A', 'Company B']
quarter = [1, 2, 3, 4]
sales_performance_prediction = ['increase', 'decrease', 'remain the same']


# Obtain the same output as above while referring to the three lists you just created. Use appropriate indexing to your benefit.
# <br/> Here's the output you need to aim for as a reference.
# <br/> "Company A expect their next year's sales of Q3 to increase."

# In[399]:


"{} expect their next year's sales of Q{} to {}".format(companies[0],quarter[2],sales_performance_prediction[0])


# Feel free to experiment with the same line of code while referencing different values from the three lists that have been given.

# Here's an example:

# In[403]:


"{0} expect their next year's sales of Q {2} to {1}.".format(companies[1], quarter[3], sales_performance_prediction[2])


# In[409]:


"{com[0]} expect their next year's sales of Q {quar[0]} to {sale[0]}.".format(
    com=companies, quar=quarter,sale= sales_performance_prediction)


# In[ ]:





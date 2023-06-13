#!/usr/bin/env python
# coding: utf-8

# In[51]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn import preprocessing
import sklearn
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle


# In[52]:


rain = pd.read_csv("/Users/rag/Desktop/rain2/rain.csv")


# In[53]:


rain.head()


# In[54]:


rain.shape


# In[55]:


#Feature Selection:
rain.drop(['WindSpeed3pm', 'Temp9am','Temp3pm'], axis=1, inplace=True)


# In[56]:


rain.head()


# In[57]:


#get unique locations
locations = rain['Location'].unique()
locations


# In[58]:


#Checking the missing values
rain.isnull().sum()


# In[59]:


rain2= rain.dropna()
rain2.shape


# In[60]:


rain2.isnull().sum()


# In[61]:


warnings.filterwarnings("ignore")


# In[62]:


rain2['RainToday'] = rain2['RainToday'].map({'Yes': 1, 'No': 0})


# In[63]:


rain2 = np.array(rain2)


# In[71]:


X = rain2[1:, 1:-1]
y = rain2[1:, -1]
y = y.astype('int')
X = X.astype('int')


# In[80]:


rain2


# In[81]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
log_reg = LogisticRegression()


# In[82]:


log_reg.fit(X_train, y_train)


# In[83]:


theinput=[int(x) for x in "45 32 60".split(' ')]
final=[np.array(theinput)]


# In[84]:


b = log_reg.predict_proba(final)
output='{0:.{1}f}'.format(b[0][1], 2)
print(output)


# In[85]:


pickle.dump(log_reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


# In[ ]:





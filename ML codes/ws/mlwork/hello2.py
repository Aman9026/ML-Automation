#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.datasets import mnist


# In[2]:


dataset = mnist.load_data('mymnist.db')


# In[3]:


len(dataset)


# In[4]:


train , test = dataset


# In[6]:


len(train)


# In[8]:


X_train , y_train = train


# In[9]:


X_train.shape


# In[10]:


X_test , y_test = test


# In[11]:


X_test.shape


# In[27]:


img1 = X_train[7]


# In[28]:


img1.shape


# In[15]:




# In[37]:


X_train.shape


# In[39]:


X_train_1d = X_train.reshape(-1 , 28*28)
X_test_1d = X_test.reshape(-1 , 28*28)


# In[40]:


X_train_1d.shape


# In[41]:


X_train = X_train_1d.astype('float32')
X_test = X_test_1d.astype('float32')


# In[42]:


X_train.shape


# In[43]:


y_train.shape


# In[44]:


from keras.utils.np_utils import to_categorical


# In[45]:


y_train_cat = to_categorical(y_train)


# In[46]:


y_train_cat


# In[48]:


y_train_cat[7]


# In[49]:


from keras.models import Sequential


# In[50]:


from keras.layers import Dense


# In[51]:


model = Sequential()


# In[52]:


model.add(Dense(units=512, input_dim=28*28, activation='relu'))


# In[53]:


model.summary()


# In[54]:


model.add(Dense(units=256, activation='relu'))


# In[55]:


model.add(Dense(units=128, activation='relu'))


# In[56]:


model.add(Dense(units=32, activation='relu'))


# In[57]:


model.summary()


# In[58]:


model.add(Dense(units=10, activation='softmax'))


# In[59]:


model.summary()


# In[60]:


from keras.optimizers import RMSprop


# In[61]:


model.compile(optimizer=RMSprop(), loss='categorical_crossentropy', 
             metrics=['accuracy']
             )


# In[62]:


h = model.fit(X_train, y_train_cat, epochs=20)


# In[64]:








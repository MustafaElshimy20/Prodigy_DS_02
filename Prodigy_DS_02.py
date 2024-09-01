#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Load Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic = pd.read_csv(url)


# In[3]:


# Data Cleaning: Handle missing values
titanic['Age'].fillna(titanic['Age'].median(), inplace=True)
titanic['Embarked'].fillna(titanic['Embarked'].mode()[0], inplace=True)


# In[4]:


# EDA: Example - Survival rate by gender
plt.figure(figsize=(8, 6))
sns.barplot(x='Sex', y='Survived', data=titanic)
plt.title('Survival Rate by Gender')
plt.show()


# In[6]:


# EDA: Example - Distribution of passenger age
plt.figure(figsize=(8, 6))
sns.histplot(titanic['Age'], bins=30, kde=True)
plt.title('Age Distribution of Titanic Passengers')
plt.show()


# In[ ]:





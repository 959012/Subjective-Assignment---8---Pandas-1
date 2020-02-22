#!/usr/bin/env python
# coding: utf-8

# # Assignment

# Q1. Write the Python program to add, subtract, multiply and divide
# two pandas series ?
# 
#     Sample Series- [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

# In[1]:


import pandas as pd
#Sample Series- [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
x = pd.Series([2,4,6,8,10])
y = pd.Series([1,3,5,7,9])


# In[2]:


x.add(y)


# In[3]:


x.subtract(y)


# In[4]:


x.multiply(y)


# In[5]:


x.divide(y)


# Q2. Write a Python program to convert a dictionary to the Pandas
# Series?
#     
#     Sample SeriesOriginal dictionary-
#     {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
#     Converted series -
#     a 100
#     b 200
#     c 300
#     d 400
#     e 800
#     dtype- int64

# In[6]:


a = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
data = pd.Series(a)
data


# Q3. Write a python program to change the data type of given a
# column or a Series?
# 
#     Sample SeriesOriginal Data Series0 100
#     1 200
#     2 python
#     3 300.12
#     4 400
#     dtype- object
#     Change the said data type to numeric0 100.00
#     1 200.00
#     2 NaN
#     3 300.12
#     4 400.00
#     dtype- float64
# 

# In[7]:


a = pd.Series(['100','200','python','300.12','400'])
data = pd.to_numeric(a, errors='coerce')
data


# Q4. Write the python pandas program to convert the first column of a
# DataFrame as a Series?
# 
#     Sample OutputOriginal DataFramecol1 col2 col3
#     0 1 4 7
#     1 2 5 5
#     2 3 6 8
#     3 4 9 12
#     4 7 5 1
#     5 11 0 11
#     1st column as a Series0 1
#     1 2
#     2 3
#     3 4
#     4 7
#     5 11
#     Name- col1, dtype- int64
#     <class 'pandas.core.series.Series'>

# In[8]:


a = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=a)
data = df.ix[:,0]
print(data)
print(type(data))


# Q5. Write a pandas program to create the mean and standard
# deviation of the data of a given Series?
# 
#     Sample OutputOriginal Data Series0 1
#     1 2
#     2 3
#     3 4
#     4 5
#     5 6
#     6 7
#     7 8
#     8 9
#     9 5
#     10 3
#     dtype- int64
#     Mean of the said Data Series4.81818181818
#     Standard deviation of the said Data Series2.52262489555

# In[9]:


data = pd.Series(data = [1,2,3,4,5,6,7,8,9,5,3])
print("Mean of the said Data Serie",data.mean())
print("Standard deviation of the said Data Series", data.std())


# Q6. Write a pandas program to get powers of an array values
# element-wise?
#  
# Note First array elements raised the powers from the second array.
# 
#     Sample data: {'X ':[78,85,96,80,86], ' Y ':[84,94,89,83,86],'Z':[86,97,96,72,83]}
#     Expected Output:
#     X Y Z
#     0 78 84 86
#     1 85 94 97
#     2 96 89 96
#     3 80 83 72
#     4 86 86 83

# In[10]:


#data: {'X ':[78,85,96,80,86], ' Y ':[84,94,89,83,86],'Z':[86,97,96,72,83]}
x = pd.DataFrame({'X ':[78,85,96,80,86], ' Y ':[84,94,89,83,86],'Z':[86,97,96,72,83]})
x


# Q7. Write the pandas program to get the first 3 rows of a given
# DataFrame?
# 
#     Sample Python dictionary data and list labelsexam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
#     'Matthew', 'Laura', 'Kevin', 'Jonas'],
#     'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#     'attempts'- [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#     'qualify'- [ 'yes', 'no', 'yes' , 'no', ' no ', ' yes ', 'yes', 'no', 'no', 'yes' ] }
#     labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ]
#     Expected OutputFirst three rows of the data frameattempts name qualify score
#     a 1 Anastasia yes 12.5
#     b 3 Dima no 9.0
#     c 2 Katherine yes 16.5

# In[11]:


import numpy as np
data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
    'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': [ 'yes', 'no', 'yes' , 'no', ' no ', ' yes ', 'yes', 'no', 'no', 'yes' ] }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ]
df = pd.DataFrame(data, labels)
df
#print(df.iloc[1:5])


# In[12]:


print(df.iloc[:3])


# Q8: Write the pandas program to select the specified columns and
# the rows from a given data frame?
# 
#     Sample Python dictionary data and list labelsSelect 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
#     exam_data = {'name ': [ 'Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
#     'Matthew', 'Laura', 'Kevin', 'Jonas'],
#     'score'- [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#     'attempts'- [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#     'qualify'- ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'] }
#     labels = ['a ', ' b ', ' c ', ' d ', ' e ', ' f ', ' g ', 'h', 'i', 'j']
#     Expected OutputSelect specific columns and rowsname score
#     b Dima 9.0
#     d James NaN
#     f Michael 20.0
#     g Matthew 14.5

# In[13]:


exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("Select specific columns and rows:")
print(df.iloc[[1, 3, 5, 6], [1, 3]])


# Q9. Write the pandas program to calculate mean score for each
# different student in DataFrame?
# 
#     Sample Python dictionary data and list labelsexam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
#     'Matthew', 'Laura', 'Kevin', 'Jonas'],
#     'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#     'attempts'- [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#     'qualify'- ['yes', 'no', ' yes ', ' no ', ' no ', ' yes ', ' yes ', ' no ', ' no ', ' yes '] }
#     labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#     Expected OutputMean score for each different student in data frame:
#     13.5625

# In[19]:


abelsexam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts':[1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', ' yes ', ' no ', ' no ', ' yes ', ' yes ', ' no ', ' no ', ' yes '] }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(abelsexam_data , index=labels)
#print(df)
print(df['score'].mean())


# Q10. Write the Pandas program to rename columns of a given
# DataFrame ?
# 
#     Sample dataOriginal data frame
#     col1 col2 col3
#     0 1 4 7
#     1 2 5 8
#     2 3 6 9
#     New data frame after renaming columns:
#     Column1 Column2 Column3
#     0 1 4 7
#     1 2 5 8
#     2 3 6 9

# In[24]:


a = {'col1':[1,2,3],'col2':[4,5,6],'col3':[7,8,9]}
data = pd.DataFrame(data=a)
data = data.rename(columns= {'col1':'Column1','col2':'Column2','col3':'Column3'})
data


# Q11. Write a pandas program to count city-wise number of people from
# a given of data set (city, name of the person)?
# 
#     Sample data-
#     city Number of people
#     0 California 4
#     1 Georgia 2
#     2 Los Angeles 4

# In[ ]:





# Q12. Write a pandas program to widen output display to see more
# columns?
#     
#     Sample dataOriginal data frame
#     col1 col2 col3
#     0 1 4 7
#     1 4 5 8
#     2 3 6 9
#     3 4 7 0
#     4 5 8 1

# In[33]:


a = {'col1':[1,4,3,4,5],'col2':[4,5,6,7,8],'col3':[7,8,9,0,1]}
data = pd.DataFrame(data=a)
data


# Q13. Write a pandas program to convert the data frame column type
# from string to DateTime?
#     
#     Sample dataString Date0 3/11/2000
#     1 3/12/2000
#     2 3/13/2000
#     dtype- object
#     Original DataFrame (string to datetime)-
#     0
#     0 2000-03-11
#     1 2000-03-12
#     2 2000-03-13

# In[37]:


a = pd.Series(['3/12/2000','3/13/2000'])
rv = pd.to_datetime(pd.Series(a))
rv


# Q14. Write a pandas program to append the data to an empty
# DataFrame?
# 
#     Sample dataOriginal DataFrame- After appending some data: col1 col2 0 0 0 1 1 1 2 2 2

# In[48]:


a = {'col1':[0,0,0],'col2':[1,1,1]}
data = pd.DataFrame()
b = pd.DataFrame(data=a)
data = data.append(b)
data


# Q15. Write a pandas program to count the number of columns of a
# DataFrame?
# 
#     Sample OutputOriginal DataFrame
#     col1 col2 col3
#     0 1 4 7
#     1 2 5 8
#     2 3 6 12
#     3 4 9 1
#     4 7 5 11
#     Number of columns- 3

# In[55]:


a = {'col':[1,2,3,4,7],'col2':[4,5,6,9,5],'col3':[7,8,12,1,11]}
data = pd.DataFrame(data=a)
print("Number of columns-",len(data.columns))


# Q16. Write a Pandas program to remove the last n rows of a given
# DataFrame ?
# 
#     Sample Output:
#     Original DataFrame
#     col1 col2 col3
#     0 1 4 7
#     1 2 5 5
#     2 3 6 8
#     3 4 9 12
#     4 7 5 1
#     5 11 0 11
#     After removing last 3 rows of the said DataFramecol1 col2 col3
#     0 1 4 7
#     1 2 5 5
#     2 3 6 8
#     
#      Link for Datasets
#      (https://drive.google.com/drive/folders/105ftuIwN9kqyPNEEm3E6IM7LqywjyvJa?usp=sharing)

# In[70]:


a = {'col':[1,2,3,4,7,11],'col':[4,5,6,9,5,0],'col3':[7,5,8,12,1,12]}
data = pd.DataFrame(data = a)
data1 = data.drop(data.tail(3).index)
data1


# Q17. Write a Pandas program to import excel data (coalpublic2013.xlsx
# ) into a Pandas data frame.

# In[ ]:


data = pd.read_excel('coalpublic2013.xlsx')


# Q18. Write a Pandas program to import excel data (coalpublic2013.xlsx
# ) into a data frame and find details where "Mine Name" starts with
# "P.
# 

# In[ ]:


data = pd.read_excel('coalpublic2013.xlsx')
data[data['Mine Name'].map(lambda x: x.startswith(p))]


# Q19. Write a Pandas program to import excel data (employee.xlsx )
# into a Pandas dataframe and find the list of employees where
# hire_date> 01-01-07.
# 

# In[ ]:


data = pd.read_excel('coalpublic2013.xlsx')
data[data['hire_date']== '20070101']


# Q20. Write a Pandas program to import excel data (employee.xlsx )
# into a Pandas dataframe and find a list of the employees of a specified
# year

# In[ ]:


data = pd.read_excel('coalpublic2013.xlsx')
data1 = [data['hire_date']=='2005']


# ## Great Job!

#!/usr/bin/env python
# coding: utf-8

# In[410]:


import pandas as pd

import matplotlib.pyplot as plt
df_companies = pd.read_csv('companies.txt', sep="\t",  skiprows=[0], names = ['company_permalink','name','homepage_url','category_list','status','country_code','state_code','region','city','founded_at'], encoding = "ISO-8859-1")
df_rounds2 = pd.read_csv('rounds2.csv', sep=",", encoding = "ISO-8859-1")

#How many unique companies are present in rounds2?
print("How many unique companies are present in rounds2?")
print(len(df_rounds2['company_permalink'].apply(lambda x:x.lower()).unique()))
df_rounds2['company_permalink'] = df_rounds2['company_permalink'].apply(lambda x:x.lower())

#How many unique companies are present in companies?
print("How many unique companies are present in companies?")
print(len(df_companies['company_permalink'].apply(lambda x:x.lower()).unique()))

#In the companies data frame, which column can be used as the unique key for each company? Write the name of the column.
print("In the companies data frame, which column can be used as the unique key for each company? Write the name of the column.")
if len(df_companies['company_permalink'].unique())==len(df_companies['company_permalink'].apply(lambda x:x.lower()).unique()):
    print('permalink is the unique key for each company in the companies data frame')
#convert the values to lower case since to compare should be case insensitive
df_companies['company_permalink'] = df_companies['company_permalink'].apply(lambda x:x.lower())

#Are there any companies in the rounds2 file which are not present in companies? Answer yes or no: Y/N
print("#Are there any companies in the rounds2 file which are not present in companies? Answer yes or no: Y/N")
if len(df_rounds2[~df_rounds2.company_permalink.isin(df_companies.company_permalink)].dropna())>0:
    print('Y')
else:
    print('N')

#pd.set_option('float_format','{:f}')
#Merge the two data frames so that all variables (columns) in the companies frame are added to the rounds2 data frame. Name the merged frame master_frame. How many observations are present in master_frame?
print("Merge the two data frames so that all variables (columns) in the companies frame are added to the rounds2 data frame. Name the merged frame master_frame. How many observations are present in master_frame?")
master_frame = pd.merge(df_rounds2, df_companies, on='company_permalink', how='inner')
print(len(master_frame))

#filter the data frame which does not have any funding_round_type and raised_amount_usd and funding_round_type is either 'venture','seed','angel','private_equity'
master_frame = master_frame[master_frame.funding_round_type.notnull() & master_frame.raised_amount_usd.notnull() & master_frame.funding_round_type.isin(['venture','seed','angel','private_equity'])] 


m = master_frame.groupby('funding_round_type')['raised_amount_usd']
print(m.count().astype(int))
print(m.mean().astype(int))


# In[411]:


#Checkpoint 3: Country Analysis
df_english_country = pd.read_csv('country.csv', sep=",", encoding = "ISO-8859-1")
m = master_frame[(master_frame.funding_round_type=='venture')]
top9_countries = m.groupby('country_code')['raised_amount_usd'].count().astype(int).sort_values(ascending=False).head(9).index.get_level_values('country_code').tolist()
top9 = m[m.country_code.isin(top9_countries)]
#eleminate the rows which does lies in the given investment range
top9 = top9.drop(top9[(top9.raised_amount_usd < 5000000)].index)
top9 = top9.drop(top9[(top9.raised_amount_usd < 15000000)].index)
print(top9[top9.country_code.isin(df_english_country.code)].groupby('country_code')['raised_amount_usd'].count().sort_values(ascending=False).head(3))


# In[412]:


#Checkpoint 4: Sector Analysis 1
df_mapping = pd.read_csv('mapping.csv', sep=",", encoding = "ISO-8859-1")
df_mapping['category_list'] = df_mapping[df_mapping.category_list.notnull()]['category_list'].apply(lambda x: x.replace('0', 'na').lower())
df_mapping['category_list'] = df_mapping['category_list'].apply(lambda x: "enterprise 2.0" if x=='enterprise 2.na' else x)
df_mapping = pd.melt(df_mapping,id_vars=["category_list"])

df_mapping = df_mapping[df_mapping.value != 0]

df_mapping = df_mapping.drop('value', axis=1)

df_mapping.rename(columns={'variable':'main_sector','category_list':'primary_sector'}, inplace=True)

df_mapping['primary_sector'] = df_mapping['primary_sector'].str.lower()
top9 = top9[top9.category_list.notnull()]

pd.options.display.float_format = '{:20,.2f}'.format
top9['primary_sector'] = top9['category_list'].apply(lambda x: x.split('|')[0].lower() if '|' in x else x.lower() )
top9 = pd.merge(top9, df_mapping, how='inner', on='primary_sector')
top9['main_sector'].dropna()
D1 = top9[(top9.country_code == 'USA')]
D2 = top9[(top9.country_code == 'GBR')]
D3 = top9[(top9.country_code == 'IND')]


# In[413]:


print(D1.raised_amount_usd.count())
print(D2.raised_amount_usd.count())
print(D3.raised_amount_usd.count())

print(D1.raised_amount_usd.mean())
print(D2.raised_amount_usd.mean())
print(D3.raised_amount_usd.mean())


# In[414]:


D1.pivot_table(values = 'raised_amount_usd',index = ['main_sector'], aggfunc = {'sum','count'})
print(D1.groupby('main_sector')['raised_amount_usd'].count().sort_values(ascending=False))
print(D1.groupby('main_sector')['raised_amount_usd'].sum().sort_values(ascending=False))


# In[415]:


D2.pivot_table(values = 'raised_amount_usd',index = ['main_sector'], aggfunc = {'sum','count'})
print(D2.groupby('main_sector')['raised_amount_usd'].count().sort_values(ascending=False))
print(D2.groupby('main_sector')['raised_amount_usd'].sum().sort_values(ascending=False))


# In[416]:


D3.pivot_table(values = 'raised_amount_usd',index = ['main_sector'], aggfunc = {'sum','count'})
print(D3.groupby('main_sector')['raised_amount_usd'].count().sort_values(ascending=False))
print(D3.groupby('main_sector')['raised_amount_usd'].sum().sort_values(ascending=False))


# In[417]:


print(D1[D1.main_sector == 'Cleantech / Semiconductors' ].groupby('company_permalink')['raised_amount_usd'].count().sort_values(ascending=False).head(2))
print(D2[D2.main_sector == 'Cleantech / Semiconductors' ].groupby('company_permalink')['raised_amount_usd'].count().sort_values(ascending=False).head(2))
print(D2[D2.main_sector == 'Others' ].groupby('company_permalink')['raised_amount_usd'].count().sort_values(ascending=False).head(2))


# In[418]:


print(D1[D1.main_sector == 'Others' ].groupby('company_permalink')['raised_amount_usd'].count().sort_values(ascending=False).head(5))
print(D2[D2.main_sector == 'Others' ].groupby('company_permalink')['raised_amount_usd'].count().sort_values(ascending=False).head(5))
print(D2[D2.main_sector == 'Social, Finance, Analytics, Advertising' ].groupby('company_permalink')['raised_amount_usd'].count().sort_values(ascending=False).head(5))


# In[419]:


import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns
#A plot showing the fraction of total investments (globally) in venture, seed, and private equity, and 
#the average amount of investment in each funding type. This chart should make it clear that a certain funding type (FT) 
#is best suited for Spark Funds.
sns.set(style="whitegrid")
ax  = sns.boxplot(x='funding_round_type', y='raised_amount_usd', data=master_frame)
plt.yscale('log')
plt.show()


# In[420]:


#A plot showing the top 9 countries against the total amount of investments of funding type FT. 
#This should make the top 3 countries (Country 1, Country 2, and Country 3) very clear.
top3 = top9[top9.country_code.isin(['USA','GBR','IND'])]
plt.figure(figsize=(20, 10))
plt.subplot(1, 2, 1)
sns.barplot(x='country_code',y='raised_amount_usd' , data=top3)
plt.title("Count")
plt.subplot(1, 2, 2)
sns.barplot(x="country_code", y='raised_amount_usd', data=top3, estimator=sum)
plt.title("Sum")
plt.yscale('log')
plt.show()


# In[421]:


'''3.A plot showing the number of investments in the top 3 sectors of the top 3 countries 
on one chart (for the chosen investment type FT). '''
data_frames = [D1, D2, D3]
top_sectors = pd.concat(data_frames)
plt.figure(figsize=(30, 20))
sns.barplot(x='main_sector', y='raised_amount_usd', hue="country_code", data=top_sectors, estimator=np.sum)
plt.show()


# In[ ]:





# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:52:30 2020

@author: msingh31
"""

import seaborn as sns
df = sns.load_dataset('tips')
df.head()
df.corr()
sns.heatmap(df.corr())

sns.jointplot(x='tip',y='total_bill',data=df, kind='hex')
sns.jointplot(x='tip',y='total_bill',data=df, kind='reg')

sns.pairplot(data=df)
sns.pairplot(data=df,hue='sex')

sns.distplot(df['tip'])
sns.distplot(df['tip'], kde=False,bins=10)

sns.countplot('sex',data=df)
sns.countplot(y='time',data=df)

sns.barplot(y='total_bill',x='smoker',data=df)
sns.barplot(x='total_bill',y='sex',data=df)

sns.boxplot('sex','total_bill',data=df)
sns.boxplot(data=df,orient='v')
sns.boxplot(x='total_bill',y='day',hue='smoker',data=df)

sns.violinplot(x='total_bill',y='day',data=df,palette='rainbow')





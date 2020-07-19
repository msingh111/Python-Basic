# Panda 
import pandas as pd
df1 = pd.read_csv('Practice.csv')
df1.shape
rows, col = df1.shape
print('# of row:',rows)
print('# of Columns:',col)

#Panda head and tail function
df1.tail()      
df1.head()      
df1.head(2)      
df1.tail(2)      
      
# Slicing in panda
df1[2:5]

#printing column in panda
df1.columns
df1.Event
df1['Event']

#printing multiple columns
df1[['Event','Wind']]

#Fetching data based on condition
df1.Temp.max()
df1.Temp.mean()
df1.Temp.min()
df1.describe()

df1[df1.Temp>=28]
df1[[df1.Temp==df1.Temp.max()]
df1[['Event','Temp']][df1.Temp==df1.Temp.max()]


#Setting index
df1.set_index('Date',inplace = True)
df1
df1.loc['14-May-20']

df1.reset_index(inplace = True)
df1



#Reading and writing CSV and Excel
data = pd.read_csv('New.csv')
data

#skipping header
data = pd.read_csv('New.csv',skiprows=1)
data

#or
data = pd.read_csv('New.csv',header=1)
data

data = pd.read_csv('New.csv',header=None, names=['Trickers','EPS','Revenue','Price','People'],skiprows=2)
data

#Readig number of rows including Header
data = pd.read_csv('New.csv',header=1,nrows=3)
data


#Replacing values to NAN: Clinging up massy data
data = pd.read_csv('New.csv',header=1, na_values=['Not available','n.a.'])

data = pd.read_csv('New.csv',header=1, na_values={
        'EPS':['Not available','n.a.'],
        'Revenue':['Not available','n.a.',-1],
        'Price':['Not available','n.a.',-1]
        })

data.to_csv('Stock_data.csv',index=False)
data.to_csv('Stock_data.csv',index=False,columns=['Trickers','EPS'],header=False)



#Reading Excel file
data1 = pd.read_excel('Stock.xlsx','New')
data1

def covert_People(cell):
    if cell=='n.a.':
        return 'Sam Walton'
    return cell

data1 = pd.read_excel('Stock.xlsx','New',converters={
            'People':covert_People
        })
data1


#Writing back to excel file
data1.to_excel('New.xlsx',sheet_name = 'Stock',startrow=1, startcol=2)



#Dealing with missing data
data = pd.read_csv('Practice.csv',parse_dates=['Date'])
#type(data.Date[0])
data.set_index('Date',inplace=True)

#replacing NAN with other value
new_data = data.fillna(0)
new_data

new_data = data.fillna({
        'Event':'No Event',
        'Temp':0,
        'Wind':0
        })

new_data = data.fillna(method='ffill')
new_data = data.fillna(method='bfill')
new_data = data.fillna(method='ffill',limit=1)
new_data


#interpolating data
new_dat = data.interpolate()
new_dat = data.interpolate(method='time')
new_dat

#droping NAN
new_data = data.dropna()
new_data = data.dropna(how='all')
new_data = data.dropna(thresh=1)
new_data


#inseting missing data
dt = pd.date_range('05-09-2020','05-19-2020')
#type(dt)
idx = pd.DatetimeIndex(dt)
data.reindex(dt)



#Panda replace
new_dt = data1.replace([-1,'n.a.'],0)
new_dt

#panda group by
import pandas as pd
df1 = pd.read_csv('Wether_by_city.csv')
g = df1.groupby('City')

for city, city_g in g:
    print(city)
    print(city_g)
    print()


g.get_group('New York')

#Describe function
g.max()
g.describe().transpose()
g.get_group('New York').max()

import matplotlib
g.plot()















































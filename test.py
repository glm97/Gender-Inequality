import numpy as np
import pandas as pd

base=pd.read_csv('adult.csv')


print('Age', (base['age']=='?').sum())
print('Workclass',(base['workclass']=='?').sum())
print('Education',(base['education']=='?').sum())
print('Education num',(base['education.num']=='?').sum())
print('Marital Status',(base['marital.status']=='?').sum())
print('Occupation',(base['occupation']=='?').sum())
print('Relationship',(base['relationship']=='?').sum())
print('Race', (base['race']=='?').sum())
print('Sex',(base['sex']=='?').sum())
print('Capital gain', (base['capital.gain']=='?').sum())
print('Capital loss', (base['capital.loss']=='?').sum())
print('Hours per week',(base['hours.per.week']=='?').sum())
print('Native country', (base['native.country']=='?').sum())
print('Income',(base['income']=='?').sum())

female = 0
male = 0
age = 0
##for index, row in base.iterrows():
##    if (row['workclass'] == '?') & (row['sex'] == 'Female'):
##        female += 1
##    if(row['workclass'] == '?') & (row['sex'] == 'Male'):
##        male += 1
##    if(row['workclass'] == '?') & (row['age'] > 50):
##        age += 1



##print ('Man', male)
##print ('Woman', female)
##print ('Age', age)
base1 = base[base['native.country'] == '?']
print(base1)

print(base.shape)

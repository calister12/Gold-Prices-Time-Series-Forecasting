import pandas as pd
import numpy as np
df=pd.read_csv('Daily Prices Preprocessed.csv')
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10=[],[],[],[],[],[],[],[],[],[]
nx1,nx2,nx3,nx4,nx5,nx6,nx7,nx8,nx9,nx10=[],[],[],[],[],[],[],[],[],[]
x11,x12,x13,x14,x15,x16,x17,x18,x19,date=[],[],[],[],[],[],[],[],[],[]
nx11,nx12,nx13,nx14,nx15,nx16,nx17,nx18,nx19=[],[],[],[],[],[],[],[],[]

def removeComma(s):
    s=s.replace(",","")
    return s

#Extracting date from the database:
for i in df['Date']:
    i=i.replace("-","/")
    date.append(i)

#Extracting USD from the database:

for i in df['USD']:
    try:
        x1.append(round(float(i),5))
    except:
        pass

#Extracting EUR from the database:

for i in df['EUR']:
    try:
        x2.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in JPY:

for i in df['JPY']:
    try:
        x3.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in GBP:

for i in df['GBP']:
    try:
        x4.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in CAD:

for i in df['CAD']:
    try:
        x5.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in CHF:

for i in df['CHF']:
    try:
        x6.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in INR:

for i in df['INR']:
    try:
        x7.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in CNY:

for i in df['CNY']:
    try:
        x8.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in TRY:

for i in df['TRY']:
    try:
        x9.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in SAR:

for i in df['SAR']:
    try:
        x10.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in IDR:

for i in df['IDR']:
    try:
        x11.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in AED:

for i in df['AED']:
    try:
        x12.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in THB:

for i in df['THB']:
    try:
        x13.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in VND:

for i in df['VND']:
    try:
        x14.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in EGP:
x15=[]
for i in df['EGP']:
    try:
        x15.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in KRW:

for i in df['KRW']:
    try:
        x16.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in RUB:

for i in df['RUB']:
    try:
        x17.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in ZAR:

for i in df['ZAR']:
    try:
        x18.append(round(float(i),5))
    except:
        pass

#Filling Values with mean in AUD:

for i in df['AUD']:
    try:
        x19.append(round(float(i),5))
    except:
        pass

#Normalizing Features:
x1mean,x2mean,x3mean,x4mean,x5mean,x6mean,x7mean,x8mean,x9mean,x10mean=np.mean(x1),np.mean(x2),np.mean(x3),np.mean(x4),np.mean(x5),np.mean(x6),np.mean(x7),np.mean(x8),np.mean(x9),np.mean(x10)
x1sd,x2sd,x3sd,x4sd,x5sd,x6sd,x7sd,x8sd,x9sd,x10sd=np.std(x1),np.std(x2),np.std(x3),np.std(x4),np.std(x5),np.std(x6),np.std(x7),np.std(x8),np.std(x9),np.std(x10)
x11mean,x12mean,x13mean,x14mean,x15mean,x16mean,x17mean,x18mean,x19mean=np.mean(x11),np.mean(x12),np.mean(x13),np.mean(x14),np.mean(x15),np.mean(x16),np.mean(x17),np.mean(x18),np.mean(x19)
x11sd,x12sd,x13sd,x14sd,x15sd,x16sd,x17sd,x18sd,x19sd=np.std(x11),np.std(x12),np.std(x13),np.std(x14),np.std(x15),np.std(x16),np.std(x17),np.std(x18),np.std(x19)
for i in x1:
  nx1.append(round(((i-x1mean)/x1sd),5))
for i in x2:
  nx2.append(round(((i-x2mean)/x2sd),5))
for i in x3:
  nx3.append(round(((i-x3mean)/x3sd),5))
for i in x4:
  nx4.append(round(((i-x4mean)/x4sd),5))
for i in x5:
  nx5.append(round(((i-x5mean)/x5sd),5))
for i in x6:
  nx6.append(round(((i-x6mean)/x6sd),5))
for i in x7:
  nx7.append(round(((i-x7mean)/x7sd),5))
for i in x8:
  nx8.append(round(((i-x8mean)/x8sd),5))
for i in x9:
  nx9.append(round(((i-x9mean)/x9sd),5))
for i in x10:
  nx10.append(round(((i-x10mean)/x10sd),5))
for i in x11:
  nx11.append(round(((i-x11mean)/x11sd),5))
for i in x12:
  nx12.append(round(((i-x12mean)/x12sd),5))
for i in x13:
  nx13.append(round(((i-x13mean)/x13sd),5))
for i in x14:
  nx14.append(round(((i-x14mean)/x14sd),5))
for i in x15:
  nx15.append(round(((i-x15mean)/x15sd),5))
for i in x16:
  nx16.append(round(((i-x16mean)/x16sd),5))
for i in x17:
  nx17.append(round(((i-x17mean)/x17sd),5))
for i in x18:
  nx18.append(round(((i-x18mean)/x18sd),5))
for i in x19:
  nx19.append(round(((i-x19mean)/x19sd),5))

'''print('Z-Score Normalization!!')
print(int(np.mean(nx1)),(np.std(nx1)))
print(int(np.mean(nx2)),(np.std(nx2)))
print(int(np.mean(nx3)),(np.std(nx3)))
print(int(np.mean(nx4)),(np.std(nx4)))
print(int(np.mean(nx5)),(np.std(nx5)))
print(int(np.mean(nx6)),(np.std(nx6)))
print(int(np.mean(nx7)),(np.std(nx7)))
print(int(np.mean(nx8)),(np.std(nx8)))
print(int(np.mean(nx9)),(np.std(nx9)))
print(int(np.mean(nx10)),(np.std(nx10)))
print(int(np.mean(nx11)),(np.std(nx11)))
print(int(np.mean(nx12)),(np.std(nx12)))
print(int(np.mean(nx13)),(np.std(nx13)))
print(int(np.mean(nx14)),(np.std(nx14)))
print(int(np.mean(nx15)),(np.std(nx15)))
print(int(np.mean(nx16)),(np.std(nx16)))
print(int(np.mean(nx17)),(np.std(nx17)))
print(int(np.mean(nx18)),(np.std(nx18)))
print(int(np.mean(nx19)),(np.std(nx19)))'''

#Creating the final Database:

data={
    'Date':date,
    'USD':nx1,
    'EUR':nx2,
    'JPY':nx3,
    'GBP':nx4,
    'CAD':nx5,
    'CHF':nx6,
    'INR':nx7,
    'CNY':nx8,
    'TRY':nx9,
    'SAR':nx10,
    'IDR':nx11,
    'AED':nx12,
    'THB':nx13,
    'VND':nx14,
    'EGP':nx15,
    'KRW':nx16,
    'RUB':nx17,
    'ZAR':nx18,
    'AUD':nx19
    }
df=pd.DataFrame(data)
df.to_csv('Daily Prices Normalized.csv',index=False)
print("You can check the final output file in Daily Prices Normalized.csv!!")


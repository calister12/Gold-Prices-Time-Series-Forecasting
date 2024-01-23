import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt
df=pd.read_csv('Daily Prices.csv')
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10=[],[],[],[],[],[],[],[],[],[]
x11,x12,x13,x14,x15,x16,x17,x18,x19,date=[],[],[],[],[],[],[],[],[],[]

def removeComma(s):
    s=s.replace(",","")
    return s

#Extracting date from the database:
for i in df['Date']:
    i=i.replace("-","/")
    date.append(i)
#Filling Values with mean in USD:

for i in df['USD']:
    try:
        i=removeComma(i)
        float(i)
        x1.append(float(i))
    except:
        pass
mean_price=np.mean(x1)
x1=[]
for i in df['USD']:
    try:
        i=removeComma(i)
        float(i)
        x1.append(float(i))
    except:
        x1.append(mean_price)

#Filling Values with mean in EUR:
        
for i in df['EUR']:
    try:
        i=removeComma(i)
        float(i)
        x2.append(float(i))
    except:
        pass
mean_price=np.mean(x2)
x2=[]
for i in df['EUR']:
    try:
        i=removeComma(i)
        float(i)
        x2.append(float(i))
    except:
        x2.append(mean_price)

#Filling Values with mean in JPY:

for i in df['JPY']:
    try:
        i=removeComma(i)
        float(i)
        x3.append(float(i))
    except:
        pass
mean_price=np.mean(x3)
x3=[]
for i in df['JPY']:
    try:
        i=removeComma(i)
        float(i)
        x3.append(float(i))
    except:
        x3.append(mean_price)

#Filling Values with mean in GBP:

for i in df['GBP']:
    try:
        i=removeComma(i)
        float(i)
        x4.append(float(i))
    except:
        pass
mean_price=np.mean(x4)
x4=[]
for i in df['GBP']:
    try:
        i=removeComma(i)
        float(i)
        x4.append(float(i))
    except:
        x4.append(mean_price)

#Filling Values with mean in CAD:

for i in df['CAD']:
    try:
        i=removeComma(i)
        float(i)
        x5.append(float(i))
    except:
        pass
mean_price=np.mean(x5)
x5=[]
for i in df['CAD']:
    try:
        i=removeComma(i)
        float(i)
        x5.append(float(i))
    except:
        x5.append(mean_price)

#Filling Values with mean in CHF:

for i in df['CHF']:
    try:
        i=removeComma(i)
        float(i)
        x6.append(float(i))
    except:
        pass
mean_price=np.mean(x6)
x6=[]
for i in df['CHF']:
    try:
        i=removeComma(i)
        float(i)
        x6.append(float(i))
    except:
        x6.append(mean_price)

#Filling Values with mean in INR:

for i in df['INR']:
    try:
        i=removeComma(i)
        float(i)
        x7.append(float(i))
    except:
        pass
mean_price=np.mean(x7)
x7=[]
for i in df['INR']:
    try:
        i=removeComma(i)
        float(i)
        x7.append(float(i))
    except:
        x7.append(mean_price)

#Filling Values with mean in CNY:

for i in df['CNY']:
    try:
        i=removeComma(i)
        float(i)
        x8.append(float(i))
    except:
        pass
mean_price=np.mean(x8)
x8=[]
for i in df['CNY']:
    try:
        i=removeComma(i)
        float(i)
        x8.append(float(i))
    except:
        x8.append(mean_price)

#Filling Values with mean in TRY:

for i in df['TRY']:
    try:
        i=removeComma(i)
        float(i)
        x9.append(float(i))
    except:
        pass
mean_price=np.mean(x9)
x9=[]
for i in df['TRY']:
    try:
        i=removeComma(i)
        float(i)
        x9.append(float(i))
    except:
        x9.append(mean_price)

#Filling Values with mean in SAR:

for i in df['SAR']:
    try:
        i=removeComma(i)
        float(i)
        x10.append(float(i))
    except:
        pass
mean_price=np.mean(x10)
x10=[]
for i in df['SAR']:
    try:
        i=removeComma(i)
        float(i)
        x10.append(float(i))
    except:
        x10.append(mean_price)

#Filling Values with mean in IDR:

for i in df['IDR']:
    try:
        i=removeComma(i)
        float(i)
        x11.append(float(i))
    except:
        pass
mean_price=np.mean(x11)
x11=[]
for i in df['IDR']:
    try:
        i=removeComma(i)
        float(i)
        x11.append(float(i))
    except:
        x11.append(mean_price)

#Filling Values with mean in AED:

for i in df['AED']:
    try:
        i=removeComma(i)
        float(i)
        x12.append(float(i))
    except:
        pass
mean_price=np.mean(x12)
x12=[]
for i in df['AED']:
    try:
        i=removeComma(i)
        float(i)
        x12.append(float(i))
    except:
        x12.append(mean_price)

#Filling Values with mean in THB:

for i in df['THB']:
    try:
        i=removeComma(i)
        float(i)
        x13.append(float(i))
    except:
        pass
mean_price=np.mean(x13)
x13=[]
for i in df['THB']:
    try:
        i=removeComma(i)
        float(i)
        x13.append(float(i))
    except:
        x13.append(mean_price)

#Filling Values with mean in VND:

for i in df['VND']:
    try:
        i=removeComma(i)
        float(i)
        x14.append(float(i))
    except:
        pass
mean_price=np.mean(x14)
x14=[]
for i in df['VND']:
    try:
        i=removeComma(i)
        float(i)
        x14.append(float(i))
    except:
        x14.append(mean_price)

#Filling Values with mean in EGP:
x15=[]
for i in df['EGP']:
    try:
        i=removeComma(i)
        float(i)
        x15.append(float(i))
    except:
        pass
mean_price=np.mean(x15)
x15=[]
for i in df['EGP']:
    try:
        i=removeComma(i)
        float(i)
        x15.append(float(i))
    except:
        x15.append(mean_price)

#Filling Values with mean in KRW:

for i in df['KRW']:
    try:
        i=removeComma(i)
        float(i)
        x16.append(float(i))
    except:
        pass
mean_price=np.mean(x16)
x16=[]
for i in df['KRW']:
    try:
        i=removeComma(i)
        float(i)
        x16.append(float(i))
    except:
        x16.append(mean_price)

#Filling Values with mean in RUB:

for i in df['RUB']:
    try:
        i=removeComma(i)
        float(i)
        x17.append(float(i))
    except:
        pass
mean_price=np.mean(x17)
x17=[]
for i in df['RUB']:
    try:
        i=removeComma(i)
        float(i)
        x17.append(float(i))
    except:
        x17.append(mean_price)

#Filling Values with mean in ZAR:

for i in df['ZAR']:
    try:
        i=removeComma(i)
        float(i)
        x18.append(float(i))
    except:
        pass
mean_price=np.mean(x18)
x18=[]
for i in df['ZAR']:
    try:
        i=removeComma(i)
        float(i)
        x18.append(float(i))
    except:
        x18.append(mean_price)

#Filling Values with mean in AUD:

for i in df['AUD']:
    try:
        i=removeComma(i)
        float(i)
        x19.append(float(i))
    except:
        pass
mean_price=np.mean(x19)
x19=[]
for i in df['AUD']:
    try:
        i=removeComma(i)
        float(i)
        x19.append(float(i))
    except:
        x19.append(mean_price)

#Creating the final Database:

data={
    'Date':date,
    'USD':x1,
    'EUR':x2,
    'JPY':x3,
    'GBP':x4,
    'CAD':x5,
    'CHF':x6,
    'INR':x7,
    'CNY':x8,
    'TRY':x9,
    'SAR':x10,
    'IDR':x11,
    'AED':x12,
    'THB':x13,
    'VND':x14,
    'EGP':x15,
    'KRW':x16,
    'RUB':x17,
    'ZAR':x18,
    'AUD':x19
    }
df=pd.DataFrame(data)
df.to_csv('Daily Prices Preprocessed.csv',index=False)
print("You can check the final output file in output.csv!!")

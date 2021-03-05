import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sc
df= pd.read_csv('https://raw.githubusercontent.com/lev925/ECG/main/ecg.csv',header=None,names=["Signal"])
ndf=pd.read_csv('https://raw.githubusercontent.com/lev925/ECG/main/OrigEcg.csv',header=None,names=["Signal"])
dis=df["Signal"][0]
df["Signal"]=df["Signal"][1::1]
df = df[df['Signal'].notna()]
ndf["Signal"]=ndf["Signal"][1::1]
ndf = ndf[ndf['Signal'].notna()]
x=[i*dis for i in range(len(df))]
col=2000
single=df["Signal"][0:775]
plt.plot(x[0:col],df["Signal"][0:col])
print(df)

N=500
def moving_average(x, w):
  avg=[]
  it=0
  while it+w<len(x):
    avg.append(x[it:it+w].sum()/w)
    it+=1
  return avg
ma=moving_average(np.array(df["Signal"]),N)

print(len(ma))
plt.plot(x[0:col],ma[0:col])
plt.plot(x[0:col],df["Signal"][N//2:col+N//2])

def moving_med(x, w):
  armed=[]
  index=w//2
  it=0
  while it+w<len(x):
    if w%2:
      armed.append(sorted(x[it:it+w])[index])
    else:
      armed.append(sum(sorted(x[it:it+w])[index-1:index+1])/2)
    it+=1
  return armed
mm=moving_med(np.array(df["Signal"]),N)
plt.plot(x[0:col],mm[0:col])
plt.plot(x[0:col],df["Signal"][N//2:col+N//2])

df['Signal'] = df['Signal'][N//2:len(df)-N//2]
df=df.dropna()
ndf['Signal'] = ndf['Signal'][N//2:len(ndf)-N//2]
ndf=ndf.dropna()
x=[i*dis for i in range(len(df))]
print(len(x),len(df))

plt.plot(x[0:col],mm[0:col])
plt.plot(x[0:col],ma[0:col])

plt.plot(x,df["Signal"])

plt.plot(x[0:len(mm)],df["Signal"][0:len(mm)]-mm)

plt.plot(x[0:len(ma)],df["Signal"][0:len(ma)]-ma)

ma=df["Signal"]-ma
mm=df["Signal"]-mm

srez=10000


plt.plot(x[0:srez],ma[0:srez])
plt.plot(x[0:srez],mm[0:srez])
plt.plot(x[0:srez],ndf["Signal"][0:srez])

#df=df.reset_index()

def pogresh(d,y):
  if (len(d)!=len(y)):
    return "error"
  else:
    sum=0
    for i in range(N//2+1,len(d)-N//2+1):
      sum+=(d[i]-y[i])**2
    sum=sum/len(d)
    return sqrt(sum)
print(pogresh(ndf["Signal"][0:len(mm)],mm))
print(pogresh(df["Signal"][0:len(mm)],mm))


from sklearn.metrics import mean_squared_error
from math import sqrt
rms1 =mean_squared_error(ndf["Signal"][0:len(mm)],mm)
rms2 =mean_squared_error(ndf["Signal"][0:len(ma)],ma)
print(rms1,rms2)

from scipy import interpolate
print(df)
#mm=pd.Series(data=mm)
#df["Signal"]=df["Signal"][150:len(mm)+150]-mm
def f(z):
    tck = interpolate.splrep(x,df["Signal"])
    return interpolate.splev(z, tck)
print(df["Signal"][150:len(mm)+150]-mm)

# Petrol-Price-Prediction
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

delhipetrol = list()
datepetrol = list()
kolkattapetrol = list()
chennaipetrol = list()
mumbaipetrol = list()
avgpetrol = list()
avgdiesel = list()
delhidiesel = list()
kolkattadiesel = list()
mumbaidiesel = list()
chennaidiesel = list()

f=open('petrodiesel.csv','r')
line=f.readlines()
for i in range(2,32):
    a=float(line[i].split(',')[1])
    b=float(line[i].split(',')[2])
    c=float(line[i].split(',')[3])
    d=float(line[i].split(',')[4])
    av=(a+b+c+d)/4
    avgpetrol.append(av)
    
#print(avgpetrol)
#print("the length:  ",len(avgpetrol))
for i in range(39,69):
    a = float(line[i].split(',')[1])
    b = float(line[i].split(',')[2])
    c = float(line[i].split(',')[3])
    d = float(line[i].split(',')[4])
    av = (a+b+c+d)/4
    avgdiesel.append(av)
#print("\n")
#print(avgdiesel) mn 
#print('the length:  ',len(avgdiesel))
slope,intercept,r_vslopealue,p_value,std_err = stats.linregress(avgpetrol,avgdiesel)
for i in range(2,32):
    delhipetrol.append(float(line[i].split(',')[1]))
    kolkattapetrol.append(float(line[i].split(',')[2]))
    mumbaipetrol.append(float(line[i].split(',')[3]))
    chennaipetrol.append(float(line[i].split(',')[4]))

for i in range(39,69):
    delhidiesel.append(float(line[i].split(',')[1]))
    kolkattadiesel.append(float(line[i].split(',')[2]))
    mumbaidiesel.append(float(line[i].split(',')[3]))
    chennaidiesel.append(float(line[i].split(',')[4]))

for i in range(2,32):
    a = int(line[i].split(',')[0])
    datepetrol.append(a)
datepetrol.sort()
datepetrol.reverse()

fig = plt.figure()
legend = ["Delhi","Mumbai","Chennai","Kolkatta"]

#ax1 = fig.add_subplot(221)
plt.plot(datepetrol,delhipetrol)
#plt.xlabel('month')
#plt.ylabel('petrolprices')
#plt.title('delhi')
#plt.show()

#ax2 = fig.add_subplot(222)
plt.plot(datepetrol,mumbaipetrol)
#plt.xlabel('month')
#plt.ylabel('petrolprices')
#plt.title('mumbai')
#plt.show()
#print(datepetrol)
#ax3 = fig.add_subplot(223)
plt.plot(datepetrol,chennaipetrol)
#plt.xlabel('month')
#plt.ylabel('petrolprices')
#plt.title('chennai')
#plt.show()

#ax4 = fig.add_subplot(224)
plt. plot(datepetrol,kolkattapetrol)
plt.xlabel('month')
plt.legend(legend)
plt.ylabel('petrolprices')
#plt.title('kolkatta')
plt.show()
#plt4.plot(datepetrol,kolkattapetrol)
#plt4.xlabel('month')
#plt4.ylabel('petrolprices')

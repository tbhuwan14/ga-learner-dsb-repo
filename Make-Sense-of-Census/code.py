# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path, delimiter=",", skip_header=1)
#print(data)

census=np.append(data,new_record,axis=0)
print(census)



# --------------
import numpy as np
#age=np.empty((1,50))
lst=[]
for i in range(0,1001):
    b=census[i,0]
    lst.append(b)
#np.append(age,np.array(lst))
age=np.array(lst,dtype=int)
print(age)

max_age=max(age)
print(max_age)
min_age=min(age)
print(min_age)
age_mean=age.mean()
print(age_mean)
age_std=np.std(age)
print(age_std)


# --------------
#Code starts here
lst=[]
for i in range(0,1001):
    b=census[i,2]
    lst.append(b)
#np.append(age,np.array(lst))
race=np.array(lst,dtype=int)
print(race)
#print(len(race))

lst_0=[]
lst_1=[]
lst_2=[]
lst_3=[]
lst_4=[]
for i in race:
    if i==0:
        lst_0.append(i)
    elif i==1:
        lst_1.append(i)
    elif i==2:
        lst_2.append(i)
    elif i==3:
        lst_3.append(i)
    elif i==4:
        lst_4.append(i)
'''race_0=np.array(lst_0,dtype=int)
race_1=np.array(lst_1,dtype=int)
race_2=np.array(lst_2,dtype=int)
race_3=np.array(lst_3,dtype=int)
race_4=np.array(lst_4,dtype=int)'''
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
print(race_0)

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
print(len_0)
print(len_1)
print(len_2)
print(len_3)
print(len_4)


minority_race=0
if len_0<len_1 and len_0<len_2 and len_0<len_3 and len_0<len_4:
    minority_race=0
elif len_1<len_2 and len_1<len_3 and len_1<len_4:
    minority_race=1
elif len_2<len_3 and len_2<len_4:
    minority_race=2
elif len_3<len_4:
    minority_race=3
else:
    minority_race=4

print(minority_race)


# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
#print(senior_citizens)

lst=[]
for i in range(0,len(senior_citizens)):
    b=senior_citizens[i,6]
    lst.append(b)
#np.append(age,np.array(lst))
working_hours_sum=sum(np.array(lst,dtype=int))
print(working_hours_sum)

senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
print(high,low)

lst=[]
for i in range(0,len(high)):
    b=high[i,7]
    lst.append(b)
avg_high=np.array(lst,dtype=int)
#print(avg_high)
avg_pay_high=avg_high.mean()
print(avg_pay_high)

lst1=[]
for j in range(0,len(low)):
    a=low[j,7]
    lst1.append(a)
avg_low=np.array(lst1,dtype=int)
#print(avg_low)
avg_pay_low=avg_low.mean()
print(avg_pay_low)



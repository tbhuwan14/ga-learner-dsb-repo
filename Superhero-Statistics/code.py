# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data=pd.read_csv(path)
data['Gender'].replace('-', 'Agender',inplace=True)
gender_count=data['Gender'].value_counts()
print(gender_count)
gender_count.plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('No of Persons')
plt.title('Graph of Gender')
plt.legend()
plt.show()
#Code starts here 




# --------------
#Code starts here
alignment=data['Alignment'].value_counts()
print(alignment)
plt.pie(alignment,explode=(0.05,0.05,0.05))
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here
sc_df=data[['Strength','Combat']]
sc_covariance=sc_df.cov().iloc[0,1]
sc_strength=sc_df['Strength'].std()
sc_combat=sc_df['Combat'].std()
sc_pearson=sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)

ic_df=data[['Intelligence','Combat']]
ic_covariance=ic_df.cov().iloc[0,1]
ic_intelligence=ic_df['Intelligence'].std()
ic_combat=ic_df['Combat'].std()
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)


# --------------
#Code starts here
total_high=data['Total'].quantile(q=0.99)
super_best=data[data['Total']>total_high]
super_best_names=super_best['Name'].values.tolist()
print(super_best_names)


# --------------
#Code starts here
#Superhero Statistics
fig, (ax_1, ax_2, ax_3)=plt.subplots(1,3,figsize=(20,10))
ax_1.boxplot(data['Intelligence'])
plt.title('Intelligence')

ax_2.boxplot(data['Speed'])
plt.title('Speed')

ax_3.boxplot(data['Power'])
plt.title('Power')
plt.show()



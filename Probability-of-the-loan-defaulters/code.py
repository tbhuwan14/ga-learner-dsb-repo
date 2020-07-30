# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
p_a=len(df[df['fico']>700])/len(df)
print(p_a)
p_b=len(df[df['purpose']=='debt_consolidation'])/len(df)
print(p_b)

df0=df[df['purpose']=='debt_consolidation']
df1=pd.DataFrame(df0['purpose'])
#print(df1)

p_a_b=(len(df[(df['fico']>700) & (df['purpose']=='debt_consolidation')])/len(df))/p_b
print(p_a_b)

p_b_a=(len(df[(df['fico']>700) & (df['purpose']=='debt_consolidation')])/len(df))/p_a
print(p_b_a)

result=p_b_a==p_a
print(result)
# code ends here


# --------------
# code starts here
prob_lp=len(df[df['paid.back.loan']=='Yes'])/len(df)
print('p(A): ',prob_lp)

prob_cs=len(df[df['credit.policy']=='Yes'])/len(df)
print('p(B): ',prob_cs)

new_df=df[df['paid.back.loan']=='Yes']
#print(new_df)

prob_pd_cs=len(df[(df['paid.back.loan']=='Yes') & (df['credit.policy']=='Yes')])/len(df)/prob_lp
print('p(B|A): ',prob_pd_cs)

bayes=(prob_pd_cs*prob_lp)/prob_cs
print('P(A∣B): ',bayes)

# code ends here


# --------------
# code starts here
res=df.groupby(df['purpose']).size()
#print(res)
res.plot(kind='bar')
plt.show()

df1=df[df['paid.back.loan']=='No']
res1=df1.groupby(df['purpose']).size()
#print(res1)
res1.plot(kind='bar')
plt.show()


# code ends here


# --------------
# code starts here
inst_median=df['installment'].median()
print(inst_median)

inst_mean=df['installment'].mean()
print(inst_mean)

df.hist(column='installment')
plt.show()

df.hist(column='log.annual.inc')
plt.show()
# code ends here



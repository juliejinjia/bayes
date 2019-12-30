'''
学习笔记：
贝叶斯
事情A发生的情况下，推测可能导致事件A发生的各条件的概率。

单次贝叶斯的计算逻辑：
   各条件下，事件A发生的概率，进行归一化后，则为A发生的情况下，各条件可能导致的概率。
'''

from thinkbayes  import Pmf

pmf = Pmf()
#曲奇饼问题
#1.设置先验概率
pmf.Set('Bowl1',0.5)
pmf.Set('Bowl2',0.5)
print('***************')
print('Bowl1:'+str(pmf.Prob('Bowl1')))
print('Bowl2:'+str(pmf.Prob('Bowl2')))
#2.设置似然度
pmf.Mult('Bowl1',0.75) #香菜来自1碗的概率。碗1中香草曲奇饼的出现概率75%；选中1碗且是香草曲奇饼的概率0.375。
pmf.Mult('Bowl2',0.5) #香草饼干来自2碗的概率。碗2中香草曲奇饼的出现概率25%；选中2碗且是香草曲奇饼的概率0.25。
print('***************')
print('Bowl1:'+str(pmf.Prob('Bowl1')))
print('Bowl2:'+str(pmf.Prob('Bowl2')))
#3.初始化
pmf.Normalize()

print('***************')
print('Bowl1:'+str(pmf.Prob('Bowl1')))#拿出来了一个香草曲奇饼，来自碗1的概率0.375/0.625
print('Bowl2:'+str(pmf.Prob('Bowl2')))
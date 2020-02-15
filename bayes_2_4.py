# coding:utf-8
'''
Monty问题：
    A, B, C门后有奖品，选中其中一个后，主持人会随机打开一扇没有奖品的门之后，另两扇门有奖品的概率各式多少。
    先验概率：A:1/3  B:1/3  C:1/3
    各假设条件下，主持人打开B的概率
    P(B|HA) = 1/2
    P(B|HB) = 0
    P(B|HC) = 0

    P(HA) * P(B|HA) = 1/6  = p(B) * P(A|HB)
'''

from thinkbayes import Pmf

# 以hypos为参数，批量初始化先验概率
class Monty(Pmf):
    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo,1)
        self.Normalize()

    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()


    def Likelihood(self, data, hypo):
        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1

def main():
    hypos = 'ABC'
    pmf = Monty(hypos)
    data = 'c'
    pmf.Update(data)
    for hypo, prob in pmf.Items():
        print('hypo:' + str(hypo), 'prob:' + str(prob))


if __name__ == '__main__':
    main()

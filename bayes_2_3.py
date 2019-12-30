'''
事件A反复发生后（取出不放回），可能是条件X导致的概率。
'''

from thinkbayes import Pmf

# 以hypos为参数，批量初始化先验概率
class Cookie(Pmf):
    # 初始化数据

    mixes = {'Bowl1': dict(vanilla=0.75, chocolate=0.25),
             'Bowl2': dict(vanilla=0.5, chocolate=0.5)}
    # 初始化
    def __init__(self,hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo,1)
        self.Normalize()

    # 以data为参数，获取似然度并进行批量修正
    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    # 单独获取似然度
    def Likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        like = mix[data]
        return like


def main():
    hypos = ['Bowl1', 'Bowl2']
    pmf = Cookie(hypos)

    datasets = ['vanilla','vanilla','chocolate']
    for data in datasets:
        print(data)

        pmf.Update('vanilla')
        for hypo, prob in pmf.Items():
            print('hypo:' + str(hypo), 'prob:' + str(prob))


if __name__ == '__main__':
    main()
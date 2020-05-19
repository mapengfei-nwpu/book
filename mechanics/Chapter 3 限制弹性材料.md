# Chapter 3 限制弹性材料

## 1.3 不可压性

不可压材料的形变梯度满足以下性质：
$$
J \equiv \operatorname{det} \mathbf{F} \equiv \operatorname{det} \mathbf{U} \equiv \lambda_{1} \lambda_{2} \lambda_{3}=1
$$
应力张量替换为以下方程：
$$
\sigma_{i}=\lambda_{i} \frac{\partial W}{\partial \lambda_{i}}-p
$$
其中，$p$为任意标量，$p$被称为拉格朗日乘子，由于不可压条件，有没有$p$的结果都是一样的。新的应变能函数可以表示成
$$
W(\mathbf{F})-p(\operatorname{det} \mathbf{F}-1)
$$
名义应力张量可以表示成
$$
\mathbf{S}=\frac{\partial W}{\partial \mathbf{F}}-p \mathbf{F}^{-1}
$$
柯西应力张量可以表示成
$$
\boldsymbol{\sigma}=\mathbf{F} \frac{\partial W}{\partial \mathbf{F}}-p \mathbf{I}
$$
$$p$$可以被解释成是静液压。


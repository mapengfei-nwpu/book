# Chapter 2 应力与形变的关系

（各向同性材料）

超弹性材料的定义：在$B_r$中单位体积储存的能量为$W(F)$，并且满足
$$
\frac{\partial}{\partial t} W(\mathbf{F})=J \operatorname{tr}(\sigma \mathbf{L})
$$
$$W(\mathbf{F})$$也被称为应变能或者势能。因此有

$$
J \sigma=\mathbf{F} \frac{\partial W}{\partial \mathbf{F}}
$$
使用Nanson公式，在参考状态下的单元表面牵引力可写成
$$
\mathbf{t} d a=\boldsymbol{\sigma} \mathbf{n} d a=J \boldsymbol{\sigma} \mathbf{F}^{-T} \mathbf{N} d A \equiv \mathbf{S}^{T} \mathbf{N} d A
$$
其中，应力张量$S$可以定义为
$$
\mathbf{S}=J \mathbf{F}^{-1} \boldsymbol{\sigma}
$$
$S$通常不是对称的，但是从$mathbf{\sigma}$的对称性可以知道，它和形变梯度满足
$$
\mathbf{F S}=\mathbf{S}^{T} \mathbf{F}^{T}
$$
因为$mathbf{W}$仅跟$mathbf{F}$有关，我们可以得到
$$
\frac{\partial}{\partial t} W(\mathbf{F})=\frac{\partial W}{\partial F_{i j}} \frac{\partial F_{i j}}{\partial t} \equiv \operatorname{tr}\left(\frac{\partial W}{\partial \mathbf{F}} \dot{\mathbf{F}}\right)
$$
$$\partial W / \partial \mathbf{F}$$是一个二阶张量，它的成员满足
$$
\left(\frac{\partial W}{\partial \mathbf{F}}\right)_{j i}=\frac{\partial W}{\partial F_{i j}}
$$
跳过一些，得到
$$
J \sigma=\mathbf{F} \frac{\partial W}{\partial \mathbf{F}}
$$
**柯西应力张量 $\mathbf{\sigma}$**
**名义应力 $S$**
**第一PK应力张量 $\mathbf{P}=\mathbf{S}^T$**  参考状态下度量单位体积的力
**第二PK应力张量**  $$\mathbf{S} \mathbf{F}^{-T}=J \mathbf{F}^{-1} \boldsymbol{\sigma} \mathbf{F}^{-T} \equiv \mathbf{T}^{(2)}​$$

我们可以把应变能函数认为是一些不变量的函数。

## 2.3 无限制的材料

## 2.4 基于不变量的应力-形变关系
$$
\begin{aligned}
I_{1} &=\operatorname{tr}(\mathbf{B}) \equiv \lambda_{1}^{2}+\lambda_{2}^{2}+\lambda_{3}^{2} \\
I_{2} &=\frac{1}{2}\left[I_{1}^{2}-\operatorname{tr}\left(\mathbf{B}^{2}\right)\right] \equiv \lambda_{2}^{2} \lambda_{3}^{2}+\lambda_{3}^{2} \lambda_{1}^{2}+\lambda_{1}^{2} \lambda_{2}^{2} \\
I_{3} &=\operatorname{det} \mathbf{B} \equiv \lambda_{1}^{2} \lambda_{2}^{2} \lambda_{3}^{2} \equiv J^{2}
\end{aligned}
$$


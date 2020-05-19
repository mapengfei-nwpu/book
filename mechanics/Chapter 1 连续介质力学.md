# 1.1 运动学

**定义 1.1 **令$\mathrm{B}_{r}$和 $\mathrm{B}_{t}$分别是$\mathcal{B}$的参考状态和实时状态，$\mathbf{X}$和$\mathbf{x}$则是相应的坐标。存在一个双射使得
$$
\mathbf{x}=\boldsymbol{\chi}(\mathbf{X}, t) \quad \text { 对任意的 } \mathbf{X} \in \mathbf{B}_{r}, t \in I  \text{成立}
\tag{1.1.1}
$$
**刚体运动** ：
$$
\mathbf{x} \equiv \boldsymbol{\chi}(\mathbf{X}, t)=\mathbf{c}(t)+\mathbf{Q}(t) \mathbf{X}
$$
上面的$$\mathbf{c}(t)$$是一个向量，$$\mathbf{Q}(t)$$是一个适当的正交CT(2)。

**材料导数**（也可以看成是随体导数，拉格朗日坐标系中的导数） ：
$$
\frac{\partial}{\partial t} \Phi(\mathbf{X}, t) \equiv \dot{\phi} \equiv \frac{D \phi}{D t}=\frac{\partial}{\partial t} \phi+\mathbf{v} \cdot \nabla \phi
$$
比如：对于加速度$$\mathbf{a}=\dot{\mathbf{v}}$$，有 ：
$$
\mathbf{a}=\dot{\mathbf{v}}=\frac{\partial \mathbf{v}}{\partial t}+(\mathbf{v} \cdot \nabla) \mathbf{v}
$$
**梯度算子** 令$$\phi, \mathbf{u}, \mathbf{T}$$分别是关于$$X$$的标量，向量，张量函数。如果把$\left\{\mathbf{e}_{i}\right\}$作为它们的基，那么 grad 或 $\nabla$ 梯度算子的定义如下：
$$
\begin{array}{c}
\operatorname{grad} \phi \equiv \nabla \phi=\frac{\partial \phi}{\partial x_{i}} \mathbf{e}_{i} \\
\operatorname{grad} \mathbf{u} \equiv \nabla \otimes \mathbf{u}=\frac{\partial u_{p}}{\partial x_{q}} \mathbf{e}_{p} \otimes \mathbf{e}_{q} \\
\operatorname{grad} \mathbf{T} \equiv \nabla \otimes \mathbf{T}=\frac{\partial T_{p q}}{\partial x_{i}} \mathbf{e}_{p} \otimes \mathbf{e}_{q} \otimes \mathbf{e}_{i}
\end{array}
$$
**参考状态的算子** Grad, Div, Curl 分别表示参考坐标系中的算子。

**形变梯度** 
$$
\mathbf{F}(\mathbf{X}, t)=\operatorname{Grad} \mathbf{x} \equiv \operatorname{Grad} \chi(\mathbf{X}, t)
$$
**$\mathrm{B}_{t}$ 和$\mathrm{B}_{r}$的几何度量** 

长度：
$$
d \mathbf{x}=\mathbf{F} d \mathbf{X}
$$
面积（Nanson公式）：
$$
\begin{array}{c}
\mathbf{n} d a=J \mathbf{F}^{-T} \mathbf{N} d A \\
J=\operatorname{det} \mathbf{F}
\end{array}
$$
体积：
$$
d v=J d V
$$
**移动物体的算子转换**
$$
\operatorname{Grad} \phi=\mathbf{F}^{T} \operatorname{grad} \phi, \quad \operatorname{Grad} \mathbf{u}=(\operatorname{grad} \mathbf{u}) \mathbf{F}
\tag{1.1.5}
$$

$$
\operatorname{Div} \mathbf{u}=J \operatorname{div}\left(J^{-1} \mathbf{F u}\right), \quad \operatorname{Div} \mathbf{T}=J \operatorname{div}\left(J^{-1} \mathbf{F} \mathbf{T}\right)
\tag{1.1.6}
$$

**谱表示**  一个对称正定矩阵可以用一组单位正交向量表示。

**平方根定理**  一个对称正定的矩阵可以表示为两个相同的矩阵相乘。

## 1.1.1 拉伸、拉伸、剪切和应变



$\mathbf{M}$和$\mathbf{m}$分别是沿着$d \mathbf{X}$和$d \mathbf{x}$的单位向量，因此$d \mathbf{X}=\mathbf{M}|d \mathbf{X}|, d \mathbf{x}=\mathbf{m}|d \mathbf{x}|​$ ，进一步地，我们能得到拉伸关系

$$
\frac{|d \mathbf{x}|}{|d \mathbf{X}|}=|\mathbf{F} \mathbf{M}|=\left[\mathbf{M} \cdot\left(\mathbf{F}^{T} \mathbf{F} \mathbf{M}\right)\right]^{1 / 2} \equiv \lambda(\mathbf{M})
$$

角度$\Theta$和$\theta$分别表示形变前和形变后地夹角*，那么有如下公式：
$$
\cos \Theta=\mathbf{M}_{1} \cdot \mathbf{M}_{2}, \quad \cos \theta=\frac{\mathbf{M}_{1} \cdot\left(\mathbf{F}^{T} \mathbf{F} \mathbf{M}_{2}\right)}{\lambda\left(\mathbf{M}_{1}\right) \lambda\left(\mathbf{M}_{2}\right)}
$$

**剪切形变**  $\Theta-\theta$

**旋转**   当$d \mathbf{X} \cdot\left(\mathbf{F}^{T} \mathbf{F}-\mathbf{I}\right) d \mathbf{X}=0​$或者$\lambda(\mathbf{M})=1​$时只有旋转形变，记为$R​$

**应变** 用于线单元的局部变化，因此张量$\mathbf{F}^{T} \mathbf{F}-\mathbf{I}$是应变的一种度量。

**格林应变张量**   $\mathbf{E}=\frac{1}{2}\left(\mathbf{F}^{T} \mathbf{F}-\mathbf{I}\right)$

**左柯西格林应变张量**   $\mathbf{C}=\mathbf{F}^{T} \mathbf{F}=\mathbf{U}^{2}$

**右柯西格林应变张量**    $\mathbf{B}=\mathbf{F} \mathbf{F}^{T}=\mathbf{V}^{2}$

**主拉伸 $\lambda$**   
$U$和$V$分别可以在参考状态和实时状态的主方向上分解出主拉伸长度
$$
\mathbf{U}=\sum_{i=1}^{3} \lambda_{i} \mathbf{u}^{(i)} \otimes \mathbf{u}^{(i)}
$$
$$
\mathbf{V}=\sum_{i=1}^{3} \lambda_{i} \mathbf{v}^{(i)} \otimes \mathbf{v}^{(i)}
$$
主拉伸可以分别通过求解以下方程得到：
$$
\begin{aligned}
&\operatorname{det}\left(\mathbf{U}^{2}-\lambda^{2} \mathbf{I}\right)=0\\
&\operatorname{det}\left(\mathbf{V}^{2}-\lambda^{2} \mathbf{I}\right)=0
\end{aligned}
$$
**位移梯度**   
$$
\mathbf{u}=\mathbf{x}-\mathbf{X}
$$
$$
\mathbf{F}=\operatorname{Grad} \mathbf{x}=\mathbf{I}+\operatorname{Grad} \mathbf{u}
$$

# 1.2 均匀形变

均匀形变是指每一点的形变梯度都相同，最通用的形式是：
$$
x=F X+c
$$


# 1.3 运动分析

**速度的梯度**：
$$
\begin{aligned}
&\mathbf{L}=\operatorname{grad} \mathbf{v}\\
&L_{i j}=\frac{\partial v_{i}}{\partial x_{j}}
\end{aligned}
$$
利用参考状态和实时状态关系，我们可以得到下面的公式
$$
\text { Grad } \mathbf{v}=(\operatorname{grad} \mathbf{v}) \mathbf{F}=\mathbf{L} \mathbf{F}
$$
速度又可以写成$$\mathbf{v}=\dot{\mathbf{x}}$$，那么上式等价于
$$
\operatorname{Grad} \dot{\mathbf{x}}=\frac{\partial}{\partial t} \operatorname{Grad} \mathbf{x}=\dot{\mathbf{F}}
$$
其中，变量头上的一点表示随体导数。
紧接着，我们可以得到
$$
\dot{\mathbf{F}}=\mathbf{L} \mathbf{F}
$$
再利用
对于一个各向同性的运动，

本构方程和响应函数

$$
\boldsymbol{\sigma}=\mathbf{g}(\mathbf{F})
$$

张量的三个不变量用于表达本构关系，实际上T将会用F带入。
$$
\begin{array}{l}
I_{1}=\operatorname{tr}(\mathbf{T}) \equiv \lambda_{1}+\lambda_{2}+\lambda_{3} \\
I_{2}=\frac{1}{2}\left[I_{1}^{2}-\operatorname{tr}\left(\mathbf{T}^{2}\right)\right] \equiv \lambda_{2} \lambda_{3}+\lambda_{3} \lambda_{1}+\lambda_{1} \lambda_{2} \\
I_{3}=\operatorname{det} \mathbf{T} \equiv \lambda_{1} \lambda_{2} \lambda_{3}
\end{array}
$$

对称张量函数


CT(2) 是什么？
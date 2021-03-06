# IBM的介绍和有限元逼近

> PPT 作者：Lucia Gastaldi  合作者：Daniele Boffi, Luca Heltai, Nicola Cavallini, Pavia

#### 基本术语

codimension ：余维数，固体比流体少的维数，这里只介绍余维数为0的情况。

virtual work principle：虚功原理，把强形式转换成弱形式

#### 基本符号

![1589899910690.png](https://upload-images.jianshu.io/upload_images/13486212-e9d713f22d123c79.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 1. 动量守恒方程

在整个区域$$\Omega$$都满足下面的公式

$$
\rho \dot{\mathbf{u}}=\rho\left(\frac{\partial \mathbf{u}}{\partial t}+\mathbf{u} \cdot \nabla \mathbf{u}\right)=\nabla \cdot \sigma \quad \text { in } \Omega
$$

其中，方程右端的柯西应力张量可以写成

$$
\sigma=\left\{\begin{array}{ll}
\sigma_{f} & \text { in } \Omega \backslash B_{t} \\
\sigma_{f}+\sigma_{s} & \text { in } \mathcal{B}_{t}
\end{array}\right.
$$

#### 2. 虚功原理

假设固体和流体的密度相同，在动量方程两端乘上任意函数$$\mathbf{v}$$，再在整个区域上进行积分，再进行一次分部积分，可以得到

$$
\begin{array}{l}
\rho_{t} \int_{\Omega} \dot{\mathbf{u}} \cdot \mathbf{v} d \mathbf{x}=-\int_{\Omega} \sigma: \nabla \mathbf{v} d \mathbf{x}+\int_{\partial \Omega} \sigma \mathbf{n} \cdot \mathbf{v} d a 
\end{array}
$$

再将柯西应力张量代入，

$$
\begin{array}{l}
\rho_{t} \int_{\Omega} \dot{\mathbf{u}} \cdot \mathbf{v} d \mathbf{x}+\int_{\Omega} \sigma_{f}: \nabla \mathbf{v} d \mathbf{x}-\int_{\partial \Omega} \sigma_{f} \mathbf{n} \cdot \mathbf{v} d a \\
=-\int_{\mathcal{B}_{t}} \sigma_{s}: \nabla \mathbf{v} d \mathbf{x}, \quad \forall \mathbf{v}
\end{array}
$$

其中第一PK应力张量为：

$$
\tilde{\mathbb{P}}(s, t)=|\mathbb{F}(s, t)|\sigma_s(\mathbf{X}(s, t), t) \mathbb{F}^{-T}(s, t), \quad s \in \mathcal{B}
$$
进而做变量代换  $$x=\mathbf{X}(s,t)$$，可以得到：（这一步有两个地方需要注意的，$$\nabla$$变成了$$\nabla_s$$，$$d\mathbf{x}$$变成了$$ds$$，然后才有这样的等式）
$$
\int_{\mathcal{B}_{t}} \sigma_{s}: \nabla \mathbf{v} d \mathbf{x}= \int_{B} \tilde{\mathbb{P}}: \nabla_{s} \mathbf{v}(\mathbf{X}(s, t)) d s
$$
然后再做一次分部积分，得到面上的应力积分和体积上的应力积分

$$
\int_{B} \tilde{\mathbb{P}}: \nabla_{s} \mathbf{v}(\mathbf{X}(s, t)) d s
=
\int_{\mathcal{B}}\left(\nabla_{s} \cdot \tilde{\mathbb{P}}\right) \cdot \mathbf{v}(\mathbf{X}(s, t)) d s
-
\int_{\partial B} \tilde{\mathbb{P}} \mathbf{N} \cdot \mathbf{v}(\mathbf{X}(s, t)) d A
$$
利用delta函数做隐式变量替换（implicit change of variables），

$$
\mathbf{v}(\mathbf{X}(s, t))=\int_{\Omega} \mathbf{v}(\mathbf{x}) \delta(\mathbf{x}-\mathbf{X}(s, t)) d \mathbf{x}
$$
先替换前面这一项，然后再改变积分顺序：
$$
\int_{\mathcal{B}}\left(\nabla_{s} \cdot \tilde{\mathbb{P}}\right) \cdot \mathbf{v}(\mathbf{X}(s, t)) d s
=
\int_{\mathcal{B}}\left(\nabla_{s} \cdot \tilde{\mathbb{P}}\right) \cdot\left(\int_{\Omega} \mathbf{v}(\mathbf{x}) \delta(\mathbf{x}-\mathbf{X}(s, t)) d \mathbf{x}\right) d s\\
=
\int_{\Omega} \int_{\mathcal{B}}\left(\nabla_{s} \cdot \tilde{\mathbb{P}}\right) \delta(x-X(s, t)) d s \cdot \mathbf{v} d x
$$

对第二项可以做相同的变换，最后得到：

$$
\begin{array}{l}
 \int_{\Omega} (\rho_{t}\dot{\mathbf{u}} -\nabla\cdot\sigma_f)\cdot \mathbf{v} d \mathbf{x}
=\\
\int_{\Omega} \int_{\mathcal{B}}\left(\nabla_{s} \cdot \mathbb{P}\right) \delta(\mathbf{x}-\mathbf{X}(s, t)) d s \cdot \mathbf{v} d \mathbf{x} 
-\int_{\Omega} \int_{\partial \mathcal{B}} \tilde{\mathbb{P}} \mathbf{N} \delta(\mathbf{x}-\mathbf{X}(s, t)) d \mathbf{A} \cdot \mathbf{v} d \mathbf{x}
\end{array}
$$

因为$$\mathbf{v}$$是任意的，我们又回到强形式：

$$
\begin{array}{l}
\rho \dot{\mathbf{u}}-\nabla \cdot \boldsymbol{\sigma}_{f}=\int_{\mathcal{B}} \nabla_{s} \cdot \tilde{\mathbb{P}} \delta(\mathbf{x}-\mathbf{X}(s, t)) d s-\int_{\partial \mathcal{B}} \tilde{\mathbb{P}} \mathbf{N} \delta(\mathbf{x}-\mathbf{X}(s, t)) \mathrm{d} \mathbf{A}
\end{array}
$$

另设符号$$g$$，有
$$
g=\int_{\mathcal{B}} \nabla_{s} \cdot \tilde{\mathbb{P}} \delta(\mathbf{x}-\mathbf{X}(s, t)) d s=\int_{\mathcal{B}} G \delta(\mathbf{x}-\mathbf{X}(s, t)) d s
$$
实际中G可以通过下面的公式求出
$$
\int_{\mathcal{B}} (\nabla_{s} \cdot \tilde{\mathbb{P}}) \cdot\mathbf{v} d s=\int_{\mathcal{B}} G \mathbf{v} d s
$$

#### 3. 问题总结

原来的动量方程可以归结为以下三个方程的求解：

$$\rho \dot{\mathbf{u}}-\nabla \cdot \boldsymbol{\sigma}_{f}=g$$

$$\int_{\mathcal{B}} (\nabla_{s} \cdot \tilde{\mathbb{P}}) \cdot\mathbf{v} d s=\int_{\mathcal{B}} G \mathbf{v} d s$$

$$g=\int_{\mathcal{B}} \nabla_{s} \cdot \tilde{\mathbb{P}} \delta(\mathbf{x}-\mathbf{X}(s, t)) d s=\int_{\mathcal{B}} G \delta(\mathbf{x}-\mathbf{X}(s, t)) d s$$


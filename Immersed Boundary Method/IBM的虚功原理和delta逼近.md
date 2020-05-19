# IBM的介绍和有限元逼近

> PPT 作者：Lucia Gastaldi  合作者：Daniele Boffi, Luca Heltai, Nicola Cavallini, Pavia

#### 基本术语

codimension ：固体和流体相差的维数

virtual work principle：虚功原理，把强形式转换成弱形式

#### 基本符号



#### 1. 动量守恒方程



#### 2. 虚功原理

（我觉得这一步其实已经进行了分部积分）
$$
\begin{array}{l}
\rho_{t} \int_{\Omega} \dot{\mathbf{u}} \cdot \mathbf{v} d \mathbf{x}+\int_{\Omega} \sigma_{f}: \nabla \mathbf{v} d \mathbf{x}-\int_{\partial \Omega} \sigma_{f} \mathbf{n} \cdot \mathbf{v} d a \\
=-\int_{\mathcal{B}_{t}} \sigma_{s}: \nabla \mathbf{v} d \mathbf{x}, \quad \forall \mathbf{v}
\end{array}
$$

其中第一PK应力张量为：

$$
\tilde{\mathbb{P}}(s, t)=|\mathbb{F}(s, t)|(\mathbf{X}(s, t), t) \mathbb{F}^{-T}(s, t), \quad s \in \mathcal{B}
$$
进而做变量代换  $$x=\mathbf{X}(s,t)$$，可以得到：(这一步不太明白)
$$
\int_{\mathcal{B}_{t}} \sigma_{s}: \nabla \mathbf{v} d \mathbf{x}= \int_{B} \tilde{\mathbb{P}}: \nabla_{s} \mathbf{v}(\mathbf{X}(s, t)) d s
$$
然后再做一次分部积分，

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

# 一种IBM方法

这种IB方法不需要在固体区域求解。只需要在$\Omega_h$上建立函数空间，不需要在$B_h$上建立函数空间。结合了heltai等人的IBFE方法和Maitre等人的欧拉描述的IBLS。在整个过程中，固体网格$B_h$的作用只有两个：

1. 计算高斯点和高斯权重
2. 追踪固体的运动位置

### 1. 方程推导

在欧拉体系下，固体的力可以表示成
$$
-\int_{\mathcal{B}_{t}} \sigma_{s}: \nabla \mathbf{v} d \mathbf{x}, \quad \forall \mathbf{v}\in V
$$
其中，$V=\{\mathbf{u}\in L^2(\Omega)^d\}$ 是定义在$\Omega$上的函数空间。再根据Neo-Hookean的本构
$$
\tilde{\mathbb{P}}(s, t)=|\mathbb{F}(s, t)|\sigma_s(\mathbf{X}(s, t), t) \mathbb{F}^{-T}(s, t), \quad s \in \mathcal{B}
$$

$$
\tilde{\mathbb{P}}(s, t)=\mu_e(\mathbb{F}(s, t)-\mathbb{F}^{-T}(s,t))
$$

可以将原来的公式推导成
$$
-\int_{\mathcal{B}_{t}} \mu_e(\mathbb{FF^T-\mathbb{I}}): \nabla \mathbf{v} d \mathbf{x}, \quad \forall \mathbf{v}\in V
$$
那么，原来的动量方程可以写成
$$
\rho_{t} \int_{\Omega} \dot{\mathbf{u}} \cdot \mathbf{v} d \mathbf{x}-\int_{\Omega} \sigma_{f}: \nabla \mathbf{v} d \mathbf{x}=-\int_{\mathcal{B}_{t}} \mu_e(\mathbb{FF^T-\mathbb{I}}): \nabla \mathbf{v} d \mathbf{x}
$$

式子的左边等价于没有源项的流体的动量方程，右边可以看成源项。

### 2. 有限元离散

将$\Omega$离散成$\Omega_h$，将$B_t$离散成$B_h$，在$\Omega_h$上建立有限元空间$V_h$，$V_h$是$V$的有限维子空间，记成$\{\mathbf{v}_i\}$。然后原来的动量方程可以组装成线性系统$Ax=b$，就可以解出速度了。但是这里有个比较难处理的地方，右端的源并不容易积分，因为有两个问题：

1. $B_h$的单元和$V_h$的单元不匹配，数值积分比较复杂。
2. $\mathbb{F}$ 需要间接地计算。

**解决第一个问题**

我们将源项组装出来的向量记成 $b_s$，其中有$b_s[i]=\int_{\mathcal{B}_{t}} \mu_e(\mathbb{FF^T-\mathbb{I}}): \nabla \mathbf{v}_i d \mathbf{x}$

$B_h$可以看成是三角单元或者四边形单元的集合，记为$\{e_k\}$，那么$b_s[i]$就等价于

$$
\sum\limits_{e_k\in B_h}\int_{\mathcal{e}_{k}} \mu_e(\mathbb{FF^T-\mathbb{I}}): \nabla \mathbf{v}_i d \mathbf{x}
$$

根据$B_h$的网格结构计算出$\{e_i\}$中所有单元的高斯点和高斯权重（这里应该按$B_t$求解），记为$\{p_g\}$和$\{w_g\}$ 。那么上式等价于

$$
\sum\limits_{p_g} w_g \mu_e(\mathbb{FF^T-\mathbb{I}})(p_g): \nabla \mathbf{v}_i(p_g)
$$

实际计算中，我们要根据结构网格的特点，找到在高斯点处非零的$\mathbf{v}$ 。

**解决第二个问题**

令$X(x,t) \in V_h$，是一个$\Omega_h$上的函数，为整个区域的向后追踪坐标，表示质点$x$运动了时间t以后会到达$X$。
$$
\left\{  
             \begin{array}{**lr**}  
             X(x,t_{n+1})=X(x,t_n)+\Delta t\mathbf{u}(X(x,t_n),t_n), &  \\  
             X(x,0)=x, 
             \end{array}  
\right.
$$

我们假设固体不会运动到流体外部，因此$\mathbf{u}({X(x,t_n)})=0\quad|\quad X(x,t_n)\notin \Omega$ 。我们要知道只计算固体区域的高斯点处的$X$导数就行了。因此可以求出$\mathbb{F}=\nabla X$，$X\in B_t$。

最后$b_s$就计算出来了。


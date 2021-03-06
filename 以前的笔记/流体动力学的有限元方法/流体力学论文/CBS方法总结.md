​		特征线Galerkin方法是通过沿着特征线离散时间项，采用介值定理，系数取0.5得到的格式。基于这种格式，我们得到了CBS算法。相对普通算法来说，CBS算法多了一些稳定项，不会产生震荡，而且对压强和速度的有限元空间没有要求。CBS中使用了两个参数$\theta_1$和$\theta_2$。$\theta_1$是在离散连续性方程时得到的，$\theta_2$是离散动量方程（特征线Galerkin方法）时得到的。取不同的$\theta$可以得到不同的格式。

​		CBS有两种分裂格式，分裂A是完全将压力项移出动量方程构造出来的，书上说这种格式没有分裂B精确，但是我们推荐在稳态问题中使用第一种格式。

​		对于不可压流体，声速近似为无穷大，对于显格式，要保证格式稳定，就需要让时间步长无穷小，然而在实际的算例中，显格式也能取得较好的解。相反书上说隐格式可以算，并且公式这些可以一动不动地拿过来用，我把压强项删去，按照分裂A来算，算不出结果。我算出来的是速度和压强并不会随时间变化，始终保持着初值，稍微调整了一下（边界项），连第一步都算不下去了。论文《**FULLY EXPLICIT AND SEMI-IMPLICIT CBS PROCEDURES FOR INCOMPRESSIBLE FLOWS**》使用了分裂B，外加人工可压条件，算出了结果。



***以上都是胡说***
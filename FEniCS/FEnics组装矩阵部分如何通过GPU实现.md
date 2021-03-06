FEnics组装矩阵部分如何通过GPU实现

FFC能够编译出这样的**函数接口**：

```c++
 void tabulate_tensor(double * A,
                      const double * const * w,
                      const double * coordinate_dofs,
                      int cell_orientation,
                      std::size_t local_facet) const final override
```

这个函数能实现在**系数矩阵**在局部单元上的组装。

A：局部系数矩阵。A是一个指针。它指向一个有$M^2$个元素的数组，是个输出量。

w：已知函数的基函数权重。w是指针的指针，它可以看成是一个MxN的矩阵，其中M表示这个局部单元上非零的有限元基函数个数；N表示弱形式中已知函数的个数。（在已知的有限元空间中，一个函数可以用一个数组表示）

coordinate_dofs：坐标自由度，把单元节点(三角元有三个节点)的坐标排列程一个数组(三维情况下就是一个6维数组)。

cell_orientation：字面含义为单元的方向。在实际使用中并未出现，可以当成冗余的参数。

局部的**系数矩阵**组装完毕以后要把它放到全局的系数矩阵中，这个过程需要知道单元对应的全局自由度索引。

#### 编程实现

首先考虑输入变量的数据结构，我们先要把整体的**已知函数**，**坐标**，**自由度索引**存成三个数组。

一个单元上的坐标数量为2x3，自由度数量为M，假设我们现在要去计算第$i$个单元上的系数矩阵，那么我们要从自由度索引中取出$[Mi,Mi+M-1]$作为**局部自由度索引**，从坐标中取出$[6i,6i+5]$为**局部坐标**。最后根据**局部自由度索引**取出**已知函数的局部权重**。有了这三个变量，我们就可以将它们代入tabulate_tensor函数进行局部系数矩阵的计算。局部系数矩阵计算好以后再根据**局部自由度索引**对总的刚度矩阵进行叠加，最后得到整体的刚度矩阵。

```c++
/// 代码片段
double dofmap_All

```


### fenics中的自由度在不同处理器上的划分

有限元中的节点分为两类：

1. 有限元点，使用了多项式空间才会有这个。

2. 网格点。

网格点和有限元点可以没有任何关系，但实际中有限元点可以根据网格节点生成（我自己编程的时候）。有限元点的排列顺序和自由度的排列顺序是一样的，两者一一对应。

dofmap有两种，网格的或者网格单元。网格单元的dofmap联结了下面三者：

1. 网格单元的索引

2. 一组自由度的索引

3. 一组有限元点的索引

不知道dofmap怎么生成不要紧，但要知道它是怎么用的。fenics中的函数是存储在一个自由度向量中的，知道了dofmap怎么用的就能从自由度层面操作一个函数。自由度是这样在处理器之间分布的：

假设自由度是N维的，处理器有size个，当前处理器的秩为process，存储在在这个处理器上的局部自由度向量当然是全部自由度的一段，其范围是：

```c++
  // Compute number of items per process and remainder
  const std::int64_t n = N / size;
  const std::int64_t r = N % size;

  // Compute local range
  if (process < r)
    return {process*(n + 1), process*(n + 1) + n + 1};
  else
    return {process*n + r,  process*n + r + n};
```



   

   
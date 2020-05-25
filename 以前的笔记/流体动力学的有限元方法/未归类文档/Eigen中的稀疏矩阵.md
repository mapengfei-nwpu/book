# Eigen中的稀疏矩阵
#### 1. 包含头文件

一句话就可以包含所有跟稀疏矩阵有关的模块：`# include<Eigen/Sparse>`

#### 2. 创建稀疏矩阵

类`SparseMatrix`定义了稀疏矩阵主要的数据结构，它使用了比较常见的CSC格式，包含了四个数组：

..........还是直接上代码吧~~

```c++
SparseMatrix<double> mat(rows,cols);         // default is column major
mat.reserve(VectorXi::Constant(cols,6));
for each i,j such that v_ij != 0
  	mat.insert(i,j) = v_ij;                    
	// alternative: mat.coeffRef(i,j) += v_ij;
mat.makeCompressed();                        // optional
```



第二行是很关键的，它为矩阵的每一行保留六个非零元。reserve的参数是一个向量，向量的每个元素可以不同。这样做的好处是节约了大量的开辟、销毁内存的 时间。

第四行必须在元素（i，j）不存在的情况下使用，否则就用coeffRef(i,j)。coeffRef会先判断元素是否存在，然后再执行操作

第五行会压缩仍空余的空间，将矩阵转换成压缩存储。


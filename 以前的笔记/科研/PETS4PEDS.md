PETSC是搭建在MPI的基础上的，因此处处都是MPI的风味。

```C
#include <petsc.h>
int main(int argc, char **argv) {
    PetscErrorCode ierr;
    int 		   rank, i;
    double 		   localval, globalsum;
    PetscInitialize(&argc, &argv, NULL, "Compute e with PETSC.\n\n");
    ierr = MPI_Comm_rank(PETSC_COMM_WORLD, &rank); CHERRQ(ierr);
    localval = 1.0;
    for (i=2; i<rank+1; i++) localval /= i;
    ierr = MPI_Allreduce(&localval, &globalsum, 1,
                         MPI_DOUBLE, MPI_SUM, PETSC_COM_WORLD); CHKERRQ(ierr);
    ierr = PetscPrintf(PETSC_COMM_WORLD, "e is about %17.15f.\n"); CHKERRQ(ierr);
    ierr = PetscPrintf(PETSC_COMM_WORLD, "rank %d did %d flops.\n"); CHKERRQ(ierr);
    return PetscFinalize();
}
```

PETSc中的Vec和Mat数据类型本质上是对象。尽管C不是一门面向对象的，PETSc却是严格的面向对象的库。

```c
Mat A;
MatCreate(COMM, &A);
MatSetSizes(A,PETSC_DECIDE,PETSC_DECIDE,N,N);
MatSetFromOptions(A);
MatSetUp(A);
//填充矩阵A
MatDestroy(&A);
```

函数`MatSetFromOptions(A);`可以设定运行时参数，例如进程数。

矩阵配置和建立好了以后就可以使用了。

函数`MatSetValue()`可以设定矩阵元素，函数`MatView()`可以打印矩阵。

分布式存储向量：

```c
Vec 	x;
int 	i[4] = {0, 1, 2, 3};
double  v[4] = {11.0, 7.0, 5.0, 3.0};

VecCreate(COMM, &x);
VecSetSizes(x, PETSC_DECIDE, N);
VecSetFromOptions(x);
VecSetValues(x, 4, i, v, INSERT_VALUES);
VecAssembleyBegin(x);
VecAssembleyEnd(x);
```

`VecSetSizes(x, PETSC_DECIDE, N);`中的`PETSC_DECIDE`会让元素尽可能地分布在每个处理器中。

设定向量的元素时可能需要进程之间的通信，因为一个处理器上的向量元素可能被另外一个处理器操作。这样的通信发生在`VecAssembleyBegin(x);`和`VecAssembleyEnd(x);`之间。

矩阵的分布式存储需要更多的参数。一种常用的存储格式是并行压缩稀疏存储(parallel compressed sparse row storage)，MATMPIAIJ。按行划分，通常按向量的划分规格。

在装配矩阵时是不需要知道矩阵是怎么存储的。

```c
Mat 	A;
int 	i, j[4] = {0, 1, 2, 3};
double  aA[4][4] = {{11.0, 7.0, 5.0, 3.0},
                    {11.0, 7.0, 5.0, 3.0},
                    {11.0, 7.0, 5.0, 3.0},
                    {11.0, 7.0, 5.0, 3.0}};

MatCreate(COMM, &A);
MatSetSizes(A,PETSC_DECIDE,PETSC_DECIDE,N,N);
MatSetFromOptions(A);
MatSetUp(A);
for (i=0; i<4; i++) {
    MatSetValues(A, 1, &i, 4, j, aA[i], INSERT_VALUES);
}

MatAssemblyBegin(A, MAT_FINAL_ASSEMBLY);
MatAssemblyEnd(A, MAT_FINAL_ASSEMBLY);
```

`MatSetValues(A, 1, &i, 4, j, aA[i], INSERT_VALUES);`可以设置矩阵内一个矩形块的值。

# 矩阵可视化的方法

1. 25页最下面。
2. 28页最下面开始到29页全页。
3. 31页最下面、32页全页、33页全页。

# 方程组求解方法

1. 单进程组装矩阵并用ksp求解。30页

   现在我们知道了如何**创建**、**填充**、**组装**、**可视化**、**销毁**矩阵和向量。现在来求解线性系统：
   $$
   \begin{bmatrix}
   
        1  & 2 &  3 &  0 \\
        2  & 1 & -2 & -3 \\
        -1 & 1 &  1 &  0 \\
        0  & 1 &  1 & -1 \\
   
   \end{bmatrix}
   \begin{bmatrix}
   
        x_0 \\
        x_1 \\
        x_2 \\
        x_3 \\
   
   \end{bmatrix}
   =
   \begin{bmatrix}
   
        7 \\
        1 \\
        1 \\
        3 \\
   
   \end{bmatrix}
   $$

   这里，Kroylov方法的KSP对象被用来求解线性系统，但是求解算法只能在运行时选择。KSP对象也有**Create/SetFromOptions/Destroy**的使用顺序。

   ```c
   KSP ksp;
   KSPCreate(PETSC_COMM_WORLD, &ksp);
   KSPSetOperators(ksp, A, A);
   KSPSetFromOptions(ksp);
   VecDuplicate(b, &x);
   KSPSolve(ksp, b, x);
   VecView(x, PETSC_VIEWER_STDOUT_WORLD);
   KSPDestroy(&ksp);
   ```

   `KSPSetOperators(ksp, A, A);`使用了两次A，第一次用于定义线性系统，第二个用于预处理。运行时会指定预处理算法，从A构建一个$M^{-1}$矩阵。之所以第二个参数是A而不是M是为了方便我们在运行期制定预处理算法。

   `KSPSolve(ksp, b, x);`用于实际的方程求解。提供了线性系统的右端项，分配好空间的向量b。

   `VecDuplicate(b, &x);`不是复制向量的意思，而是分配和b一样布局的向量。`VecCopy()`才是复制向量。

2. 多进程组装对三角线性系统。34页

   1. 创建一个整数选项`PetscOptionsXXX()`，能够在运行期间控制线性系统的大小
   2. 在运行期间组装任意大小的矩阵，跨越任意个处理器。
   3. 使用`MatGetOwnershipRange()`可以让每个处理器只填充自己的存储的数据。
   4. 计算数值误差。

   ```c
   PetscOptionsBegin(PETSC_COMM_WORLD, "tri_", "options for tri", "");
   PetscOptionsInt("-m", "dimension of linear system", "tri.c", m, &m, NULL);
   PetscOptionsEnd();
   ```

   这一组命令设定了用户可以使用`-tri_m`选项设定`m`的大小。

   ```c
   MatGetOwnershipRange(A, &Istart, &Iend);
   for(i=Istart; i<Iend; i++){
       if (i == 0) {
           v[0] = 3.0; v[1] = -1.0;
           j[0] = 0;   j[1] = 1;
           MatSetValues(A, 1, &i, 2, j, INSERT_VALUES);
       } else {
           v[0] = -1.0; v[1] = 3.0; v[2] = -1.0;
           j[0] = i-1;  j[1] = i;   j[2] = i+1;
           if (i == m-1) {
               MatSetValues(A, 1, &i, 2, j, v, INSERT_VALUES);
           } else {
               MatSetValues(A, 1, &i, 3, j, v, INSERT_VALUES);
           }
       }
       xval = exp(cos(i));
       VecSetValues(xexact,1,&i,&xval,INSERT_VALUES);
   }
   MatAssemblyBegin(A, MAT_FINAL_ASSEMBLY);
   MatAssemblyEnd(A, MAT_FINAL_ASSEMBLY);
   MatMult(A, xexact, b); 	//	b = A*xexact.
   VecAXPY(x, -1.0, xexact); //  x += -1.0*xexact.
   VecNorm(x, NORM_2, &errnorm); // errnorm = ||x||_2
   ```

   `MatGetOwnershipRange(A, &Istart, &Iend);`可以告诉当前进程，哪几行数据是归它管的。

# 从文件读入矩阵

任何基于KSP的代码都可通过-ksp_view_(mat|rhs)保存最终的矩阵和右端向量。我们对章节7和10中的例子使用这个技术，从而生成两个额外的测试矩阵。一段简单的代码`c/ch2/loadsolve.c`可以从文件中加载这个线性系统，然后用KSP求解。更精确地说，它创建了一个PETSC查看器，为线性系统进行Matload()和VecLoad()操作。然后它创建出了一个KSP对象，并调用KSPsolve()。关键部分看起来是这样的：

```c
Vec  x, b;
Mat  A;
KSP  ksp;
PetscViewer fileA, fileB;

MatCreate(PETSC_COMM_WORLD, &A);
MatSetFromOptions(A);
PestscViewerBinaryOpen(PETSC_COMM_WORLD, nameA, FILE_MODE_READ, &fileA);
MatLoad(A, fileA);

MatCreate(PETSC_COMM_WORLD, &b);
MatSetFromOptions(b);
PestscViewerBinaryOpen(PETSC_COMM_WORLD, nameb, FILE_MODE_READ, &fileb);
MatLoad(b, fileb);

KSPCreate(PETSC_COMM_WORLD, &ksp);
KSPSetOperators(ksp, A, A);
KSPSetFromOptions(ksp);

VecDuplicate(b, &x);
KSPsolve(ksp,b,x);
```

在实际的代码中，对象一旦用不着了，就会被销毁。

我们的第一个例子来自于一个结构网格非线性偏微分问题，来自于第七章的最小表面方程求解器`minimal.c`。我们选取了257*257的网格，线性系统的维数变成了N=66049。为了生成这个矩阵，我们需要如下命令：

```bash
cd ../ch7/
make minimal
./minimal -snes_grid_sequence 7 -snes_fd_color \
        -ksp_view_mat binary:A.dat -ksp_view_rhs binary:b.dat
cp A.dat b.dat ../ch2/
cd ../ch2/
```

矩阵A是带状的，每一行包含了9个非零元素。A是块对称，但不是对称的。带宽约为网格大小的两倍。。。。


























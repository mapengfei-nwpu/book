> 在知道如何构造矩阵和向量后，就可以使用KSP对象进行线性方程组的求解了

# 预处理器

KSP对象是PETSC的核心，它为线性方程组的求解提供了统一的接口，不论是并行的还是串行的，迭代法或是直接法，只要线性系统是非奇异的。
$$
Ax=b
$$
不管是用直接法还是用迭代法，KSP的使用流程都是一样的。此外，还可以在运行时制定求解格式。KSP对象中包含了KSP接口和PC接口，使用者需要掌握这些接口的使用，因为它们是PETSc的核心。

### KSP的使用流程

ksp对象可以看作是线性方程组的求解环境(context)，矩阵A和右端项b，迭代格式和预处理算子都可以写进ksp里面，也就是说，所有东西都可以塞进ksp对象里待使用。

```c
KSPCreate(MPI Comm comm,KSP *ksp);
KSPSetOperators(KSP ksp,Mat Amat,Mat Pmat);
KSPSetFromOptions(KSP ksp);//从命令行赋予KSP一些参数。
KSPSetUp(KSP ksp);//这一步通常来说会被隐式调用，必须放在设定好参数以后。
KSPSolve(KSP ksp,Vec b,Vec x);//看好了，这一步就是在求解了奥
KSPGetIterationNumber(KSP ksp, PetscInt *its);//返回迭代步数
KSPDestroy(KSP *ksp);//销毁求解对象释放内存空间
```

（KSP支持matrix free方法？？？）

Amat是用来求解线性方程组的矩阵，Pmat是用来计算预处理算子的矩阵，通常情况下两者是一样的。

### KSP的进阶使用

规定预处理条件，保存日志等等额外的工作需要***显式***地调用 KSPSetUp(KSP ksp)。也可以从ksp中提取出pc对象 KSPGetPC(KSP ksp,PC *pc); 

### Krylov方法

Krolove子空间方法可以接受许多选项。首先调用下列函数设置将要被使用的方法。对于 Richardson, 

```c
 KSPSetType(KSP ksp,KSPType method); 
```

Chebyshev, and GMRES 方法，有额外的参数可以设定。

```c
KSPRichardsonSetScale(KSP ksp,PetscReal scale);
KSPChebyshevSetEigenvalues(KSP ksp,PetscReal emax,PetscReal emin);
KSPGMRESSetRestart(KSP ksp,PetscInt max_steps);
KSPGMRESSetOrthogonalization(KSP ksp,KSPGMRESClassicalGramSchmidtOrthogonalization);
KSPGMRESSetCGSRefinementType(KSP ksp,KSPGMRESCGSRefinementType type)
KSPGMRESModifiedGramSchmidtOrthogonalization();
KSPCGSetType(KSP ksp,KSPCGType KSP CG SYMMETRIC);
```

ksp通常是以零向量为初值进行迭代的，我们可以设成置其他的。

```c
KSPSetInitialGuessNonzero(KSP ksp,PetscBool flg);
```

###  KSP的预处理器

默认情况下，大部分KSP方法都默认使用左预处理算子，部分使用右算子，可以通过下面的函数手动设定：

```
KSPSetPCSide(KSP ksp,PCSide PC RIGHT);
```

使用预处理之后的残差还是真实残差。

 PCSetType(PC pc,PCType method); 

### 命令行选项

在命令行启动函数时，会传入一些参数，这些参数名和参数值会以字符串的键值对的形式储存在程序的数据库里，KSPSetFromOptions会选取-ksp开头的设置ksp。而PetscOptionsSetValue可以在程序中修改数据库中的键值对，不管原先存在的是什么，都会被覆盖。 

在fenics的C++部分，就是利用PetscOptionsSetValue函数进行修改命令的，而python部分是利用petsc4py库中的petsc4py.PETSc.OPTIONS来设置命令行参数的，并不需要在运行时设定。 


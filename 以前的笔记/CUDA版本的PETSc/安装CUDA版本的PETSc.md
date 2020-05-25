### [安装CUDA版本的PETSc](https://www.mcs.anl.gov/petsc/documentation/installation.html#CUDA)

- 需要 [CUDA](https://developer.nvidia.com/cuda-downloads),
- 如果是linux系统，要确保安装了兼容的 [NVIDIA驱动](https://developer.nvidia.com/cuda-downloads) .
- 在大多数情况下，你只需要传递配置选项 --with-cuda;
- 检查示例是否能正确使用：`config/examples/arch-ci-linux-cuda-double.py`

CUDA 版本的 PETSc 能够在 Mac OS X, Linux, Microsoft Windows 上工作。

### PETSc中使用CUDA的简单总结

- 如果使用了 `VecSetFromOptions()` ，VecType `VECSEQCUDA`, `VECMPICUDA`, 或者 `VECCUDA` 也许可以和 `VecSetType()` 或 -vec_type seqcuda, mpicuda, or cuda 一起用。
- The MatType `MATSEQAIJCUSPARSE`, `MATMPIAIJCUSPARSE`, or `MATAIJCUSPARSE` maybe used with MatSetType or -mat_type seqaijcusparse, mpiaijcusparse, or aijcusparse when `MatSetOptions()` is used.
- If you are creating the vectors and matrices with a DM, you can use -dm_vec_type cuda and -dm_mat_type aijcusparse
- 其他建议
  - It is useful to develop your code with the default vectors and then run production runs with the command line options to use the GPU since debugging on GPUs is difficult.
  - All of the Krylov methods except `KSPIBCGS` run on the GPU.
  - The only preconditioners to run directly on the GPU are `PCJACOBI`, `PCSAViennaCL`, `PCCHOWILUViennaCL`, and `PCRowScalingViennaCL`. The `PCBJACOBI` and `PCASM` are just containers, so if the subsolver runs on the GPU, they can also be considered to run on the GPU.
- Some GPU systems (for example many laptops) only run with single precision; thus, PETSc must be built with the `./configure option --with-precision=single`
- We could use your help in further developing PETSc for GPUs; see [PETSc Developers site](https://www.mcs.anl.gov/petsc/developers/index.html).
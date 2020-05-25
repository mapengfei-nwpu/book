```bash
export IBAMR_DIR=/public/home/npuheart/ibamr

# 安装boost
cd $IBAMR_DIR
tar xvfz boost_1_64_0.tar.gz
mv boost_1_64_0 boost
export BOOST_ROOT=$IBAMR_DIR/boost
mkdir $BOOST_ROOT/include
ln -s $BOOST_ROOT/boost $BOOST_ROOT/include
rm boost_1_64_0.tar.gz
```

```bash
# 安装HDF5
cd $IBAMR_DIR
mkdir hdf5
tar xvfz hdf5-1.8.12.tar.gz
cd hdf5-1.8.12
./configure \
CC=gcc \
CXX=g++ \
FC=gfortran \
F77=gfortran \
--enable-production \
--disable-debug \
--prefix=$IBAMR_DIR/hdf5
make
make check
make install
cd $IBAMR_DIR
rm hdf5-1.8.12.tar.gz
rm -r hdf5-1.8.12
```

```bash
# 安装silo
cd $IBAMR_DIR
tar xvfz silo-4.10.tar.gz
cd silo-4.10
./configure \
CC=gcc \
CXX=g++ \
FC=gfortran \
F77=gfortran \
--prefix=$IBAMR_DIR/silo \
--disable-silex

make
make install
cd $IBAMR_DIR
rm -r silo-4.10
rm silo-4.10.tar.gz
```

```bash
cd $IBAMR_DIR
tar xvfj openmpi-3.1.3.tar.bz2

cd openmpi-3.1.3
./configure \
  CC=gcc \
  CXX=g++ \
  FC=gfortran \
  F77=gfortran \
  --prefix=$IBAMR_DIR/openmpi/3.1.3 \
  --disable-mpi-cxx-seek \
  --disable-heterogeneous \
  --enable-orterun-prefix-by-default
make -j4
make -j4 check
make -j4 install

cd $IBAMR_DIR


export PATH=$IBAMR_DIR/openmpi/3.1.3/bin:$PATH
```

```bash
 #安装petsc
cd $IBAMR_DIR
tar xvfz petsc-3.10.5.tar.gz
mv petsc-3.10.5 petsc
export PETSC_DIR=$IBAMR_DIR/petsc
export PETSC_ARCH=linux-opt
cd $PETSC_DIR
./configure \
--CC=mpicc \
--CXX=mpicxx \
--FC=mpif90 \
--COPTFLAGS="-O3" \
--CXXOPTFLAGS="-O3" \
--FOPTFLAGS="-O3" \
--PETSC_ARCH=$PETSC_ARCH \
--with-debugging=0 \
--download-hypre=1 \
--download-fblaslapack=1 \
--with-x=0

make
make test                                                  
```

```bash
# 安装samrai
cd $IBAMR_DIR
tar xvfz SAMRAI-v2.4.4.tar.gz
mv SAMRAI samrai
cd samrai
# 打补丁
cp ../ibamr-samrai-fixes.patch ibamr-samrai-fixes.patch
patch -p1 < ibamr-samrai-fixes.patch
# 配置安装
./configure \
CFLAGS="-O3" \
CXXFLAGS="-O3" \
FFLAGS="-O3" \
--prefix=$IBAMR_DIR/samrai/linux-g++-opt \
--with-CC=mpicc \
--with-CXX=mpicxx \
--with-F77=mpifort \
--with-hdf5=$IBAMR_DIR/hdf5 \
--without-hypre \
--without-silo \
--without-blaslapack \
--without-cubes \
--without-eleven \
--without-kinsol \
--without-petsc \
--without-sundials \
--without-x \
--with-doxygen \
--with-dot \
--disable-debug \
--enable-opt \
--enable-implicit-template-instantiation \
--disable-deprecated
make
make install
cd $IBAMR_DIR
# rm SAMRAI-v2.4.4.tar.gz
```

```bash
cd $IBAMR_DIR
tar xvfz libmesh-1.2.1.tar.gz
mv libmesh-1.2.1 libmesh
cd $IBAMR_DIR/libmesh
mkdir objs-opt
cd objs-opt
../configure \
--prefix=$IBAMR_DIR/libmesh/1.2.1-opt \
--with-methods=opt \
PETSC_DIR=$IBAMR_DIR/petsc \
PETSC_ARCH=linux-opt \
CC=mpicc \
CXX=mpicxx \
FC=mpif90 \
F77=mpif90 \
--enable-exodus \
--enable-triangle \
--disable-boost \
--disable-openmp \
--disable-perflog \
--disable-pthreads \
--disable-strict-lgpl \
--disable-glibcxx-debugging
make
make install
cd $IBAMR_DIR
rm libmesh-1.2.1.tar.gz
```

```bash
cd $IBAMR_DIR
tar xvfz IBAMR-0.5.1.tar.gz
mv IBAMR-0.5.1 IBAMR
cd IBAMR
mkdir ibamr-objs-opt
cd ibamr-objs-opt
../configure \
CC=mpicc \
CXX=mpicxx \
F77=mpif90 \
FC=mpif90 \
MPICC=mpicc \
MPICXX=mpicxx \
CFLAGS="-O3 -Wall" \
CXXFLAGS="-O3 -Wall -std=c++11" \
FFLAGS="-O3 -Wall" \
FCFLAGS="-O3 -Wall" \
CPPFLAGS="-DOMPI_SKIP_MPICXX" \
--with-hypre=$PETSC_DIR/$PETSC_ARCH \
--with-samrai=$IBAMR_DIR/samrai \
--with-hdf5=$IBAMR_DIR/hdf5 \
--with-silo=$IBAMR_DIR/silo \
--with-boost=$IBAMR_DIR/boost \
--enable-libmesh \
--with-libmesh=$IBAMR_DIR/libmesh/1.2.1-opt \
--with-libmesh-method=opt
```

```bash
make lib
make examples
cd examples/IB/explicit/ex0
./main2d input2d
```


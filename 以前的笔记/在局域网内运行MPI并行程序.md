# 在局域网

#### 预备
1. 装好了ubuntu和mpich2
2. 在master上操作
3. 所有机器连在同一个局域网中
## 步骤一：配置hosts文件
`/etc/hosts`
## 步骤二：创建一个用户
`sudo adduser mpiuser`
## 步骤三：建立SSH连接
```
sudo apt-get install openssh-server
su - mpiuser
ssh-keygen -t dsa
ssh-copy-id -p 9999 npuheart9@10.69.30.128
```
## 步骤四：建立NFS
通过NFS共享master上的一个文件夹，client能加载这个文件夹以供数据交换。
#### NFS-Server
```bash
sudo apt-get install nfs-kernel-server
```
在`/etc/exports`建立一个入口
```bash

```
`*`：IP地址。
`rw`或者`ro`：read+write或者read only
`sync`：只有更改commited以后共享文件夹的更改才能真正发生
`no_subtree_check`：扫描父文件夹以检验权限
`no_root_squash`：允许root账户连接这个文件夹

保存`/etc/exports`中的更改，重新启动`nfs`服务器
```
exportfs -a
```

#### NFS-Client
服务器上也需要安装NFS
```bash
sudo apt-get install nfs-common
mkdir cloud
sudo mount -t nfs -p 9999 pengfei@server:/home/pengfei/cloud ~/cloud
```
检查文件夹
```
df -h
```
使挂载永久
```bash
cat /etc/fstab
#MPI CLUSTER SETUP
-p 9999 pengfei@server:/home/pengfei/cloud /home/pengfei/cloud nfs
```
## 步骤五：运行MPI程序
1. 编译
```bash
mpicc -o mpi_sample mpi_sample.c
```
2. 将可执行文件拷贝到共享文件夹内
3. 在本地运行：
```bash
mpi run -np 2 ./mpi_example
```
在集群上跑：
```bash
mpirun -np 5 -hosts client,localhost ./mpi_example
#hostsname 可以用ip地址替换
```
或者在一个文件夹内指定：
```
mpirun -np 5 --hostfile mpi_file ./cpi
```
## 常见问题
1. MPI版本需要是一样的
2. 主节点的hosts文件通常是这样的：
```bash
1.2.3.4 master
2.3.4.1 slave1
3.3.5.3 slave2
```
子节点的hosts文件是这样的：
```bash
1.2.3.4 master
2.3.4.1 slave1
```
```bash
1.2.3.4 master
3.3.5.3 slave2
```
就是说要包含自己IP和主节点IP
3. 可以本地跑，可以本地和远程一起跑，但是不能只是远程跑 


dsa

dsa

dsa















的步骤二

```

```
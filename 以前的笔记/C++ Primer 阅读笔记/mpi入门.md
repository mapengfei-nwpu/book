# MPI并行程序设计实例教程
消息处理接口：message process interface，是一个标准，不同厂商由不同版本的实现：MPICH、LAMMPI、IBM MPL
下载、解压、编译、测试。
进程管理器：MPD，用于MPI进程的创建启动和管理。
目标主机列表：`$HOME/mpd.hosts`文件中指定。
节点间无密码登陆：

通讯子（communicator）：也称为通讯器
秩（rank）：每个进程被分配的一个序号，用于显式地进行通信。
消息标签（tag）：
点对点通信（point-to-point）：
集体性通信（collective）：


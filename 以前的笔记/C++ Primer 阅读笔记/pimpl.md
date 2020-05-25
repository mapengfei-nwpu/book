pimpl: pointer to implementation.

Pimpl习惯用法。第一部分是把某类的数据成员对象换成一个指针，这个指针指向实际的对象。声明一个指针型别的数据成员，指涉到一个非完整性别，第二部分是动态分配和回收持有从前在原始类里的那些数据成员的对象，而分配和回收的代码则放在实现文件中。

比如，原来的Widget类：

```c++
class Widget {
    public:
    Widget();
    private:
    std::string name;
    std::vector<double> data;
    Gadget g1,g2,g3,g4;
}
```

包含这个类的文件中必须有string、vector、Gadget等的头文件。

1. 这些头文件增加了编译时间。
2. 如果这些文件改动了，Widget也要重新编译。

Pimpl用法：

```c++
class Widget {
    public:
    Widget();
    ~Widget();
    private:
    struct Impl;
    Impl *pImpl;
}
```

1. 提升了编译速度
2. 这些对象的改变，Widget不用重新编译，编译改动了的对象即可。

Impl已声明但未定义，是一个非完整型别，可以声明指针，但不能声明对象。

（区别：删除器、delete函数、析构函数）


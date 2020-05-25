```std::unique_ptr```

工厂函数

对象继承谱系

在堆上分配一个对象，并且返回一个指涉它的指针，由调用者（调用工厂函数的人）负责删除。

工厂函数的函数签名如下：

```c++
template<typename... Ts>
std::unique_ptr<Investment> makeInvestment(Ts&& params);
```

调用方式如下：

```
auto pInvestment = makeInvestment( arguments );
```

事实上，资源的所有权即使经过多次转交，仍然只有一个unique指针占有它，并最后析构它。如果所有权链断了，那么资源占用的内存会随着局部对象的析构而释放。

自定义析构器

```c++
auto delInvmt = [](Investment* pInvestment)
{
	makeLogEntry(pInvestment);
	delete pInvestment;
};
```

修改后的返回类型

```c++
template<typename... Ts>
std::unique_ptr(Ts&&... params)
{
    std::unique_ptr<Investment, decltype(delInvmt)> pInv(nullptr, delInvmt);
    /*if( it is stock)*/
    return pInv;
}
```

`unique_ptr`接受两个参数，一个是资源的地址，一个是自定义析构函数对象。这里是先给了空指针，然后再用`reset`方法重新分配资源。

这种做法无需为资源何时析构费心。

1. 无法将一个裸指针赋值给unique指针。

2. 自定义析构器的类型作为第二个模板参数。

3. 撰写lambda函数比普通函数方便，且效率更高。

4. 使用std::forward对传递给makeInvestment的实参实施完美转发？？？（条款25）

5. 我们自定义析构函数的参数是Investment，析构函数条用的基类的析构函数。基类必须有一个虚析构函数才能为不同的子类完成特定的析构步骤。

   ```c++
   class Investment {
       public:
       virtual ~Investment();
   }
   ```

6. unique指针的自定义析构器如果是函数指针，那么会多出一两个字节，如果是无捕获的lambda函数，那么就和裸指针一样。

这样，一个比较完备的工厂函数就写好了。

Pimpl习惯用法（条款22）

unique指针有两种形式：单个对象和数组，因此unique指针不会产生二义性，所提供的接口也有所不同。指向数组的unique指针不常用。

unique指针隐式转换为shared指针，因此工厂函数大可采用unique指针作为返回类型，不用在意实际使用者想要哪种类型的指针。

```c++
std::unique_ptr<Investment> sp = makeInvestment( arguements );
```


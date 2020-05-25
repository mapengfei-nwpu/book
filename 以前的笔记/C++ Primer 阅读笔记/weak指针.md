weak指针：有可能空悬的共享指针。本质上来说，shared指针和weak指针是一样的。

weak指针指涉的对象可能是已经析构了的，关键问题在于如何判断指针是否空悬。其实weak并不是一种独立的智能指针，只是shared指针的一种扩充罢了。weak指针一般是通过shared指针创建的：

```c++
auto spw = std::make_shared<Widget>();
std::weak_ptr(Widget) wpw(spw);
// 引用计数为零，对象被析构，wpw空悬。
spw = nullptr;
```

weak指针没有引用计数，但是能判断指针是否失效。 weak指针不能进行提领操作（类似解引用），需要通过weak指针创建shared指针才能提领。通过weak指针创建shared指针有两种操作，区别在于，如果weak指针失效，第一种操作会创建一个空shared指针，第二种操作会抛出异常。

```c++
// 第一种,用lock()函数
auto spw = wpw.lock();
// 第二种，用构造函数
std::shared_ptr<Widget> spw(wpw);
```

weak指针的有三种用处：

1. 缓存，考虑一个工厂函数：

```c++
std::shared_ptr<const Widget> fastLoadWidget(Widget id){
    static std::unordered_map<WidgetID,
    						  std::weak_ptr<const Widget>> cache;
    auto objPtr = cache[id].lock();
    if(!objPtr) // 如果对象不在缓存中，则加载并缓存。
    {
        //。。。。。
    }
    return objPtr
}
```

2. 观察者设计模式（有待学习）

让每个主题持有一个容器来放置weak指针，以便主题在使用某个指针之前，能够先确认它是否空悬。

2. 避免share指针环路

shared指针环路会导致内存泄漏。

严格的继承谱系中，子节点的生存期不会比父节点的更长，因此，即使子节点中有指向父节点的成员指针，那么因为子节点比父节点先销毁，子节点的那个指针不会变成空悬指针。但如果不是严格的继承谱系，那么就要慎重了。


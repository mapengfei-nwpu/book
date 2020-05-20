手写**Find<NAME>**模块：

```cmake
# 文件名为 FindHELLO.cmake
FIND_PATH(HELLO_INCLUDE_DIR hello.h /usr/include/hello
/usr/local/include/hello)
FIND_LIBRARY(HELLO_LIBRARY NAMES hello PATH /usr/lib
/usr/local/lib)
IF (HELLO_INCLUDE_DIR AND HELLO_LIBRARY)
	SET(HELLO_FOUND TRUE)
ENDIF (HELLO_INCLUDE_DIR AND HELLO_LIBRARY)
IF (HELLO_FOUND)
	IF (NOT HELLO_FIND_QUIETLY)
		MESSAGE(STATUS "Found Hello: ${HELLO_LIBRARY}")
	ENDIF (NOT HELLO_FIND_QUIETLY)
ELSE (HELLO_FOUND)
	IF (HELLO_FIND_REQUIRED)
		MESSAGE(FATAL_ERROR "Could not find hello library")
	ENDIF (HELLO_FIND_REQUIRED)
ENDIF (HELLO_FOUND)
```

这样使用：

```cmake
SET(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)
FIND_PACKAGE(HELLO)
FIND_PACKAGE(HELLO QUIET)
FIND_PACKAGE(HELLO REQUIRED)

```

使用了FIND_PACKAGE命令以后可以使用如下变量
• <name>_FOUND
• <name>_INCLUDE_DIR or <name>_INCLUDES
• <name>_LIBRARY or <name>_LIBRARIES



详细编译过程

make VERBOSE=1

${}引用变量

生成库、可执行文件不需要加后缀名

最好是所有变量都大写

源文件名字写全

默认有make clean命令但是没有dist clean命令

推荐使用外部构建，<projectname>_BINARY_DIR的路径会被更改

EXCLUDE_FROM_ALL不会被默认构建
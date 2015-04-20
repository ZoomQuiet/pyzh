# 简介 #

这里说的是简体繁体转换，而不仅仅是编码转换。理由很简单：GBK编码或UTF8编码中本来就是包含简体和繁体的，因此即使在同一个编码体系内也是存在简体和繁体转换的问题。

简而言之，本软件能实现不同编码体系或同一编码体系内简体到繁体的相互转换。软件基于标准的Python2.5版本，因此本质上是跨平台的。

# 使用方法 #

这个软件就是一个单独的python文件jft.py,主要调用接口是两个函数j2f(简体到繁体转换)和f2j(繁体到简体转换)：
```
def j2f(sourceEncoding,destinationEncoding,sourceString):
    '''
    Simplified Chinese character to traditional Chinese character converter
    
    Parameters:
        sourceEncoding : The encoding codec name of string to be converted
        destinationEncoding : The encoding codec name of output string
        sourceString : The string to be converted
        
    Return value:
        The output traditional Chinese character string
    '''

def f2j(sourceEncoding,destinationEncoding,sourceString):
    '''
    Traditional Chinese character to simplified Chinese character converter
    
    Parameters:
        sourceEncoding : The encoding codec name of string to be converted
        destinationEncoding : The encoding codec name of output string
        sourceString : The string to be converted
        
    Return value:
        The output simplified Chinese character string
    '''
```

假设用户的console的缺省编码是GBK，下面这个例子实现了GBK编码的简体到繁体的转换：

```
>>> import jft
>>> a='飞机飞向蓝天'
>>> b = jft.j2f('gbk','gbk',a)
飞机飞向蓝天
>>> print b
飛機飛向藍天
```

在不同编码方式间转换也是没有问题的，下面这个例子就实现从GBK编码的简体到UTF8繁体的转换：
```
>>> a='飞机飞向蓝天'
>>> b=jft.j2f('gbk','utf8',a)
飞机飞向蓝天
>>> print unicode(b,'utf8').encode('gbk')
飛機飛向藍天
>>>
```

# 局限或使用条件 #
本软件仅仅实现纯汉字字符的转换，请不要在待转换字符串中包含标点符号或非汉字字符，如果这样做了，结果是未定义的。
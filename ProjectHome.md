a set of localization tools to make python support Chinese and Chinese culture better.

Contact me (panjy at zopen dot cn) if you want to contribute.

聚合国内python人的力量，建立一整套python的中文本地化工具包。

gb18030的python-codec是韩国人帮咱们写的，这个有些汗了。自己的事情，还是应该由咱们自己来完成！

典型的是：

1. 汉字 -> 拼音 转换

2. 中英文字数统计

3. 公历 -> 阴历 转换

4. 中文分词

5. 中英文文本折行

6. 繁簡中文轉換, 支援多種編碼方式

# 架構 #

主要模塊名稱: zhutils

調用方法
```
>>> import zhutils
>>> dir(zhutils)
......
```

主要分類模塊:

> - word
> > 與文字處理, 翻譯有關模塊


> - datetime
> > 與曆法, 時間有關模塊

調用方法
```
>>> import zhutils
>>> dir(zhutils.word)
......
>>> dir(zhutils.datetime)
......
```

# 相關專案 #

**[周蟒](http://zhpy.googlecode.com): Python 中文編程工具, 繁簡中文關鍵字對應表, 咬一口 Python 電子書(中文)**


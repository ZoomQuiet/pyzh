# -*- coding: utf-8 -*-
# 作者: 潘俊勇, panjy at zopen dot cn
import re
rx=re.compile(u"([\u2e80-\uffff])", re.UNICODE)

def cjkwrap(text, width, encoding="utf8"):
     return reduce(lambda line, word, width=width: '%s%s%s' %              
                (line,
                 [' ','\n', ''][(len(line)-line.rfind('\n')-1
                       + len(word.split('\n',1)[0] ) >= width) or
                      line[-1:] == '\0' and 2],
                 word),
                rx.sub(r'\1\0 ', unicode(text,encoding)).split(' ')
            ).replace('\0', '').encode(encoding)

def test():
     msg ="""我们自己可以的，不是吗? whay 我们正的
 要求是什么、how to dothat? no problem? !! 但是中文就不同了，一个汉字的空间占用等于2个英文。汉字的分词，是没有空格的。

 借鉴CJKSplitter的开发经验，我准备也做一个中文折行算法（应该也很容易支持日韩文字），当然不可能有英文的那么高效了：
 英文是ascii，每个字符占用空间相同，直接使用空格就可以分词。因此英文版本的折行算法在python cookbook上有很经典的高效算法：

 one-liner word-wrap function"""
     return cjkwrap(msg, 50)

if __name__ == '__main__':
     print test()

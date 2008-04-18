#!/usr/bin/env python
#coding=utf-8
#
# Copyleft 2008 limodou@gmail.com
# License BSD
# Version 0.1
#
# 说明
#    本程序用来进行文本的折行处理，支持中文和英文，可以处理Unicode和普通字符串
#
# 参数说明
#    text       待处理的文本，可以是unicode或str
#    width      处理宽度
#    encoding   字符串编码，只当text不是unicode时有效
#    cr         换行符，如果为None则自动从文本中判断，自动设定为找到的第一个换
#               行符，如果找不到缺省为'\n'，如果不为None，则使用设定的换行符
#    indent     非首行缩近量
#    firstindent首行缩近量
#    skipchar   行首忽略字符，如果存在则在处理前会清除每前开始前有skipchar的文本
#
# 功能描述
#  1.支持unicode和非unicode文本，如果为非unicode文本，则会使用encoding指定的编
#    码对文本转换为unicode，在返回时，会根据原文本是unicode还是非unicode进行转
#    换并输出。
#  2.支持段落概念。两个以上连续的回车为段落分隔，其中如果一行只包括空白(空格或
#    制表符的行)将视为空行。最终的结果段落间只保存一个空行。如果只存在单个换行
#    则相邻的行视为同一段落。支持'\n', '\r\n', '\r'三种形式的换行符。可以自动
#    使用文本中的回车符或指定转换后的回车符。
#  3.自动处理亚洲文字和半角字符，自动处理空白，多个空白(包括制表符)将自动合并
#    成一个。亚洲文字和英文之间以空格分隔。对于亚洲文字中间的空白自动删除。
#  4.支持缩近设置，首行缩近和非首行缩近。缩近量可以是数值，则为空格*数值，可以
#    是字符串。如果firstindent没有设置将缺省为indent的值。
#  5.可以设置每行行首要忽略的字符，如注释行的'#'，在处理时将先删除匹配的行首字
#    符。
#
# 示例
#  msg = '''中文 中文hello, world'''
#  wraptext(msg, 10)

def wraptext(text, width=75, encoding='utf-8', cr=None, indent='', firstindent=None, skipchar=None):
    import unicodedata
    import re
    if isinstance(text, unicode):
        unicode_flag = True
    else:
        unicode_flag = False
        text = unicode(text, encoding)
        
    if not cr:
        if text.find('\r\n') > -1:
            cr = '\r\n'
        elif text.find('\r') > -1:
            cr = '\r'
        else:
            cr = '\n'
    
    if skipchar:
        text = re.sub(r'(?m)^%s' % skipchar, '', text)
        
    lines = re.split(r'\r\n|\r|\n(:\s*\r\n|\s*\r|\s*\n)+', text)
    rx = re.compile(u"[\u2e80-\uffff]+", re.UNICODE)
    
    if isinstance(indent, int):
        indent = ' ' * indent
    if firstindent is None:
        firstindent = indent
    if isinstance(firstindent, int):
        firstindent = ' ' * firstindent
    
    def _wrap(text, width, indent, firstindent):
        if not text:
            return ''
        text = text.strip()
        s = []
        pos = 0
        for i in rx.finditer(text):
            if i.start() > pos:
                s.extend(text[pos:i.start()].split())
            s.append(i.group())
            pos = i.end()
        if pos < len(text):
            s.extend(text[pos:].split())
        
        ss = [s[0]]
        #get first element character is asian char flag
        flag = unicodedata.east_asian_width(s[0][0]) != 'Na'
        for i in range(1, len(s)):
            f = unicodedata.east_asian_width(s[i][0]) != 'Na'
            if f and f == flag:
                ss[-1] = ss[-1] + s[i]
            else:
                ss.append(s[i])
            flag = f
        
        s = ss
        
        t = []
        y = 0
        buf = []
        x = 0
        while s:
            i = s.pop(0)
            if unicodedata.east_asian_width(i[0]) != 'Na':
                factor = 2
            else:
                factor = 1
                
            if x == 0:
                w = width - len(firstindent)
                step = firstindent
            else:
                w = width - len(indent)
                step = indent
            length = y + len(i)*factor + len(buf)
            if length == w:
                buf.append(i)
                t.append(step + ' '.join(buf))
                x = 1
                buf = []
                y = 0
            elif length > w:
                if factor == 2 or (factor==1 and len(i) * factor >= w):
                    buf.append(i[:(w-y-len(buf)-1)/factor])
                    t.append(step + ' '.join(buf))
                    x = 1
                    s.insert(0, i[(w-y-len(buf)-1)/2:])
                    buf = []
                    y = 0
                    continue
                else:
                    t.append(step + ' '.join(buf))
                    x = 1
                    s.insert(0, i)
                    buf = []
                    y = 0
                    continue
                    
            else:
                buf.append(i)
                y += factor * len(i)
                
        if buf:
            t.append(step + ' '.join(buf))
        return '\n'.join(t)
    
    s = []
    for line in lines:
        if not line.strip():
            s.append('')
        else:
            s.append(_wrap(line, width, indent, firstindent))
       
    text = '\n'.join(s)
    if not unicode_flag:
        text = text.encode(encoding)
    return text
        
def test():
    msg =u"""   我们自  己可以的，不是吗? whay 我们正的
 要求是什么、how to dothat? no problem? !! 但是中文就不同了，一个汉字的空间占用等于2个英文。汉字的分词，是没有空格的。

 借鉴CJKSplitter的开发经验，我准备也做一个中文折行算法（应该也很容易支持日韩文字），当然不可能有英文的那么高效了：
 英文是ascii，每个字符占用空间相同，直接使用空格就可以分词。因此英文版本的折行算法在python cookbook上有很经典的高效算法：

 one-liner word-wrap function

Hey!


#I  would like to know wheter you are aware of using the google accounts
#for your app or not, and how you think about alternatives ?
#
#
#http:/asdfl.asf.asdf.asf.asfadsfds.fads.fads.fasdf.asdf.sdf.asf.asdf.sdf.asdf.adsfa.dsf
#
#
#I'm not sure wheter I Would use my Googleaccount for an app of an
external developer - mainly beeing frightenend of that the external
developer is leading me on a "wrong" login-site an thiefing my data or
just that he is able to find out about my gmail-data..
"""
    print wraptext(msg, 60, indent='#  ', skipchar='#').encode('gbk')

if __name__ == '__main__':
#    from timeit import Timer
#    t = Timer("test()", "from __main__ import test")
#    print t.timeit(1000)
    test()
    
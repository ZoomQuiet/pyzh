#!/usr/bin/env python
#coding=utf-8

#如果要统计总的字符个数,请直接decode为unicode再用len

#UTF-8：采用变长字节 (1 ASCII, 2 希腊字母, 3 汉字, 4 平面符号)
#UTF-8字符各字节含义
#0×00-0×7F 	同ASCII，也不可能作为任何其他多字节UTF-8字符的一部分
#0xC0-0xDF 	多字节UTF-8字符的开始字节，而且据此可以判断出该UTF-8字符的长度（字节数）
#0×80-0xBF 	多字节UTF-8字符的跟随字节
#0xFE-0xFF 	UTF-8未使用

#那么如何判断UTF-8字符的长度呢？
#\x00-\x7F 	1字节
#\xC0-\xDF 	2字节
#\xE0-\xEF 	3字节
#\xF0-\xF7 	4字节
#\xF8-\xFB 	5字节
#\xFC-\xFD 	6字节

#作者:张沈鹏 2008-2-16 
#电子科大 08年7月毕业
#Email:zsp007@gmail.com

def utf8_count(word):
    """
    统计utf8字符串中文字符和非中文字符数
    >>>print utf8_count("作者:张沈鹏")
    (1,5)
    """
    cn=0
    en=0
    i=0
    length=len(word)
    while i<length:
        c=word[i]
        if c>"\xE0" and c<="\xEF":
            i+=3
            cn+=1
        else:
            en+=1
            if c<"\xC0":i+=1
            elif c<="\xDF":i+=2
            elif c<="\xF7":i+=4
            elif c<="\xFB":i+=5
            else:i+=6
    return (en,cn)

def utf8_cn_conut(word):
    return utf8_count(word)[1]

def utf8_en_conut(word):
    return utf8_count(word)[0]

_visable_width=0, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 3, 4, 7, 7, 11, 8, 2, 4, 4, 5, 7, 3, 4, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 3, 3, 7, 7, 7, 7, 12, 7, 8, 9, 9, 8, 7, 9, 9, 3, 6, 8, 7, 9, 9, 9, 8, 9, 9, 8, 7, 9, 7, 11, 7, 7, 7, 3, 3, 3, 5, 7, 4, 7, 7, 6, 7, 7, 3, 7, 7, 3, 3, 6, 3, 11, 7, 7, 7, 7, 4, 7, 3, 7, 5, 9, 5, 5, 5, 4, 3, 4, 7

def utf8_cut(word,limit,etc="..."):
    """一个中文当2个E文"""
    cn=0
    en=0
    i=0
    length=len(word)
    if length<=limit:return word
    limit = limit<<2
    width=0
    while i<length:
        c=word[i]
        if c>"\xE0" and c<="\xEF":
            offset=3
            width+=4
        else:
            if c<"\xC0":
            	offset=1
            	width+=ord
            else:
                width+=4
                if c<="\xDF":offset=2
                elif c<="\xF7":offset=4
                elif c<="\xFB":offset=5
                else:offset=6
        if width>limit:
            return word[:i]+etc
        else:
            i+=offset
    return word


if __name__=="__main__":
    print utf8_count("作者:张沈鹏")
    print utf8_count("Email:zsp007@gmail.com")
    print utf8_cn_conut("电子科大Uestc")
    print utf8_en_conut("电子科大Uestc")
    print utf8_cut("张沈鹏123456",5)
    print utf8_cut("张沈鹏123456",10)
    

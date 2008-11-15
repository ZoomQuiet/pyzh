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

def utf8_cut(word,limit,etc="..."):
    """一个中文当2个E文"""
    i=0
    length=len(word)
    if length<=limit:return word
    limit = limit<<1
    width=0
    while i<length:
        c=word[i]
        if c>"\xE0" and c<="\xEF":
            offset=3
            width+=2
        else:
            if c<"\xC0":
            	offset=1
            	width+=1
            else:
                width+=2
                if c<="\xDF":offset=2
                elif c<="\xF7":offset=4
                elif c<="\xFB":offset=5
                else:offset=6
        if width>limit:
            return word[:i]+etc
        else:
            i+=offset
    return word

_visable_width=0, 24, 24, 24, 24, 24, 24, 24, 24, 0, 0, 0, 0, 0, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 12, 12, 16, 28, 28, 44, 32, 8, 16, 16, 20, 28, 12, 16, 12, 12, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 12, 12, 28, 28, 28, 28, 48, 28, 32, 36, 36, 32, 28, 36, 36, 12, 24, 32, 28, 36, 36, 36, 32, 36, 36, 32, 28, 36, 28, 44, 28, 28, 28, 12, 12, 12, 20, 28, 16, 28, 28, 24, 28, 28, 12, 28, 28, 12, 12, 24, 12, 44, 28, 28, 28, 28, 16, 28, 12, 28, 20, 36, 20, 20, 20, 16, 12, 16, 28, 24
#中文长48

def visable_length(word):
    length=len(word)
    width=0
    i=0
    while i<length:
        c=word[i]
        if c>"\xE0" and c<="\xEF":
            i+=3
            width+=48
        else:
            if c<"\xC0":
                i+=1
                width+=_visable_width[ord(c)]
            else:
                width+=48
                if c<="\xDF":i+=2
                elif c<="\xF7":i+=4
                elif c<="\xFB":i+=5
                else:i+=6
    return width
    
def visable_cut(word,limit,etc="..."):
    i=0
    length=len(word)
    if length<=limit:return word
    limit = limit*48
    width = 0
    while i<length:
        c=word[i]
        if c>"\xE0" and c<="\xEF":
            offset=3
            width+=48
        else:
            if c<"\xC0":
            	offset=1
            	width+=_visable_width[ord(c)]
            else:
                width+=48
                if c<="\xDF":offset=2
                elif c<="\xF7":offset=4
                elif c<="\xFB":offset=5
                else:offset=6
        if width>limit:
            etc_length=(48+visable_length(etc))/48
            return word[:i-etc_length]+etc
        else:
            i+=offset
    return word



if __name__=="__main__":
    print utf8_count("作者:张沈鹏")
    print utf8_count("Email:zsp007@gmail.com")
    print utf8_cn_conut("电子科大Uestc")
    print utf8_en_conut("电子科大Uestc")
    print utf8_cut("张沈鹏123456",5).decode("utf-8")
    print utf8_cut("张沈鹏123456",10).decode("utf-8")
    print visable_cut("张沈鹏@@@",5).decode("utf-8")
    print visable_cut("张沈鹏lll",5).decode("utf-8")
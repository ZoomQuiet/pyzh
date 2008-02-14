#!/usr/bin/python
# -*- coding: utf-8 -*-
#支持中英文混合的substr函数。如果给定的数字超过字符串长度，则返回整个字符串和一个空字符串。
# Author: charles huang
# Mail: huangyy@gmail.com

class StrUtility:
    def __init__(self):
        pass
    
    def csubstr(self, long, str):
        str_tmp = []
        str_l = len(str)
        i = 0
        while (i< str_l):
            if ord(str[i]) > 0x80:
                str_tmp.append(str[i:i+2])
                i=i+2
            else:
                str_tmp.append(str[i])
                i=i+1
        str_a = ""
        str_b = ""
        if len(str_tmp) <= long:
            return str, ''
        for x in range(0,long):
            str_a = str_a + str_tmp[x]
        for j in range(x+1, len(str_tmp)):
            str_b = str_b + str_tmp[j]
        
        return str_a, str_b
    
if __name__=='__main__':
    str_ob = StrUtility()
    a, b = str_ob.csubstr(4, "123测试试")
    print a, b

#!/usr/bin/python
# -*- coding: utf-8 -*-
# 分别统计中文和英文的字数，不包括标点符号。
# Author: Pan Junyong from zopen.cn, panjy at zopen dot cn
import re
import sys
from types import StringType
import operator

# See CJKSplitter
rx = re.compile(u"[a-zA-Z0-9_\u0392-\u03c9]+|[\u4E00-\u9FFF\u3400-\u4dbf\uf900-\ufaff\u3040-\u309f\uac00-\ud7af]+", re.UNICODE)

def caculateWords(s, encoding='utf-8'):
    result = []

    if type(s) is StringType: # not unicode
        s = unicode(s, encoding, 'ignore')

    splitted = rx.findall(s)
    cjk_len = 0
    asc_len = 0
    for w in splitted:
        if ord(w[0]) >= 12352:  # \u3040
            cjk_len += len(w)
            # result.append(w)
        else:
            #result.append(w)
            asc_len += 1
    return (cjk_len, asc_len)

def main():
    index=0
    total_words = (0, 0)

    for filename in sys.argv[1:]:
        s = open(filename).read()
        # TODO: check encoding
        words = caculateWords(s)
        index += 1

        total_words = map(operator.add, total_words, words)
        print "%2d" % index, filename.ljust(18), '(Chinese, English):', words

    print "total: %2d files,     " % index, '(Chinese, English):', tuple(total_words)

def test():
    print caculateWords( 'abc+ def我们的很 好。金益康(eHR)产品')

if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] in ['-h', '--help']:
        print u"\t统计字数工具。直接接上多个文件名统计。如 zishu.py *.rst 。"
    else:
        main()

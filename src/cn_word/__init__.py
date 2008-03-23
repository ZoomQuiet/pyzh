#coding=utf-8
from cn_word import add_word,cn_word_utf8

def load_dict(txt):
    f=open(txt)
    for line in f:
        add_word(line.strip())

if __name__=='__main__':
    import time

    begin=time.time()

    load_dict("dict.txt")

    print "Load Dictionary Cost Time %ssec\n"%(time.time()-begin)

    begin=time.time()

    for i in open("test.txt"):
        print ' '.join(cn_word_utf8(i)).decode('utf-8'),


    print "\nCost Time %ssec"%(time.time()-begin)
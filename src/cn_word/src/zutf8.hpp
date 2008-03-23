#ifndef _ZUTF8_HPP_2008_3_18_0_59_ZSP007_AT_GMAIL_COM
#define _ZUTF8_HPP_2008_3_18_0_59_ZSP007_AT_GMAIL_COM
#include <mem.h>
#include <assert.h>
struct utf8_char{
    utf8_char(){
        c_[6]='\0';
    }
    utf8_char(const char* c){
        memcpy(c_,c,6*sizeof(char));
    }
    utf8_char(const utf8_char& o){
        memcpy(c_,o.c_,sizeof(c_));
    }
    ~utf8_char(){
    }
    const char* c_str(){
        return c_;
    }
private:
    char c_[7];
};
enum CharType{undefined=0,ascii,cn};

template<class Iter,class String>
void english_word(Iter& next,Iter end,String& str){
    unsigned char c;
    while(next!=end){
        c=static_cast<unsigned char>(*next);
        if(c<0x7F && c!=' '){
            str+=c;
        }else break;
        ++next;
    }
}
template<class Iter,class String>
CharType utf8_next(Iter& next,Iter end,String& str){
    int pos=0;
    int char_length=0;
    char buf[7];
    unsigned char c;
    CharType char_type=undefined;
    while(next!=end){
        c=static_cast<unsigned char>(*next++);
        
        buf[pos++]=static_cast<char>(c);
        
        //cout<<int(c)<<"  ";
        
        assert(pos<7);
        
        if(char_length==0){
            pos=1;
            /*
            1.ascii 2.希腊字母 3.汉字 4.平面符号
            #那么如何判断UTF-8字符的长度呢？
            #0x00-0x7F 	1字节
            #0xC0-0xDF 	2字节
            #0xE0-0xEF 	3字节
            #0xF0-0xF7 	4字节
            #0xF8-0xFB 	5字节
            #0xFC-0xFD 	6字节
            */
            //设置char_length
            if(c>=0xE0){
                if(c<=0xEF){
                    char_length=3;//先判断中文,提高效率
                    char_type=cn;
                }
                else if(c<=0xF7)char_length=4;
                else if(c<=0xFB)char_length=5;
                else if(c<=0xFD)char_length=6;
            }
            else if(c<=0x7F){//ascii码
                char_type=ascii;
                break;
            }
            else
                if(c>=0xC0)char_length=2;
        }else if(pos==char_length)break;
    }
    buf[pos]='\0';
    str=String(buf);
    return char_type;
}
#endif

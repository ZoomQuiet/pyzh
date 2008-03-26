#ifndef _CN_WORD_HPP_2008_3_18_12_39_ZSP007_AT_GMAIL_COM
#define _CN_WORD_HPP_2008_3_18_12_39_ZSP007_AT_GMAIL_COM
#include <map>
#include <vector>
#include <tr1/unordered_map>
#include <string>
#include <iostream>
#include "zutf8.hpp" 
template<class CnChar=std::string,class String=std::string>
class BasicCnWord{
typedef std::vector<String> v_str;
typedef std::pair<bool,v_str> BoolVstr;
typedef std::tr1::unordered_map<CnChar,BoolVstr> SecondDict;
typedef std::tr1::unordered_map<CnChar,SecondDict> Dict;
private:
    static Dict dict;
    static void add_second_word(SecondDict* second_dict,CnChar second,String more){
        SecondDict& sd=*second_dict;
        typename String::size_type len=more.length();
        bool is_word;
        if(len)is_word=false;
        else is_word=true;
        typename SecondDict::iterator i=sd.find(second);
        if(i!=sd.end()){
            BoolVstr& b=i->second;
            if(is_word)b.first=is_word;
            else{
                //由长到短
                v_str& vs=b.second;
				//TODO:比较长度排序
                typename v_str::iterator iter=vs.begin();
                while(iter!=vs.end()){
                    if(len>(*iter).length())break;
                    ++iter;
                }
                vs.insert(iter,more);
            }
        }else{
            v_str v;
            if(!is_word)v.push_back(more);
            sd[second]=make_pair(is_word,v);
        }
    }


public:
    BasicCnWord(){}
    ~BasicCnWord(){
    }
    
    
    static void add(const char* word){
        String s(word);
        typename String::iterator i=s.begin(),end=s.end();
        CnChar first,second;
        switch(utf8_next(i,end,first)){
        case ascii:
            english_word(i,end,first);
        default:
            if(dict.find(first)==dict.end()){
                dict[first]=SecondDict();
            }
            if(utf8_next(i,end,second)){
                //std::cout<<'\n'<<first<<" "<<second<<" "<<String(i,end)<<'\n';
                add_second_word(&dict[first],second,String(i,end));
            }
        }
    }

    template <typename InputIterator, typename Token>
    bool operator()(InputIterator& next,InputIterator end,Token& tok) {
        tok=Token();
        CnChar first_char,c;
        CharType char_type_first=utf8_next(next,end,first_char);
		if(char_type_first){
            tok+=first_char;
			if (char_type_first==ascii&&is_stop_word(first_char[0]))
			{
				return true;
			}
            InputIterator break_point=next;
            CharType char_type_second=utf8_next(next,end,c);
            switch(char_type_second){
                case undefined:return true;
                case ascii:
                	if(is_stop_word(c[0])){
                		next=break_point;
                		return true;
                	}
                    if(char_type_first==ascii){
                        tok+=c;
                        english_word(next,end,tok);
                        break_point=next;
                        if(!utf8_next(next,end,c))return true;
                    }
            }
            
            typename Dict::iterator i=dict.find(tok);

            if(i!=dict.end()){
                typename SecondDict::iterator j=i->second.find(c);
                if(j!=(i->second).end()){
                    BoolVstr& bv=j->second;
                    if(bv.first){
                        break_point=next;
                        tok+=c;
                    }
                    v_str& vs=bv.second;
                    int len=end-next;//TODO:iterator相减的类型
                    for(typename v_str::iterator i=vs.begin();i!=vs.end();++i){
                        //匹配更多,成功时返回
                        String& s=*i;
                        //std::cout<<"\ns = "<<s<<"\n";
						typename String::size_type s_len=s.length();
                        if(s_len<=len){
							//std::cout<<"\ns_len="<<s_len<<"\n";
                            while(s_len--){
                                if(s[s_len]!=*(next+s_len))goto next;
                            }
                            next+=s.length();
                            tok.insert(tok.end(),break_point,next);
                            return true;
                        }
                        next:continue;
                    }
                }
            }
            next=break_point;
            return true;
        }
        return false;
    }

    void reset(){}
};

template<class CnChar,class String>
typename BasicCnWord<CnChar,String>::Dict BasicCnWord<CnChar,String>::dict(6719);

typedef BasicCnWord<> CnWord;


#endif

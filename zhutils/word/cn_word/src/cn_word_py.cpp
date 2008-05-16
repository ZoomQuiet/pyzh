#include "../src/cn_word.hpp"  

#include <boost/python.hpp>
#include <boost/python/list.hpp>
#include <boost/tokenizer.hpp>

#include <string>
#include <iostream>
using std::string;
using namespace boost;
using namespace boost::python;

typedef tokenizer<CnWord> CnTokenizer;

list cn_word_utf8(const string s){
	list l;
	CnTokenizer tok(s);
	for(CnTokenizer::iterator beg=tok.begin();beg!=tok.end();++beg){
			l.append(*beg);
	}
	return l;
}

BOOST_PYTHON_MODULE(cn_word)
{
    def("add_word",&CnWord::add);
	def("cn_word_utf8",cn_word_utf8);

}

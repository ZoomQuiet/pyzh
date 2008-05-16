基于双字hash的最大正向匹配分词,只支持utf-8编码.

速度约1M/s,没有进行细致的优化.

依赖库:
Boost
TR1

毕业设计中的一小部分,没有追求准确率(呵呵,这个准确率对我的聚类算法没有什么提高)

如果想优化准确率,请改写cn_word.hpp的
bool operator()(InputIterator& next,InputIterator end,Token& tok)

如果想优化性能,可以优化一下查表,比如第二个字的hash表,根据候选字数量而动态选择数据结构等等.

此外,可以替换std::string,因为utf-8中文只是char[3]

张沈鹏 电子科大 大四
zsp007@gmail.com
http://zsp.javaeye.com
2008年3月23日 4:17:58

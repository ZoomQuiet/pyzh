# subversion的安装 #

scp root@172.16.100.205:/root/svn\_files.tar .
(密码123456)

tar xsf svn\_files.tar

cd svn\_files

rpm -i **.rpm --force**

svn checkout https://pyzh.googlecode.com/svn/trunk/ pyzh --username 您的用户名

# Introduction #

谁负责补充一下需求或者功能介绍。

# lunarSolarTerms #


> lunarSolarTerms    = {'立春':(2, 3),  '雨水':(2, 18), '惊蛰':(3, 5), '春分':(3, 20), '清明':(4,4),
> > '谷雨':(4,19),  '立夏':(5,5), '小满':(5,20), '芒种':(6,5), ' 夏至':(6,21),
> > '小暑':(7,6), ' 大暑':(7,22),  '立秋':(8,7), '处暑':(8,22), ' 白露':(9,7),
> > '秋分':(9,22), ' 寒露':10,8), ' 霜降':(10,23),' 立冬':(11,7), ' 小雪':(11,22),
> > '大雪':(12,6),' 冬至':(12,21),' 小寒':(1,5),' 大寒':(1,20)  }
# 1.有关年分信息查询 #

# Details #

输入年份,返回本年度阴历的闰月

-名字:getLeapMonthOfThisYear()

-输入:year

-输出:如果没有,就返回空,否则返回今年的闰月

输入年份,返回本年度所有节气信息(dic)

-名字:getAllSolarTermOfThisYear()

-输入:year

-输出:dict: {'节气':(year, month, day)}

输入年份,返回本年度所有节日信息(dic)

-名字:getAllFestivalOfThisYear()

-输入:year

-输出:dict: {'节日':(year, month, day)}

输入年份,节气,返回所在日期

-名字:getDateOfThisSolarTerm()

-输入:year,solarTerm

-输出:(year,month,day)

输入年份,节日,返回所在日期

-名字:getTheDateOfThisFestival()

-输入:year,festival

-输出:(year,month,day)

输入年份,返回本年度属相

-名字:getAnimalSignOfThisYear()

-输入:year

-输出:animalSign

输入年份,返回本年年号(天干地支)

-名字:getHeavenlyAndEarthlyOfThisYear()

-输入:year

-输出:heavenlyAndEarthly

输入年号(天干地支),返回本年

-名字:getHeavenlyAndEarthlyOfThisYear()

-输入:year

-输出:heavenlyAndEarthly


输入属相,返回前后分别10个此属相年份(LIST)

-名字:getYearsOfThisAnimalSign()

-输入:animalSign

-输出:list:[...,...,...]

# 2.月份相关信息查询 #

输入年份月份,返回本月天数

-名字:getDayCount()

-输入:year,month

-输出:num

输入年份月份,返回本月所有节气信息(dic)

-名字:getAllSolarTermsofThisMonth()

-输入:year,month

-输出:dict: {'节气':(year, month, day)}

输入年份月份,返回本年度所有节日信息(dic)

-名字:getAllFestivalofThisMonth()

-输入:year,month

-输出:dict: {'节日':(year, month, day)}

# 3.详细日期信息查询 #

输入阳历年月日,返回本日阴历

-名字:getLunarOfThisDay()

-输入:(year,month,day)

-输出:(year,month,day)


reference:

http://docs.python.org/lib/module-calendar.html

http://docs.python.org/lib/module-datetime.html


# Suggest Reading #

# Details #
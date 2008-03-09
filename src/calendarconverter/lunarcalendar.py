# -*- encoding: utf-8 -*-
""" CalendarConversion   公历 <-> 阴历.
"""

class LunarCalendar:

    daysInSolarMonth= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    lunarMonthDays  = [29,30] # a short (long) lunar month has 29 (30) days */

    shengXiaoEn     = ["Mouse", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
			   "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    shengXiaoGB     = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡",
			   "狗", "猪"]
    zhiGB           = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉",
			   "戌", "亥"]
    ganGB           = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]

    monthEn         = ['January', 'February', 'March', 'April', 'May', 'June',
			   'July', 'August', 'September', 'October', 'November',
			   'December']
    weekdayEn       = ["Monday", "Tuesday", "Wednesday", "Thursday",
			   "Friday", "Saturday", "Sunday"]
    weekdayGB       = ["一", "二", "三", "四", "五", "六", "日"]
    numGB           = ['○', "一", "二", "三", "四", "五", "六", "七", "八", "九",
			   "十"]
    lunarHoliday    = {'0_0':'春节', '4_4':'端午', '7_14':'中秋', '8_8':'重阳',
			   '0_14':'元宵'}

    yearCode = [
                                        0x04bd8,        # 1900
    0x04ae0, 0x0a570, 0x054d5, 0x0d260, 0x0d950,        # 1905
    0x16554, 0x056a0, 0x09ad0, 0x055d2, 0x04ae0,        # 1910
    0x0a5b6, 0x0a4d0, 0x0d250, 0x1d255, 0x0b540,        # 1915
    0x0d6a0, 0x0ada2, 0x095b0, 0x14977, 0x04970,        # 1920
    0x0a4b0, 0x0b4b5, 0x06a50, 0x06d40, 0x1ab54,        # 1925
    0x02b60, 0x09570, 0x052f2, 0x04970, 0x06566,        # 1930
    0x0d4a0, 0x0ea50, 0x06e95, 0x05ad0, 0x02b60,        # 1935
    0x186e3, 0x092e0, 0x1c8d7, 0x0c950, 0x0d4a0,        # 1940
    0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, 0x025d0,        # 1945
    0x092d0, 0x0d2b2, 0x0a950, 0x0b557, 0x06ca0,        # 1950
    0x0b550, 0x15355, 0x04da0, 0x0a5d0, 0x14573,        # 1955
    0x052d0, 0x0a9a8, 0x0e950, 0x06aa0, 0x0aea6,        # 1960
    0x0ab50, 0x04b60, 0x0aae4, 0x0a570, 0x05260,        # 1965
    0x0f263, 0x0d950, 0x05b57, 0x056a0, 0x096d0,        # 1970
    0x04dd5, 0x04ad0, 0x0a4d0, 0x0d4d4, 0x0d250,        # 1975
    0x0d558, 0x0b540, 0x0b5a0, 0x195a6, 0x095b0,        # 1980
    0x049b0, 0x0a974, 0x0a4b0, 0x0b27a, 0x06a50,        # 1985
    0x06d40, 0x0af46, 0x0ab60, 0x09570, 0x04af5,        # 1990
    0x04970, 0x064b0, 0x074a3, 0x0ea50, 0x06b58,        # 1995
    0x055c0, 0x0ab60, 0x096d5, 0x092e0, 0x0c960,        # 2000
    0x0d954, 0x0d4a0, 0x0da50, 0x07552, 0x056a0,        # 2005
    0x0abb7, 0x025d0, 0x092d0, 0x0cab5, 0x0a950,        # 2010
    0x0b4a0, 0x0baa4, 0x0ad50, 0x055d9, 0x04ba0,        # 2015
    0x0a5b0, 0x15176, 0x052b0, 0x0a930, 0x07954,        # 2020
    0x06aa0, 0x0ad50, 0x05b52, 0x04b60, 0x0a6e6,        # 2025
    0x1d0b6, 0x0d250, 0x0d520, 0x0dd45, 0x0b5a0,        # 2040
    0x056d0, 0x055b2, 0x049b0, 0x0a577, 0x0a4b0,        # 2045
    0x0aa50, 0x1b255, 0x06d20, 0x0ada0                  # 2049
    ]

    solar1st = (1900, 1, 30)   # January 31, 1900 
    lunar1st = (1900, 1, 1, 6, 0) # First day, First month, 1900, 庚/子年

    def __init__(self):
        pass

    def getLunarYearInfo(self, year):
        iYear = year - 1900
        code = self.yearCode[iYear]
        leapMonth = code&0xf #leapMonth==0 means no lunar leap month
        monthDays = [0] * 12

        code >>= 4
        for iMonth in range(12):
            monthDays[11-iMonth] = self.lunarMonthDays [code&0x1]
            code >>= 1

        if leapMonth>0:
            monthDays.insert (leapMonth-1, self.lunarMonthDays [code & 0x1])
        return monthDays, leapMonth

    # 1.有关年分信息查询

    def getLeapMonthOfThisYear(self, year):
        """ 输入年份,返回本年度阴历的闰月

        如果没有,就返回空,否则返回今年的闰月"""

    def getAllSolarTermOfThisYear(self, year):
        """输入年份,返回本年度所有节气信息(dic)

        输出:dict: {'节气':(year, month, day)}
        """

    def getAllFestivalOfThisYear(self, year):
        """ 输入年份,返回本年度所有节日信息(dic)

        输出:dict: {'节日':(year, month, day)}"""

    def getDateOfThisSolarTerm(self, year, solarTerm):
        """输入年份,节气,返回所在日期

        输出:(year,month,day)"""

    def getAnimalSignOfThisYear(self,year):
	"""输入年份,返回本年度属相

	输出:animalSign"""

    def getHeavenlyAndEarthlyOfThisYear(self,year):
	"""输入年份,返回本年年号(天干地支)

	输出:heavenlyAndEarthly"""

    def getYearOfThisHeavenlyAndEarthly(self,HandE,starYear,endYear):
	"""输入天干地支,返回指定范围内的年份

	输出:如果没有输入起始年份或截止年份的话,则返回最近的一个年份"""

 #2.月份相关信息查询	

    def getDayCount(self,year,month):
	""""输入年份月份,返回本月天数

	输出:num"""
	
    def getAllSolarTermsofThisMonth(self,year,month):
	"""份月份,返回本月所有节气信息(dic)

	输出:dict: {'节气':(year, month, day)}
	"""
    def getAllFestivalofThisMonth(self,year,month):
	"""输入年份月份,返回本年度所有节日信息(dic)
	
	输出:dict: {'节日':(year, month, day)}"""

  #3.详细日期信息查询

    def getLunarOfThisDay(self,year,month,day):
	"""输入阳历年月日,返回本日阴历

	输出:(year,month,day)
	"""

    def getSolarTermOfThisDay(self,year,month,day):
	"""输入阴历年月日,返回本日阳历信息

	输出:(year,month,day) 
	"""	

if __name__ == "__main__":
    import sys
    cal = LunarCalendar()
    print cal.getLunarYearInfo( int(sys.argv[1]) )

# -*- encoding: utf-8 -*-
""" CalendarConversion   公历 <-> 阴历.
"""

class LunarCalendar:

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






"""输入年份,节日,返回所在日期(暂时不做)

-名字:getTheDateOfThisFestival()

-输入:year,festival

-输出:(year,month,day)"""

# calendar.py [from Bernd Klein]

class Calendar(object):
    months = (31,28,31,30,31,30,31,31,30,31,30,31)

    def __init__(self, month=1, day=1, year=2016):
        self.__day = day
        self.__month = month
        self.__year = year

    def leapyear(self, y):
        if y % 4:
        # not a leap year
            return 0;
        else:
            if y % 100:
                return 1;
            else:
                if y % 400:
                    return 0
                else:
                    return 1;

    def set(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def get(self):
        return (self, self.__month, self.__day, self.__year)

    def month(self):
        return self.get()[1]

    def day(self):
        return self.get()[2]

    def year(self):
        return self.get()[3]
    
    def advance(self):
        months = Calendar.months
        max_days = months[self.__month-1]
        if self.__month == 2:
            max_days += self.leapyear(self.__year)
        if self.__day == max_days:
            self.__day = 1
            if (self.__month == 12):
                self.__month = 1
                self.__year += 1
            else:
                self.__month += 1
        else:
            self.__day += 1


    def __str__(self):
       return str(self.__month)+ "/"+ str(self.__day)+"/"+ str(self.__year)

if __name__ == "__main__":
   x = Calendar()
   print(x)
   x.advance()
   print(x)

##       ============= RESTART: /Users/wrc/Desktop/time/calendar.py ==========
##    1/1/2016
##    1/2/2016
##    >>> 

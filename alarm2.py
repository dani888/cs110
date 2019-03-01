# alarm2.py -- an alarm clock with a clock as a component field

from clock import *

import time  

class AlarmClock():
    '''A (fake) alarm clock.  We say it's fake because it "tocks"
        a minute every real second. Like Clock, this is a 24 hour clock.
    '''
    
    def __init__(self):
        t = time.localtime()[3:6]   # t = (hour,min, sec)
        self.__clock = Clock(t[0],t[1],0) # ignote seconds here
        self.nowTime()

    def __str__(self):
        return str(self.__clock)

    def hours(self):
        return self.__clock.hours()

    def minutes(self):
        return self.__clock.minutes()

    def nowTime(self):
        '''Set our time to now (EST).'''
        t = time.localtime()[3:6]   # t = (hour,min, sec)
        self.__clock.set_Clock(t[0],t[1],0) # 

    def setAlarm(self, hour, minute):
        ''' Set our alarm to an hour (0-23) and minute (0-59).'''
        if hour == self.hours() and minute == self.minutes():
            raise TypeError( "Cannot set alarm to now." )
        elif type(hour) != int or hour < 0 or hour > 23:
            raise TypeError("Hours have to be integers between 0 and 23!")
        elif type(minute) != int or minute < 0 or minute > 59:
            raise TypeError("Minutes have to be integers between 0 and 59!")
        else:
            print(self)
            print "Alarm set for", str(hour)+":"+str(minute)+":00"
            while True:
                if self.__clock.hours() == hour and \
                    self.__clock.minutes() == minute:
                    # Ring Alarm
                    print "********Alarm*********"
                    print self
                    print "********Alarm*********"
                    return
                else:
                    print self
                    time.sleep(1) # 1 second real time = 1 minute fake time.
                    self.tock()
                    
    def tick(self):
        self.__clock.tick() # delegation
        
        
    def tock(self):
        '''Advance one minute.'''
        for s in range(60):
            self.__clock.tick()

##    >>> t = AlarmClock()
##    >>> print(t)
##    16:52:00
##    >>> t.setAlarm(17,0)
##    16:52:00
##    Alarm set for 17:0:00
##    16:52:00
##    16:53:00
##    16:54:00
##    16:55:00
##    16:56:00
##    16:57:00
##    16:58:00
##    16:59:00
##    ********Alarm*********
##    17:00:00
##    ********Alarm*********
##    >>> t.tick()
##    >>> print(t)
##    17:00:01
##    >>> t.tock()
##    >>> print(t)
##    17:01:01
##    >>>

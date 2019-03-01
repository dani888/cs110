# alarm1.py -- an alarm clock inheriting from Clock

from clock import *

import time  

class AlarmClock(Clock):
    '''A (fake) alarm clock.  We say it's fake because it ticks
        a minute every second. Like Clock, this is a 24 hour clock.
    '''
    
    def __init__(self):
        self.nowTime()

    def nowTime(self):
        '''Set our time to now (EST).'''
        t = time.localtime()[3:6]   # t = (hour,min, sec)
        self.set_Clock(t[0],t[1],0) # 

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
                if self.hours() == hour and self.minutes() == minute:
                    # Ring Alarm
                    print "********Alarm*********"
                    print self
                    print "********Alarm*********"
                    return
                else:
                    print(self)
                    time.sleep(1) # 1 second real time = 1 minute fake time.
                    self.tock()

    def tock(self):
        '''Advance one minute.'''
        for s in range(60):
            self.tick()

# danisAlarmClock = AlarmClock()
# danisAlarmClock.setAlarm(16,0)
##    >>> t = AlarmClock()
##    >>> print(t)
##    14:44:00
##    >>> t.setAlarm(14,50)
##    14:44:00
##    Alarm set for 14:50:00
##    14:44:00
##    14:45:00
##    14:46:00
##    14:47:00
##    14:48:00
##    14:49:00
##    ********Alarm*********
##    14:50:00
##    ********Alarm*********
##    >>> t = AlarmClock()
##    >>> print(t)
##    14:44:00
##    >>> t.tick()
##    >>> print(t)
##    14:44:01
##    >>> t.tock()
##    >>> print(t)
##    14:45:01
##    >>> t.tock()
##    >>> print(t)
##    14:46:01
##    >>> t.setAlarm(14,50)
##    14:46:01
##    Alarm set for 14:50:00
##    14:46:01
##    14:47:01
##    14:48:01
##    14:49:01
##    ********Alarm*********
##    14:50:01
##    ********Alarm*********
##    >>> 

from datetime import datetime
import calendar
def changetime(stime):
            dt=datetime.strptime(stime,'%Y-%m-%dT%H:%M:%S')
            #print dt
            return calendar.timegm(datetime.timetuple(dt))*1000
            
print changetime('2014-02-13T00:00:00')
print changetime('2014-02-20T00:00:00')
print changetime('2014-02-28T00:00:00')
print changetime('2014-07-14T00:00:00')

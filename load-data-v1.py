#2/3/16  Changed batch size to 8000
#
#Will iterate through the 13.7m csv file and put into Riak in batches of 500
#SMDE 2/3/16

from riak import RiakClient
from datetime import datetime
import calendar
import csv
def changetime(stime):
            dt=datetime.strptime(stime,'%Y-%m-%dT%H:%M:%S')
            #print dt
            return calendar.timegm(datetime.timetuple(dt))*1000
            
c=RiakClient()
c.ping()


#to load data in the table

totalcount=0
batchcount=0
batchsize=8000
ds=[]
t=c.table('aarhus')
print t


with open('./traffic_feb_june/all-data-2.csv', 'rU') as infile:
    r=csv.reader(infile)
    for l in r:
		if l[0]!='status':
			newl=['1',str(l[3]),changetime(l[5]),int(l[1]),int(l[2]),int(l[4]),int(l[6]),int(l[7]),int(l[8])]
			totalcount=totalcount+1
			#print count
			ds.append(newl)
			batchcount=batchcount+1
			if batchcount==batchsize:
				#add the records to the table
				print "Count at  ", totalcount
				to=t.new(ds)
				print "Created ts object"
				print "Storage result:  ",to.store()
				batchcount=0
				ds=[]       
infile.close()
print "Input file closed"
to=t.new(ds)
print "Storage result:  ",to.store()
print totalcount

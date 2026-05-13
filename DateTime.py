from datetime import date
d = date.fromordinal(738630) # 738630th day after 1. 1. 0001
print (d)
print (d.timetuple())
# Methods related to formatting string output
print (d.isoformat())
print (d.strftime("%d/%m/%y"))
print (d.strftime("%A %d. %B %Y"))
print (d.ctime())

from datetime import *
from dateutil.relativedelta import *

now = datetime.now()

print("Today: " + str(now))

#add 1
now = now + relativedelta(month=1, weeks=1, hour=12)

print("New date using relativedelta: "+ str(now))
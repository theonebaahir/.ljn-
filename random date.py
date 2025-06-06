import random
import time


def get(startDate , enddate  ):
    print("Printing random date between ", startDate, "and" , enddate)
    randome = random.random()
    dateformat = '%m/%d/%Y'
    
    
    starttime = time.mktime(time.strptime(startDate,dateformat)) 
    endtime = time.mktime(time.strptime(startDate,dateformat)) 
    randomtime = starttime + randome * (endtime - starttime)
    randomdate = time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("random date = ", get("1/1/2026", "12/12/2018"))
    
    
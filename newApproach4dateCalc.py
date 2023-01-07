#!/usr/bin/env python3
from datetime import datetime, date, timedelta
import re

#print(datetime.now()) #2023-01-02 20:36:26.176472

#converting STRING into DATE
#print(datetime.strptime('01-02-2023', '%m-%d-%Y'))

{"""
    departure_date = '01-02-2023'
    # arrival_time = '17:50'
    # time_left_4_next = '12:20'
    # arrival_of_next = '16:00'
    # time_left_4_other = '11:33'

    #converting STRING into DATE
    initial = (datetime.strptime(departure_date, '%m-%d-%Y'))
    print(initial)
    _initinal = initial + timedelta(hours=17, minutes=50)
    print(_initinal)
    next_flight = _initinal + timedelta(hours=12, minutes=20)
    print(next_flight)

    #turning DATE into STRING (i.e.: to remove hours + mins)
    str_next_flight = datetime.strftime(next_flight, '%m-%d-%Y')
    #... then STRING into DATE again! LOL
    next_flight_departure = datetime.strptime(str_next_flight, '%m-%d-%Y')
    print(next_flight_departure)
    _next_flight_departure = next_flight_departure + timedelta(hours=16, minutes=0)
    print(_next_flight_departure)
    other_flight = _next_flight_departure + timedelta(hours=11, minutes=33)
    print(other_flight)
"""}


departure_date = '01-02-2023' #STRING

initial = datetime.strptime(departure_date, '%m-%d-%Y') #DATE
next = datetime.strftime(initial + timedelta(hours=17, minutes=50) + timedelta(hours=12, minutes=20), '%m-%d-%Y') #=Sum of date, arrival & connection time

# print(initial)
# print(next)


#origin + arrival + connection

['AM 477', 'AM 628']
['V', 'V']
['IAHMEX', 'MEXSAL']
['12Jan', '12Jan']
['Arrival9:30am', 'Arrival1:10pm']
['Departure7:00am', 'Departure10:45am']
['Layover: 1h 15m in Mexico City']



#Converting strings '13jan', '09dec', '22sep' --> into: <class 'datetime.datetime'> 
_tempdate = ['12Jan', '12Jan'] #[0] —12jan2023
_date_ = datetime.strptime(f"{_tempdate[0]}{datetime.now().year}", '%d%b%Y')


test1 = '01-02-2023'
_arrivals = [re.findall('Arrival.*\d+', x)[0].strip('Arrival') for x in ['Arrival9:30am', 'Arrival13:10pm']] #[30, 10]
arr_h= [re.findall('\d+:', x)[0].strip(':') for x in _arrivals]
arr_m= [re.findall(':\d+', x)[0].strip(':') for x in _arrivals]

layover_h = [re.findall('\d+', x)[0] for x in ['Layover: 1h 15m in Mexico City']]
layover_m = [re.findall('\d+', x)[1] for x in ['Layover: 1h 15m in Mexico City']]
# print(arr_h)
# print(arr_m)
# print(layover_h)
# print(layover_m)



"TODO: turn 04jan into a date. i.e.: '01-04-2023'"

def next_day(first,  AH, AM,  LH, LM):
    initial = datetime.strptime(first, '%m-%d-%Y') #DATE
    posterior = []

    for i, val in enumerate(LH): #limit is set by number of connections
        posterior.append(datetime.strftime(initial + timedelta(hours=int(AH[i]), minutes=int(AM[i])) + timedelta(hours=int(LH[i]), minutes=int(LM[i])), '%m-%d-%Y')) #=Sum of date, arrival & connection time

    return posterior



#print(next_day(test1, arr_h, arr_m, layover_h, layover_m))


def next_day_1(first,  arrivals,  layovers):
    #initial = datetime.strptime(first, '%m-%d-%Y') #DATE
    initial = datetime.strptime(f"{first}{datetime.now().year}", '%b %d%Y')
    _arrivals = [datetime.strftime(datetime.strptime(re.findall("\d+:\d+am|\d+:\d+pm", x)[0],"%I:%M%p"), "%H:%M") for x  in arrivals] #['09:30', '13:10'] from ['Arrival9:30am', 'Arrival1:10pm']

    posterior = [] #departure date of each following flight

    #_arrivals = [re.findall('Arrival.*\d+', x)[0].strip('Arrival') for x in arrivals] #[30, 10]
    AH= [re.findall('\d+:', x)[0].strip(':') for x in _arrivals]
    AM= [re.findall(':\d+', x)[0].strip(':') for x in _arrivals]

    LH = [re.findall('\d+', x)[0] for x in layovers]
    LM = [re.findall('\d+', x)[1] for x in layovers]

    # print(LH)
    # print(LM)
    # print(AH)
    # print(AM)

    for i, val in enumerate(layovers): #limit is set by number of connections
        posterior.append(datetime.strftime(initial + timedelta(hours=int(AH[i]), minutes=int(AM[i])) + timedelta(hours=int(LH[i]), minutes=int(LM[i])), '%m-%d-%Y')) #=Sum of date, arrival & connection time
        initial = datetime.strptime(posterior[i], '%m-%d-%Y') #Next iteration's "initial" is updated

    posterior.sort() #I think it's useless here...
    return posterior

# print(next_day_1(test1, ['Arrival9:30am', 'Arrival1:10pm'] , ['Layover: 1h 15m in Mexico City'])) #10/10

start_date = 'Jan 4' #'01-04-2023'#'Jan 4'
arri = ['Arrival11:25am', 'Arrival8:11am', 'Arrival8:45am']
layo = ['Layover: 17h 35m in Newark', 'Layover: 14h 33m in Dallas']


start_date1 = 'Jan 4' #'02-27-2023'#'Jan 4'
arri1 = ['Arrival1:00am', 'Arrival10:21am']
layo1 = ['Layover: 5h 30m in New York']
other1 = ['JFK']#['Arrives Tue, Feb 28']
cities1 = ['SALJFK', 'JFKPAP']
cities2 = ['SALJFK', 'JFKPAP', 'PAPSJU', 'SJUMIA']
cities3 = ['SAL','JFK', 'JFK','PAP', 'PAP','SJU', 'SJU','MIA']

other2 = ['JFK', 'SJU'] #expected indexes: 1 3

#print([re.findall(other1[0], x) for x in cities1])
print(re.findall(other1[0], "".join(cities1)))
print(re.findall(other1[0], "".join(cities2)))

from collections import Counter

# cntr = Counter(cities3)
#print("".join(cities3)) #len(re.findall('SAL', cities3))
# print(cntr['SJU'])
# cnt = Counter('123111')
# print(cnt['1'])



#this function accepts parameters:
#list → ['SAL','JFK', 'JFK','PAP', 'PAP','SJU', 'SJU','MIA'] Each city!
#list → ['JFK', 'SJU'] Cities in which next flight starts on following day
#returns: [0, 1, 0, 1, 0] a list in which the '1' represent where a day-change occurs
#idea is to update next_day_1() by adding a + timedelta(day=int(newdays[i]))



#Now,this one below may not be the cleanest regex BUT gets the job done:
#    '...\).*\n\nArrives'

def newday_indicator(each_city, flag):
    additional_dates = []

    nodupe = [] #each city appears a single time
    for x in each_city:
        if x not in nodupe:
            nodupe.append(x)


    for x in nodupe:
        #print(each_city.count(x))

        #puts a +1 on every index at which a day-change occurs
        if x in flag:
            additional_dates.append(1)
        else:
            additional_dates.append(0)

    return additional_dates



print(newday_indicator(cities3, other1))



print(next_day_1(start_date, arri , layo))
print(next_day_1(start_date1, arri1 , layo1))






#print(datetime.now())
#print(datetime.now() + timedelta(hours=int('08')))

['4Jan', '5Jan', '5Jan']

#Arrives -------increase a counter and add a whole DAY if for each ---['Arrives Tue, Feb 28']
#---------------- this below catches airport after which date-change occurs. Works fine on regexr.com
#...\).*\n\nArrives

# arrivals = ['Arrival9:30am', 'Arrival1:10pm']
# onelin = [datetime.strftime(datetime.strptime(re.findall("\d+:\d+am|\d+:\d+pm", x)[0],"%I:%M%p"), "%H:%M") for x  in arrivals]
# print(onelin)

# testing = [re.findall("\d+:\d+am|\d+:\d+pm", x)[0] for x in testList] #['9:30am', '1:10pm']
# print(testing)
#
# in_time1 = datetime.strptime(testing[0],"%I:%M%p")
# in_time2 = datetime.strptime(testing[1],"%I:%M%p")
# print(in_time1)
# print(in_time2)
#
# out_time1 = datetime.strftime(in_time1, "%H:%M")
# out_time2 = datetime.strftime(in_time2, "%H:%M")
# print(out_time1)
# print(out_time2)
#










"""
from datetime import datetime
m2 = '1:35 PM'
in_time = datetime.strptime(m2, "%I:%M %p")
out_time = datetime.strftime(in_time, "%H:%M")
print(out_time)
13:35
"""








#my_str = '09-24-2023'  # 👉️ (mm-dd-yyyy)
#date_1 = datetime.strptime(my_str, '%m-%d-%Y')

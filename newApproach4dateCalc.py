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

print(initial)
print(next)


#origin + arrival + connection

['AM 477', 'AM 628']
['V', 'V']
['IAHMEX', 'MEXSAL']
['12Jan', '12Jan']
['Arrival9:30am', 'Arrival1:10pm']
['Departure7:00am', 'Departure10:45am']
['Layover: 1h 15m in Mexico City']


test1 = '01-02-2023'
_arrivals = [re.findall('Arrival.*\d+', x)[0].strip('Arrival') for x in ['Arrival9:30am', 'Arrival13:10pm']] #[30, 10]
arr_h= [re.findall('\d+:', x)[0].strip(':') for x in _arrivals]
arr_m= [re.findall(':\d+', x)[0].strip(':') for x in _arrivals]

layover_h = [re.findall('\d+', x)[0] for x in ['Layover: 1h 15m in Mexico City']]
layover_m = [re.findall('\d+', x)[1] for x in ['Layover: 1h 15m in Mexico City']]
print(arr_h)
print(arr_m)
print(layover_h)
print(layover_m)



"TODO: reduce params to only 3 → str, list, list"

def next_day(first,  AH, AM,  LH, LM):
    initial = datetime.strptime(first, '%m-%d-%Y') #DATE
    posterior = []

    for i, val in enumerate(LH): #limit is set by number of connections
        posterior.append(datetime.strftime(initial + timedelta(hours=int(AH[i]), minutes=int(AM[i])) + timedelta(hours=int(LH[i]), minutes=int(LM[i])), '%m-%d-%Y')) #=Sum of date, arrival & connection time

    return posterior

print(next_day(test1, arr_h, arr_m, layover_h, layover_m))



















#my_str = '09-24-2023'  # 👉️ (mm-dd-yyyy)
#date_1 = datetime.strptime(my_str, '%m-%d-%Y')

#!/usr/bin/env python3
from datetime import datetime, date, timedelta
import re

#print(datetime.now()) #2023-01-02 20:36:26.176472
#print(datetime.strptime('01-02-2023', '%m-%d-%Y')) #converting STRING into DATE

"TODO: turn 04jan into a date. i.e.: '01-04-2023'"

def next_day_1(first,  arrivals,  layovers):

    initial = datetime.strptime(f"{first}{datetime.now().year}", '%b %d%Y')
    _arrivals = [datetime.strftime(datetime.strptime(re.findall("\d+:\d+am|\d+:\d+pm", x)[0],"%I:%M%p"), "%H:%M") for x  in arrivals] #['09:30', '13:10'] from ['Arrival9:30am', 'Arrival1:10pm']

    posterior = [] #departure date of each following flight


    AH= [re.findall('\d+:', x)[0].strip(':') for x in _arrivals]
    AM= [re.findall(':\d+', x)[0].strip(':') for x in _arrivals]

    LH = [re.findall('\d+', x)[0] for x in layovers]
    LM = [re.findall('\d+', x)[1] for x in layovers]

    for i, val in enumerate(layovers): #limit is set by number of connections
        posterior.append(datetime.strftime(initial + timedelta(hours=int(AH[i]), minutes=int(AM[i])) + timedelta(hours=int(LH[i]), minutes=int(LM[i])), '%d%b')) #=Sum of date, arrival & connection time
        initial = datetime.strptime(posterior[i], '%d%b') #Next iteration's "initial" is updated

    #posterior.sort() #I think it's useless here...
    
    return posterior


def newday_indicator(each_city, flag):

    """
        this function accepts parameters:
        list → ['SAL','JFK', 'JFK','PAP', 'PAP','SJU', 'SJU','MIA'] Each city!
        list → ['JFK', 'SJU'] Cities in which next flight starts on following day
        returns: [0, 1, 0, 1, 0] a list in which the '1' represent where a day-change occurs
        idea is to update next_day_1() by adding a + timedelta(day=int(newdays[i]))

        Now,this one below may not be the cleanest regex BUT gets the job done:
        '...\).*\n\nArrives'
    """

    additional_dates = []

    nodupe = [] #each city appears a single time
    for x in each_city:
        if x not in nodupe:
            nodupe.append(x)


    for x in nodupe:

        #puts a +1 on every index at which a day-change occurs
        if x in flag:
            additional_dates.append(1)
        else:
            additional_dates.append(0)

    return additional_dates









['AM 477', 'AM 628']
['V', 'V']
['IAHMEX', 'MEXSAL']
['12Jan', '12Jan']
['Arrival9:30am', 'Arrival1:10pm']
['Departure7:00am', 'Departure10:45am']
['Layover: 1h 15m in Mexico City']


start_date = 'Jan 4' #'01-04-2023'#'Jan 4'
arri = ['Arrival11:25am', 'Arrival8:11am', 'Arrival8:45am']
layo = ['Layover: 17h 35m in Newark', 'Layover: 14h 33m in Dallas']


start_date1 = 'Jan 4' #'02-27-2023'#'Jan 4'
arri1 = ['Arrival1:00am', 'Arrival10:21am']
layo1 = ['Layover: 5h 30m in New York']
other1 = ['JFK'] #['Arrives Tue, Feb 28'] #flight departing from this airport starts next day
cities3 = ['SAL','JFK', 'JFK','PAP', 'PAP','SJU', 'SJU','MIA']


print(next_day_1(start_date,  arri1,  layo1))
print(newday_indicator(cities3, other1)) 



#print([re.findall(other1[0], x) for x in cities1])
# print(re.findall(other1[0], "".join(cities1)))
# print(re.findall(other1[0], "".join(cities2)))







# print(newday_indicator(cities3, other1))



# print(next_day_1(start_date, arri , layo))
# print(next_day_1(start_date1, arri1 , layo1))





def next_day(first,  arrivals,  layovers, cities, nextday_departures):


    additional_dates = []

    nodupe = [] #each city appears a single time
    for x in cities:
        if x not in nodupe:
            nodupe.append(x)


    for x in nodupe:

        #puts a +1 on every index at which a day-change occurs #[0, 1, 0]
        if x in nextday_departures:
            additional_dates.append(1)
        else:
            additional_dates.append(0)
        
    additional_dates.pop(0)

    initial = datetime.strptime(f"{first}{datetime.now().year}", '%b %d%Y')
    _arrivals = [datetime.strftime(datetime.strptime(re.findall("\d+:\d+am|\d+:\d+pm", x)[0],"%I:%M%p"), "%H:%M") for x  in arrivals] #['09:30', '13:10'] from ['Arrival9:30am', 'Arrival1:10pm']

    posterior = [] #departure date of each following flight


    AH= [re.findall('\d+:', x)[0].strip(':') for x in _arrivals]
    AM= [re.findall(':\d+', x)[0].strip(':') for x in _arrivals]

    LH = [re.findall('\d+', x)[0] for x in layovers]
    LM = [re.findall('\d+', x)[1] for x in layovers]

    for i, val in enumerate(layovers): #limit is set by number of connections
        posterior.append(datetime.strftime(initial + timedelta(days=int(additional_dates[i])) + timedelta(hours=int(AH[i]), minutes=int(AM[i])) + timedelta(hours=int(LH[i]), minutes=int(LM[i])), '%d%b')) #=Sum of date, arrival & connection time
        initial = datetime.strptime(posterior[i], '%d%b') #Next iteration's "initial" is updated

    #posterior.sort() #I think it's useless here...
    
    return posterior


print(
    next_day(
        'Jan 4',
        ['Arrival11:25am', 'Arrival8:11am', 'Arrival8:45am'],
        ['Layover: 17h 35m in Newark', 'Layover: 14h 33m in Dallas'],
        ['SAL','JFK', 'JFK','PAP', 'PAP','SJU', 'SJU','MIA'],
        ['JFK']))



print(
    next_day(
        'Jan 12',
        ['Arrival9:55am', 'Arrival1:40pm', 'Arrival6:10pm'],
        ['Layover: 8h 10m in Seattle', 'Layover: 3h 10m in Frankfurt'],
        ['IAH', 'SEA', 'SEA', 'FRA', 'FRA', 'VIE'],
        ['FRA'])) #10/10


print(
    next_day(
        'Jan 4',
        ["Arrival11:25am", "Arrival8:11am", "Arrival8:45am"],
        ["Layover: 17h 35m in Newark", "Layover: 14h 33m in Dallas"],
        ["LHR","EWR","EWR","DFW","DFW","AKL"],
        [])) #10/10




'Alaska Airlines 453'


"Expected: 12 12 13 jan"
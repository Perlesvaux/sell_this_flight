#!/usr/bin/env python3
from datetime import datetime, date, timedelta
import re

#print(datetime.now()) #2023-01-02 20:36:26.176472
#print(datetime.strptime('01-02-2023', '%m-%d-%Y')) #converting STRING into DATE


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


    definitive = []
    posterior = [] #departure date of each following flight

    definitive.append(datetime.strftime(initial, '%b %d'))


    AH= [re.findall('\d+:', x)[0].strip(':') for x in _arrivals]
    AM= [re.findall(':\d+', x)[0].strip(':') for x in _arrivals]

    LH = [re.findall('\d+', x)[0] for x in layovers]
    LM = [re.findall('\d+', x)[1] for x in layovers]

    for i, val in enumerate(layovers): #limit is set by number of connections
        posterior.append(datetime.strftime(initial + timedelta(days=int(additional_dates[i])) + timedelta(hours=int(AH[i]), minutes=int(AM[i])) + timedelta(hours=int(LH[i]), minutes=int(LM[i])), '%d%b')) #=Sum of date, arrival & connection time
        initial = datetime.strptime(posterior[i], '%d%b') #Next iteration's "initial" is updated

    #posterior.sort() #I think it's useless here...
    
    definitive.extend(posterior)
    return definitive



if __name__ == "__main__":

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